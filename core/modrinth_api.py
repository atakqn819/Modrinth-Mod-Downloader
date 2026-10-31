"""
Modrinth API Client & Installer Engine
Handles Modrinth v2 API interaction, downloads, dependency resolution, and mrpack extraction.
"""

import requests
import json
import time
import os
import socket
import zipfile
import io

API_BASE = "https://api.modrinth.com/v2"
DEFAULT_HEADERS = {"User-Agent": "ModrinthUniverseDownloader/1.1.0 (contact@modrinthdownloader.local)"}

class ModrinthAPI:
    def __init__(self, gv="26.3", loader="fabric"):
        self.gv = gv
        self.loader = loader
        self.s = requests.Session()
        self.s.headers.update(DEFAULT_HEADERS)

    @staticmethod
    def check_internet():
        try:
            socket.setdefaulttimeout(3)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("api.modrinth.com", 443))
            return True
        except:
            return False

    def build_facets(self, project_type):
        if project_type == "mod":
            return json.dumps([[f"categories:{self.loader}"], [f"versions:{self.gv}"], ["project_type:mod"]])
        elif project_type == "resourcepack":
            return json.dumps([[f"versions:{self.gv}"], ["project_type:resourcepack"]])
        elif project_type == "datapack":
            return json.dumps([[f"versions:{self.gv}"], ["project_type:datapack"]])
        elif project_type == "shader":
            return json.dumps([["project_type:shader"]])
        elif project_type == "modpack":
            return json.dumps([[f"categories:{self.loader}"], [f"versions:{self.gv}"], ["project_type:modpack"]])
        return json.dumps([[f"project_type:{project_type}"]])

    def fetch_page(self, project_type, page_index=0, limit=100):
        facets = self.build_facets(project_type)
        r = self.s.get(
            f"{API_BASE}/search",
            params={"facets": facets, "index": "downloads", "limit": limit, "offset": page_index * limit},
            timeout=25
        )
        r.raise_for_status()
        return r.json()

    def get_project_details(self, pid_or_slug):
        try:
            r = self.s.get(f"{API_BASE}/project/{pid_or_slug}", timeout=15)
            if r.status_code == 200:
                return r.json()
        except:
            pass
        return None

    def get_compatible_version(self, pid_or_slug, project_type="mod"):
        try:
            params = {}
            if project_type in ("mod", "modpack"):
                params["loaders"] = json.dumps([self.loader])
                params["game_versions"] = json.dumps([self.gv])
            elif project_type in ("resourcepack", "datapack"):
                params["game_versions"] = json.dumps([self.gv])
                
            r = self.s.get(f"{API_BASE}/project/{pid_or_slug}/version", params=params, timeout=20)
            if r.status_code == 200:
                versions = r.json()
                if versions:
                    return versions[0]
            # Fallback
            r2 = self.s.get(f"{API_BASE}/project/{pid_or_slug}/version", timeout=20)
            if r2.status_code == 200:
                v2 = r2.json()
                return v2[0] if v2 else None
        except:
            pass
        return None

    def get_version_by_id(self, vid):
        try:
            r = self.s.get(f"{API_BASE}/version/{vid}", timeout=20)
            if r.status_code == 200:
                return r.json()
        except:
            pass
        return None

    def resolve_dependencies(self, ver, resolved=None, log_cb=None):
        if resolved is None:
            resolved = {}
        for dep in ver.get("dependencies", []):
            if dep.get("dependency_type") != "required":
                continue
            pid, vid = dep.get("project_id"), dep.get("version_id")
            if not pid and vid:
                dv_temp = self.get_version_by_id(vid)
                if dv_temp:
                    pid = dv_temp.get("project_id")
            if not pid or pid in resolved:
                continue
            dv = self.get_version_by_id(vid) if vid else None
            if not dv:
                dv = self.get_compatible_version(pid)
            if not dv:
                continue
            pf = self.get_primary_file(dv)
            if pf:
                info = self.get_project_details(pid)
                title = info.get("title", pid) if info else pid
                resolved[pid] = {
                    "url": pf["url"],
                    "filename": pf["filename"],
                    "title": title
                }
                if log_cb:
                    log_cb(f"  📦 Dependency: {title}")
                time.sleep(0.1)
                self.resolve_dependencies(dv, resolved, log_cb)
        return resolved

    @staticmethod
    def get_primary_file(ver):
        files = ver.get("files", [])
        for f in files:
            if f.get("primary"):
                return f
        return files[0] if files else None

    def download_file(self, url, target_path, progress_cb=None):
        try:
            os.makedirs(os.path.dirname(target_path) or ".", exist_ok=True)
            r = self.s.get(url, stream=True, timeout=120)
            r.raise_for_status()
            total_size = int(r.headers.get("content-length", 0))
            downloaded = 0
            with open(target_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=16384):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if progress_cb and total_size > 0:
                            progress_cb(downloaded, total_size)
            return True
        except Exception:
            return False

    def download_bytes(self, url):
        try:
            r = self.s.get(url, timeout=180)
            r.raise_for_status()
            return r.content
        except:
            return None

    def install_mrpack(self, mrpack_bytes, target_dir, log_cb=None, is_cancelled=None):
        try:
            with zipfile.ZipFile(io.BytesIO(mrpack_bytes)) as zf:
                with zf.open("modrinth.index.json") as f:
                    index_data = json.load(f)

                files = index_data.get("files", [])
                if log_cb:
                    log_cb(f"  📦 Found {len(files)} mod files in modpack")

                installed_mods = 0
                for i, mf in enumerate(files, 1):
                    if is_cancelled and is_cancelled():
                        return False, "Cancelled by user"

                    rel_path = mf.get("path", "")
                    downloads = mf.get("downloads", [])
                    if not rel_path or not downloads:
                        continue

                    dest = os.path.join(target_dir, rel_path)
                    if os.path.exists(dest):
                        continue

                    fname = os.path.basename(rel_path)
                    if log_cb:
                        log_cb(f"    ⬇ [{i}/{len(files)}] {fname}")

                    if self.download_file(downloads[0], dest):
                        installed_mods += 1
                    time.sleep(0.05)

                for item in zf.namelist():
                    if item.startswith("overrides/") and not item.endswith("/"):
                        rel = item[len("overrides/"):]
                        dest = os.path.join(target_dir, rel)
                        os.makedirs(os.path.dirname(dest), exist_ok=True)
                        with zf.open(item) as src, open(dest, "wb") as dst:
                            dst.write(src.read())

                    elif item.startswith("client-overrides/") and not item.endswith("/"):
                        rel = item[len("client-overrides/"):]
                        dest = os.path.join(target_dir, rel)
                        os.makedirs(os.path.dirname(dest), exist_ok=True)
                        with zf.open(item) as src, open(dest, "wb") as dst:
                            dst.write(src.read())

                deps_info = index_data.get("dependencies", {})
                mc_ver = deps_info.get("minecraft", "?")
                return True, f"Successfully installed ({installed_mods} mods, MC {mc_ver})"
        except Exception as e:
            return False, str(e)
