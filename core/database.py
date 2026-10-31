"""
Database Manager for Modrinth Downloader
Uses SQLite with WAL mode for ultra-fast performance, caching, and persistence.
"""

import sqlite3
import json
import os
import sys
import threading
from core.category_classifier import classify_categories

def resolve_db_path():
    # Check PyInstaller extracted dir if packaged
    base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data_db = os.path.join(base_dir, "data", "modrinth_catalog.db")
    if os.path.exists(data_db):
        return data_db
    local_db = os.path.join(base_dir, "modrinth_catalog.db")
    if os.path.exists(local_db):
        return local_db
    # Fallback to local data dir
    os.makedirs(os.path.join(base_dir, "data"), exist_ok=True)
    return data_db

DB_PATH = resolve_db_path()

class Database:
    _instance = None
    _lock = threading.Lock()

    def __init__(self, db_path=None):
        self.db_path = db_path or resolve_db_path()
        self._local = threading.local()
        self.init_db()

    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls()
            return cls._instance

    def get_conn(self):
        if not hasattr(self._local, "conn") or self._local.conn is None:
            self._local.conn = sqlite3.connect(self.db_path, check_same_thread=False)
            self._local.conn.row_factory = sqlite3.Row
            cur = self._local.conn.cursor()
            cur.execute("PRAGMA journal_mode = WAL")
            cur.execute("PRAGMA synchronous = NORMAL")
            cur.execute("PRAGMA cache_size = -64000") # 64MB cache
            cur.close()
        return self._local.conn

    def init_db(self):
        conn = self.get_conn()
        cur = conn.cursor()
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS items (
                slug TEXT,
                project_id TEXT,
                project_type TEXT,
                title TEXT,
                author TEXT,
                description TEXT,
                categories TEXT,
                primary_category TEXT,
                downloads INTEGER,
                follows INTEGER,
                icon_url TEXT,
                date_modified TEXT,
                versions TEXT,
                loaders TEXT,
                client_side TEXT,
                server_side TEXT,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (slug, project_type)
            )
        """)

        cur.execute("CREATE INDEX IF NOT EXISTS idx_items_type ON items (project_type, downloads DESC)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_items_cat ON items (project_type, primary_category)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_items_title ON items (title)")

        cur.execute("""
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """)
        conn.commit()

    def upsert_batch(self, items_list, project_type):
        if not items_list:
            return 0
        conn = self.get_conn()
        cur = conn.cursor()
        data = []
        for m in items_list:
            slug = m.get("slug")
            if not slug:
                continue
            raw_cats = m.get("categories", [])
            title = m.get("title", slug)
            desc = m.get("description", "")
            clean_cats, primary_cat = classify_categories(project_type, raw_cats, title, desc)
            data.append((
                slug,
                m.get("project_id", slug),
                project_type,
                title,
                m.get("author", "Unknown"),
                desc,
                json.dumps(clean_cats),
                primary_cat,
                int(m.get("downloads", 0)),
                int(m.get("follows", 0)),
                m.get("icon_url", ""),
                m.get("date_modified", ""),
                json.dumps(m.get("versions", [])),
                json.dumps(m.get("loaders", [])),
                m.get("client_side", "optional"),
                m.get("server_side", "optional")
            ))
        
        cur.executemany("""
            INSERT INTO items (
                slug, project_id, project_type, title, author, description,
                categories, primary_category, downloads, follows, icon_url,
                date_modified, versions, loaders, client_side, server_side, last_updated
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(slug, project_type) DO UPDATE SET
                title=excluded.title,
                author=excluded.author,
                description=excluded.description,
                categories=excluded.categories,
                primary_category=excluded.primary_category,
                downloads=excluded.downloads,
                follows=excluded.follows,
                icon_url=excluded.icon_url,
                date_modified=excluded.date_modified,
                versions=excluded.versions,
                loaders=excluded.loaders,
                last_updated=CURRENT_TIMESTAMP
        """, data)
        conn.commit()
        return len(data)

    def query_items(self, project_type, search="", category="All", sort_by="downloads", sort_desc=True, limit=100, offset=0):
        conn = self.get_conn()
        cur = conn.cursor()

        where_clauses = ["project_type = ?"]
        params = [project_type]

        if category and category not in ("All", "Tümü", "Tous", "Alle", "Todos", "Tutti", "All Categories"):
            where_clauses.append("(primary_category = ? OR categories LIKE ?)")
            params.extend([category, f'%"{category}"%'])

        if search:
            search_pattern = f"%{search.strip().lower()}%"
            where_clauses.append("(LOWER(title) LIKE ? OR LOWER(description) LIKE ? OR LOWER(author) LIKE ? OR LOWER(slug) LIKE ?)")
            params.extend([search_pattern, search_pattern, search_pattern, search_pattern])

        where_sql = " AND ".join(where_clauses)

        col_map = {
            "downloads": "downloads",
            "name": "LOWER(title)",
            "title": "LOWER(title)",
            "author": "LOWER(author)",
            "date": "date_modified",
            "date_modified": "date_modified",
            "primary_category": "primary_category"
        }
        order_col = col_map.get(sort_by, "downloads")
        order_dir = "DESC" if sort_desc else "ASC"

        sql = f"""
            SELECT * FROM items
            WHERE {where_sql}
            ORDER BY {order_col} {order_dir}
            LIMIT ? OFFSET ?
        """
        params.extend([limit, offset])

        cur.execute(sql, params)
        rows = cur.fetchall()

        result = []
        for r in rows:
            d = dict(r)
            try:
                d["categories"] = json.loads(d["categories"])
            except:
                d["categories"] = [d["primary_category"]]
            result.append(d)
        return result

    def get_count(self, project_type, search="", category="All"):
        conn = self.get_conn()
        cur = conn.cursor()

        where_clauses = ["project_type = ?"]
        params = [project_type]

        if category and category not in ("All", "Tümü", "Tous", "Alle", "Todos", "Tutti", "All Categories"):
            where_clauses.append("(primary_category = ? OR categories LIKE ?)")
            params.extend([category, f'%"{category}"%'])

        if search:
            search_pattern = f"%{search.strip().lower()}%"
            where_clauses.append("(LOWER(title) LIKE ? OR LOWER(description) LIKE ? OR LOWER(author) LIKE ? OR LOWER(slug) LIKE ?)")
            params.extend([search_pattern, search_pattern, search_pattern, search_pattern])

        where_sql = " AND ".join(where_clauses)
        cur.execute(f"SELECT COUNT(*) FROM items WHERE {where_sql}", params)
        return cur.fetchone()[0]

    def get_categories(self, project_type):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("""
            SELECT DISTINCT primary_category FROM items
            WHERE project_type = ? AND primary_category IS NOT NULL AND primary_category != ''
            ORDER BY primary_category ASC
        """, (project_type,))
        return [r[0] for r in cur.fetchall()]

    def get_item(self, slug, project_type=None):
        conn = self.get_conn()
        cur = conn.cursor()
        if project_type:
            cur.execute("SELECT * FROM items WHERE slug = ? AND project_type = ? LIMIT 1", (slug, project_type))
        else:
            cur.execute("SELECT * FROM items WHERE slug = ? LIMIT 1", (slug,))
        row = cur.fetchone()
        if not row:
            return None
        d = dict(row)
        try:
            d["categories"] = json.loads(d["categories"])
        except:
            d["categories"] = [d["primary_category"]]
        return d

    def get_setting(self, key, default=None):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT value FROM settings WHERE key = ?", (key,))
        row = cur.fetchone()
        return row[0] if row else default

    def set_setting(self, key, value):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO settings (key, value) VALUES (?, ?)
            ON CONFLICT(key) DO UPDATE SET value = excluded.value
        """, (key, str(value)))
        conn.commit()
