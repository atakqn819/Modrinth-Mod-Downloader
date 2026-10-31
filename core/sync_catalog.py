"""
Catalog Synchronizer
Fetches all pages requested:
- Mods: 90 pages
- Resourcepacks: 65 pages
- Datapacks: 29 pages
- Shaders: 11 pages
- Modpacks: 8 pages
Populates local SQLite database.
"""

import time
import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

from core.modrinth_api import ModrinthAPI
from core.database import Database

CONFIG = [
    ("mod", 90),
    ("resourcepack", 65),
    ("datapack", 29),
    ("shader", 11),
    ("modpack", 8),
]

def sync_all(callback=None):
    api = ModrinthAPI()
    db = Database.get_instance()
    
    total_added = 0
    for ptype, max_pages in CONFIG:
        type_added = 0
        for page in range(max_pages):
            try:
                data = api.fetch_page(ptype, page_index=page, limit=100)
                hits = data.get("hits", [])
                if not hits:
                    break
                count = db.upsert_batch(hits, ptype)
                type_added += count
                total_added += count
                if callback:
                    callback(ptype, page + 1, max_pages, type_added, total_added)
                time.sleep(0.18)
            except Exception as e:
                time.sleep(0.5)

    return total_added

if __name__ == "__main__":
    sync_all()
