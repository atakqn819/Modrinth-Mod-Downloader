"""
Minecraft Directory Detector
Auto-detects standard .minecraft and launcher instance paths.
Note: Modpacks do NOT use auto-detection (user selects custom instance folder).
"""

import os
import glob

def get_minecraft_base_dir():
    appdata = os.environ.get("APPDATA", "")
    if appdata:
        mc_standard = os.path.join(appdata, ".minecraft")
        if os.path.exists(mc_standard):
            return mc_standard

    # Check Modrinth App instances
    mr_app = os.path.join(appdata, "com.modrinth.theseus", "profiles")
    if os.path.exists(mr_app):
        profiles = [p for p in glob.glob(os.path.join(mr_app, "*")) if os.path.isdir(p)]
        if profiles:
            profiles.sort(key=os.path.getmtime, reverse=True)
            return profiles[0]

    # Check PrismLauncher
    prism = os.path.join(appdata, "PrismLauncher", "instances")
    if os.path.exists(prism):
        instances = [p for p in glob.glob(os.path.join(prism, "*", ".minecraft")) if os.path.isdir(p)]
        if instances:
            instances.sort(key=os.path.getmtime, reverse=True)
            return instances[0]

    return os.path.join(appdata, ".minecraft") if appdata else os.path.abspath(".minecraft")

def get_auto_path(project_type):
    """
    Returns auto-detected path for mods, resourcepacks, shaders, datapacks.
    For modpacks, returns empty string as user manual selection is required.
    """
    if project_type == "modpack":
        return ""  # User requirement: no auto-detect for modpacks

    base = get_minecraft_base_dir()

    if project_type == "mod":
        return os.path.join(base, "mods")
    elif project_type == "resourcepack":
        return os.path.join(base, "resourcepacks")
    elif project_type == "shader":
        return os.path.join(base, "shaderpacks")
    elif project_type == "datapack":
        saves_dir = os.path.join(base, "saves")
        if os.path.exists(saves_dir):
            worlds = [w for w in glob.glob(os.path.join(saves_dir, "*")) if os.path.isdir(w)]
            if worlds:
                worlds.sort(key=os.path.getmtime, reverse=True)
                return os.path.join(worlds[0], "datapacks")
        return os.path.join(base, "datapacks")

    return os.path.join(base, "downloads")

def ensure_directory(path):
    if not path or not path.strip():
        return False
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except:
        return False
