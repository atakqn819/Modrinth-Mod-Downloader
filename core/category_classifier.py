"""
Category Classifier & Normalizer for Modrinth Downloader
Ensures every single item belongs to at least one valid, clean category.
"""

MOD_CATEGORIES = [
    "adventure", "cursed", "decoration", "economy", "equipment", "food",
    "game-mechanics", "library", "magic", "management", "minigame", "mobs",
    "optimization", "social", "storage", "technology", "transportation",
    "utility", "worldgen"
]

RESOURCEPACK_CATEGORIES = [
    "16x", "32x", "64x", "128x", "256x", "512x+", "audio", "blocks",
    "entities", "environment", "equipment", "fonts", "gui", "items",
    "locale", "models", "modded", "realistic", "simplistic", "themed",
    "tweaks", "utility", "vanilla-like"
]

DATAPACK_CATEGORIES = [
    "adventure", "cursed", "decoration", "economy", "equipment", "food",
    "game-mechanics", "magic", "management", "minigame", "mobs",
    "optimization", "storage", "technology", "transportation",
    "tweaks", "utility", "worldgen"
]

SHADER_CATEGORIES = [
    "atmosphere", "bloom", "cartoon", "colored-lighting", "cursed",
    "fantasy", "foliage", "high", "low", "medium", "path-tracing",
    "pbr", "potato", "realistic", "reflections", "screenshot",
    "semi-realistic", "shadows", "vanilla-like"
]

MODPACK_CATEGORIES = [
    "adventure", "challenging", "combat", "kitchen-sink", "lightweight",
    "magic", "multiplayer", "optimization", "quests", "technology"
]

KEYWORD_MAPPINGS = [
    (["fps", "optimi", "perform", "cull", "fast", "speed", "memory", "lag", "sodium", "lithium", "phosphor", "ferrite", "entityculling"], "optimization"),
    (["biome", "terrain", "world", "dimension", "cave", "structure", "dungeon", "generation"], "worldgen"),
    (["chest", "storage", "bag", "backpack", "inventory", "drawer", "crate"], "storage"),
    (["sword", "weapon", "armor", "shield", "bow", "tool", "gear", "equipment"], "equipment"),
    (["magic", "spell", "wizard", "wand", "enchant", "alchemy", "sorcery"], "magic"),
    (["tech", "energy", "machine", "pipe", "wire", "power", "generator", "automation", "cable"], "technology"),
    (["food", "crop", "farm", "cook", "eat", "apple", "bread", "meal", "farmer"], "food"),
    (["mob", "creature", "boss", "animal", "monster", "entity", "npc", "villager", "zombie"], "mobs"),
    (["chair", "table", "furniture", "decor", "light", "block", "aesthetic", "glass", "paint"], "decoration"),
    (["gui", "hud", "menu", "ui", "interface", "display", "overlay", "tooltip", "crosshair"], "management"),
    (["quest", "rpg", "dungeon", "level", "skill", "story", "adventure", "explore"], "adventure"),
    (["chat", "voice", "multiplayer", "friend", "party", "server", "ping", "social"], "social"),
    (["boat", "cart", "train", "flight", "elytra", "vehicle", "mount", "travel", "transport"], "transportation"),
    (["economy", "shop", "coin", "trade", "money", "bank", "currency"], "economy"),
    (["api", "library", "lib", "core", "dependency", "framework"], "library"),
]

def classify_categories(project_type, raw_categories, title="", description=""):
    loaders_to_strip = {"fabric", "quilt", "forge", "neoforge", "liteloader", "rift", "modloader"}
    clean_cats = [c for c in raw_categories if c.lower() not in loaders_to_strip]
    
    if clean_cats:
        return clean_cats, clean_cats[0]
    
    combined_text = f"{title} {description}".lower()
    for keywords, category in KEYWORD_MAPPINGS:
        if any(kw in combined_text for kw in keywords):
            return [category], category
            
    default_cat = {
        "mod": "utility",
        "resourcepack": "tweaks",
        "datapack": "game-mechanics",
        "shader": "atmosphere",
        "modpack": "adventure"
    }.get(project_type, "utility")
    
    return [default_cat], default_cat
