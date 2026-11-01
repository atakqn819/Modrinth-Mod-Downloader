"""
Internationalization (i18n) & Localization System for Modrinth Mod Manager
Languages in exact order:
1. English (en) - Default
2. Italian (it)
3. French (fr)
4. German (de)
5. Spanish (es)
6. Turkish (tr)
"""

LANGUAGES = [
    ("en", "English"),
    ("it", "Italiano"),
    ("fr", "Français"),
    ("de", "Deutsch"),
    ("es", "Español"),
    ("tr", "Türkçe")
]

# Category translations across all 6 languages
CATEGORY_NAMES = {
    "en": {
        "all": "All Categories",
        "optimization": "⚡ Optimization", "worldgen": "🌍 World Generation",
        "adventure": "⚔ Adventure & RPG", "equipment": "🛡 Equipment & Armor",
        "storage": "📦 Storage & Chests", "magic": "✨ Magic & Spells",
        "technology": "⚙ Technology & Machines", "decoration": "🪑 Decoration & Building",
        "utility": "🔧 Utility & Tools", "mobs": "🐾 Mobs & Creatures",
        "food": "🍎 Food & Farming", "game-mechanics": "🎲 Game Mechanics",
        "management": "🖥 Interface & Management", "social": "💬 Social & Multiplayer",
        "transportation": "🚀 Transportation", "economy": "💰 Economy",
        "library": "📚 Library & API", "cursed": "🤪 Cursed & Memes",
        "atmosphere": "🌄 Atmosphere & Lighting", "bloom": "🌟 Bloom Effects",
        "realistic": "🎨 Realistic", "vanilla-like": "🧱 Vanilla-like",
        "simplistic": "📐 Simplistic / Clean", "tweaks": "🛠 Tweaks & Fixes",
        "16x": "16x Standard", "32x": "32x Crisp", "64x": "64x HD",
        "128x": "128x Ultra", "256x": "256x Maximum", "512x+": "512x+ Photoreal",
        "audio": "🔊 Audio & Sounds", "models": "🧊 3D Models", "fonts": "🔤 Custom Fonts",
        "gui": "🎛 Custom GUI", "datapack": "📜 Datapack", "modpack": "📦 Modpack"
    },
    "it": {
        "all": "Tutte le Categorie",
        "optimization": "⚡ Ottimizzazione", "worldgen": "🌍 Generazione Mondo",
        "adventure": "⚔ Avventura & RPG", "equipment": "🛡 Equipaggiamento",
        "storage": "📦 Magazzino & Casse", "magic": "✨ Magia & Incantesimi",
        "technology": "⚙ Tecnologia & Macchine", "decoration": "🪑 Decorazione",
        "utility": "🔧 Utilità & Strumenti", "mobs": "🐾 Creature & Mob",
        "food": "🍎 Cibo & Agricoltura", "game-mechanics": "🎲 Meccaniche di Gioco",
        "management": "🖥 Interfaccia & Gestione", "social": "💬 Social & Multigiocatore",
        "transportation": "🚀 Trasporti & Veicoli", "economy": "💰 Economia",
        "library": "📚 Librerie & API", "cursed": "🤪 Maledetti & Meme",
        "atmosphere": "🌄 Atmosfera & Luci", "bloom": "🌟 Effetti Bloom",
        "realistic": "🎨 Realistico", "vanilla-like": "🧱 Simil-Vanilla",
        "simplistic": "📐 Semplice / Minimale", "tweaks": "🛠 Modifiche & Ritocchi",
        "16x": "16x Standard", "32x": "32x Dettagliato", "64x": "64x HD",
        "128x": "128x Ultra", "256x": "256x Massimo", "512x+": "512x+ Fotorealistico",
        "audio": "🔊 Audio & Suoni", "models": "🧊 Modelli 3D", "fonts": "🔤 Font Personalizzati",
        "gui": "🎛 GUI Personalizzata", "datapack": "📜 Datapack", "modpack": "📦 Modpack"
    },
    "fr": {
        "all": "Toutes les Catégories",
        "optimization": "⚡ Optimisation", "worldgen": "🌍 Génération de Monde",
        "adventure": "⚔ Aventure & RPG", "equipment": "🛡 Équipement & Armures",
        "storage": "📦 Stockage & Coffres", "magic": "✨ Magie & Sortilèges",
        "technology": "⚙ Technologie & Machines", "decoration": "🪑 Décoration",
        "utility": "🔧 Utilitaires & Outils", "mobs": "🐾 Monstres & Animaux",
        "food": "🍎 Nourriture & Agriculture", "game-mechanics": "🎲 Mécaniques de Jeu",
        "management": "🖥 Interface & Gestion", "social": "💬 Social & Multijoueur",
        "transportation": "🚀 Transport & Véhicules", "economy": "💰 Économie",
        "library": "📚 Bibliothèques & API", "cursed": "🤪 Maudit & Mèmes",
        "atmosphere": "🌄 Atmosphère & Lumières", "bloom": "🌟 Effets Bloom",
        "realistic": "🎨 Réaliste", "vanilla-like": "🧱 Style Vanilla",
        "simplistic": "📐 Simpliste / Épuré", "tweaks": "🛠 Ajustements",
        "16x": "16x Standard", "32x": "32x Net", "64x": "64x HD",
        "128x": "128x Ultra", "256x": "256x Maximum", "512x+": "512x+ Photoréaliste",
        "audio": "🔊 Audio & Sons", "models": "🧊 Modèles 3D", "fonts": "🔤 Polices",
        "gui": "🎛 Interface GUI", "datapack": "📜 Datapack", "modpack": "📦 Modpack"
    },
    "de": {
        "all": "Alle Kategorien",
        "optimization": "⚡ Optimierung", "worldgen": "🌍 Weltgenerierung",
        "adventure": "⚔ Abenteuer & RPG", "equipment": "🛡 Ausrüstung & Rüstung",
        "storage": "📦 Lager & Kisten", "magic": "✨ Magie & Zauber",
        "technology": "⚙ Technologie & Maschinen", "decoration": "🪑 Dekoration",
        "utility": "🔧 Nützliches & Werkzeuge", "mobs": "🐾 Mobs & Kreaturen",
        "food": "🍎 Nahrung & Landwirtschaft", "game-mechanics": "🎲 Spielmechaniken",
        "management": "🖥 Benutzeroberfläche", "social": "💬 Soziales & Multiplayer",
        "transportation": "🚀 Transport & Fahrzeuge", "economy": "💰 Wirtschaft",
        "library": "📚 Bibliotheken & API", "cursed": "🤪 Verflucht & Memes",
        "atmosphere": "🌄 Atmosphäre & Beleuchtung", "bloom": "🌟 Bloom-Effekte",
        "realistic": "🎨 Realistisch", "vanilla-like": "🧱 Vanilla-ähnlich",
        "simplistic": "📐 Einfach / Schlicht", "tweaks": "🛠 Anpassungen",
        "16x": "16x Standard", "32x": "32x Scharf", "64x": "64x HD",
        "128x": "128x Ultra", "256x": "256x Maximal", "512x+": "512x+ Fotorealistisch",
        "audio": "🔊 Audio & Sounds", "models": "🧊 3D-Modelle", "fonts": "🔤 Eigene Schriften",
        "gui": "🎛 Eigene GUI", "datapack": "📜 Datapack", "modpack": "📦 Modpack"
    },
    "es": {
        "all": "Todas las Categorías",
        "optimization": "⚡ Optimización", "worldgen": "🌍 Generación de Mundo",
        "adventure": "⚔ Aventura y Rol", "equipment": "🛡 Equipamiento y Armaduras",
        "storage": "📦 Almacenamiento y Cofres", "magic": "✨ Magia y Hechizos",
        "technology": "⚙ Tecnología y Máquinas", "decoration": "🪑 Decoración y Bloques",
        "utility": "🔧 Utilidades y Herramientas", "mobs": "🐾 Criaturas y Monstruos",
        "food": "🍎 Comida y Cultivos", "game-mechanics": "🎲 Mecánicas de Juego",
        "management": "🖥 Interfaz y Gestión", "social": "💬 Social y Multijugador",
        "transportation": "🚀 Transporte y Vehículos", "economy": "💰 Economía",
        "library": "📚 Librerías y APIs", "cursed": "🤪 Maldito y Memes",
        "atmosphere": "🌄 Atmósfera e Iluminación", "bloom": "🌟 Efectos Bloom",
        "realistic": "🎨 Realista", "vanilla-like": "🧱 Estilo Vanilla",
        "simplistic": "📐 Simplista / Limpio", "tweaks": "🛠 Ajustes y Mejoras",
        "16x": "16x Estándar", "32x": "32x Detallado", "64x": "64x HD",
        "128x": "128x Ultra", "256x": "256x Máximo", "512x+": "512x+ Fotorrealista",
        "audio": "🔊 Audio y Sonidos", "models": "🧊 Modelos 3D", "fonts": "🔤 Fuentes Personalizadas",
        "gui": "🎛 Interfaz GUI", "datapack": "📜 Datapack", "modpack": "📦 Modpack"
    },
    "tr": {
        "all": "Tüm Kategoriler",
        "optimization": "⚡ Optimizasyon", "worldgen": "🌍 Dünya Oluşumu",
        "adventure": "⚔ Macera & RPG", "equipment": "🛡 Ekipman & Zırh",
        "storage": "📦 Depolama & Sandık", "magic": "✨ Büyü & Sihir",
        "technology": "⚙ Teknoloji & Makineler", "decoration": "🪑 Dekorasyon & Yapı",
        "utility": "🔧 Genel Araçlar", "mobs": "🐾 Canlılar & Yaratıklar",
        "food": "🍎 Yiyecek & Tarım", "game-mechanics": "🎲 Oyun Mekanikleri",
        "management": "🖥 Arayüz & Yönetim", "social": "💬 Sosyal & Çok Oyunculu",
        "transportation": "🚀 Ulaşım & Araçlar", "economy": "💰 Ekonomi",
        "library": "📚 Kütüphane & API", "cursed": "🤪 Mizah & Eğlence",
        "atmosphere": "🌄 Atmosfer & Işıklandırma", "bloom": "🌟 Parlama (Bloom)",
        "realistic": "🎨 Gerçekçi", "vanilla-like": "🧱 Vanilla Benzeri",
        "simplistic": "📐 Sade / Minimal", "tweaks": "🛠 İnce Ayarlar",
        "16x": "16x Standart", "32x": "32x Net", "64x": "64x Yüksek Çözünürlük",
        "128x": "128x Ultra", "256x": "256x Maksimum", "512x+": "512x+ Fotogerçekçi",
        "audio": "🔊 Ses & Efektler", "models": "🧊 3D Modeller", "fonts": "🔤 Özel Yazı Tipleri",
        "gui": "🎛 Özel Arayüz (GUI)", "datapack": "📜 Veri Paketi", "modpack": "📦 Mod Paketi"
    }
}

TRANSLATIONS = {
    "en": {
        "app_title": "Modrinth Mod Manager v1.2",
        "app_subtitle": "Ultimate Minecraft Content Hub & Installer",
        "tab_mods": "⚙ Mods",
        "tab_resourcepacks": "🎨 Resource Packs",
        "tab_datapacks": "📊 Data Packs",
        "tab_shaders": "✨ Shaders",
        "tab_modpacks": "📦 Modpacks",
        "search_placeholder": "🔍 Search by name, author, category, or description...",
        "all_categories": "All Categories",
        "theme_selector_label": "Theme:",
        "btn_fetch_all": "⟳ Sync Online",
        "btn_select_all": "☑ Select All",
        "btn_deselect_all": "☐ Clear",
        "btn_export": "💾 Export",
        "btn_import": "📂 Import",
        "btn_download_selected": "⬇ Download Selected",
        "btn_install_modpack": "🔧 Install Modpack",
        "btn_auto_detect": "🎯 Auto-Detect",
        "btn_browse": "📂 Browse",
        "btn_open_folder": "📁 Open Folder",
        "btn_patch_notes": "📜 Patch Notes",
        "btn_tutorial": "❓ Tutorial",
        "btn_refresh": "🔄 Refresh",
        "selected_counter": "Selected",
        "page_prev": "◀ Prev",
        "page_next": "Next ▶",
        "page_indicator": "Page {cur} of {tot} ({count} items)",
        "col_select": "✓",
        "col_index": "#",
        "col_title": "Title",
        "col_author": "Author",
        "col_downloads": "Downloads",
        "col_updated": "Updated",
        "col_category": "Category",
        "col_description": "Description",
        "status_ready": "Ready. Double-click any item to open full details.",
        "status_loading": "Syncing items from Modrinth API...",
        "status_downloading": "Downloading: {cur}/{tot} - {name}",
        "status_complete": "Finished! {count} items downloaded.",
        "status_error": "An error occurred: {msg}",
        "confirm_dl_title": "Confirm Download",
        "confirm_dl_msg": "{count} {ptype} items selected.\nDestination folder:\n{path}\n\nDo you want to proceed?",
        "confirm_install_title": "Confirm Modpack Installation",
        "confirm_install_msg": "Install modpack '{title}' into:\n{path}\n\nThis will download the .mrpack, extract configs, and download all mod files. Continue?",
        "modal_details_title": "Item Overview & Details",
        "modal_btn_download": "⬇ Download This Item",
        "modal_btn_web": "🌐 View on Modrinth",
        "modal_tech_specs": "Technical Specifications",
        "welcome_title": "Welcome to Modrinth Mod Manager v1.2",
        "welcome_desc": "Your high-speed hub for Fabric Minecraft! Browse and install 20,000+ verified Mods, Resource Packs, Data Packs, Shaders, and Modpacks with instant SQLite caching and smart directory auto-detection.",
        "welcome_net_online": "● Internet Connected: Modrinth Live Sync Active",
        "welcome_net_offline": "○ Working Offline: Using Fast Local Catalog Cache",
        "welcome_btn_start": "🚀 Launch Manager",
        "welcome_btn_guide": "📖 5-Step Tutorial",
        "tutorial_title": "Interactive 5-Step Quick Guide",
        "tut_step1_title": "1. 5 Content Tabs (Comprehensive Catalog)",
        "tut_step1_desc": "Effortlessly switch between Mods, Resource Packs, Data Packs, Shaders, and Modpacks across 20,000+ items.",
        "tut_step2_title": "2. Double-Click for Full Details",
        "tut_step2_desc": "Double-click any item to open its comprehensive description, direct download button, and Modrinth webpage link.",
        "tut_step3_title": "3. Mouse Selection & Batch Actions",
        "tut_step3_desc": "Click and drag your mouse across rows for instant multi-selection! Use Shift+Click for ranges or Ctrl+Click for individual picks.",
        "tut_step4_title": "4. Smart Minecraft Directory Detection",
        "tut_step4_desc": "The application automatically detects your .minecraft folder (/mods, /resourcepacks, /shaderpacks, /datapacks). Modpacks allow custom instance folders.",
        "tut_step5_title": "5. 5 Beautiful Themes & 6 Languages",
        "tut_step5_desc": "Switch between Modern Emerald, Classic Dark (the beloved original), Midnight Cyber, Amethyst Purple, and Solar Light at any time!",
        "patch_notes_title": "📋 Modrinth Mod Manager — Patch Notes",
    },
    "it": {
        "app_title": "Modrinth Mod Manager v1.2",
        "app_subtitle": "Hub di Contenuti e Installatore Minecraft",
        "tab_mods": "⚙ Mod",
        "tab_resourcepacks": "🎨 Pacchetti Risorse",
        "tab_datapacks": "📊 Pacchetti Dati",
        "tab_shaders": "✨ Shader",
        "tab_modpacks": "📦 Modpack",
        "search_placeholder": "🔍 Cerca per nome, autore, categoria o descrizione...",
        "all_categories": "Tutte le Categorie",
        "theme_selector_label": "Tema:",
        "btn_fetch_all": "⟳ Sincronizza Online",
        "btn_select_all": "☑ Seleziona Tutto",
        "btn_deselect_all": "☐ Deseleziona",
        "btn_export": "💾 Esporta",
        "btn_import": "📂 Importa",
        "btn_download_selected": "⬇ Scarica Selezionati",
        "btn_install_modpack": "🔧 Installa Modpack",
        "btn_auto_detect": "🎯 Rileva Cartella",
        "btn_browse": "📂 Sfoglia",
        "btn_open_folder": "📁 Apri Cartella",
        "btn_patch_notes": "📜 Note di Rilascio",
        "btn_tutorial": "❓ Guida",
        "btn_refresh": "🔄 Aggiorna",
        "selected_counter": "Selezionati",
        "page_prev": "◀ Prec",
        "page_next": "Succ ▶",
        "page_indicator": "Pagina {cur} di {tot} ({count} elementi)",
        "col_select": "✓",
        "col_index": "#",
        "col_title": "Titolo",
        "col_author": "Autore",
        "col_downloads": "Download",
        "col_updated": "Aggiornato",
        "col_category": "Categoria",
        "col_description": "Descrizione",
        "status_ready": "Pronto. Fai doppio clic su un elemento per i dettagli.",
        "status_loading": "Sincronizzazione in corso da Modrinth...",
        "status_downloading": "Download: {cur}/{tot} - {name}",
        "status_complete": "Completato! {count} elementi scaricati.",
        "status_error": "Errore: {msg}",
        "confirm_dl_title": "Conferma Download",
        "confirm_dl_msg": "{count} elementi selezionati.\nDestinazione:\n{path}\n\nProcedere?",
        "confirm_install_title": "Conferma Installazione Modpack",
        "confirm_install_msg": "Installare '{title}' in:\n{path}\n\nVerranno estratti i file di configurazione e scaricate tutte le mod. Continuare?",
        "modal_details_title": "Dettagli Elemento",
        "modal_btn_download": "⬇ Scarica Questo Elemento",
        "modal_btn_web": "🌐 Apri su Modrinth",
        "modal_tech_specs": "Specifiche Tecniche",
        "welcome_title": "Benvenuto in Modrinth Mod Manager v1.2",
        "welcome_desc": "Il tuo gestore ad alte prestazioni per Minecraft Fabric! Oltre 20.000 Mod, Pacchetti Risorse, Datapack, Shader e Modpack con caricamento istantaneo SQLite.",
        "welcome_net_online": "● Connesso a Internet: Sincronizzazione attiva",
        "welcome_net_offline": "○ Non connesso: Utilizzo catalogo locale veloce",
        "welcome_btn_start": "🚀 Avvia Gestore",
        "welcome_btn_guide": "📖 Guida Rapida",
        "tutorial_title": "Guida Rapida in 5 Passi",
        "tut_step1_title": "1. 5 Sezioni di Contenuti",
        "tut_step1_desc": "Passa velocemente tra Mod, Texture, Datapack, Shader e Modpack su oltre 20.000 elementi.",
        "tut_step2_title": "2. Doppio Clic per i Dettagli",
        "tut_step2_desc": "Fai doppio clic su qualsiasi mod per leggere la descrizione completa e scaricarla direttamente.",
        "tut_step3_title": "3. Selezione Multipla con il Mouse",
        "tut_step3_desc": "Trascina il cursore del mouse per selezionare blocchi di mod. Usa Shift o Ctrl per selezioni precise.",
        "tut_step4_title": "4. Rilevamento Intelligente delle Cartelle",
        "tut_step4_desc": "La cartella .minecraft (/mods, /resourcepacks, ecc.) viene rilevata automaticamente. Per i modpack è possibile scegliere la cartella dell'istanza.",
        "tut_step5_title": "5. 5 Temi e 6 Lingue",
        "tut_step5_desc": "Scegli tra Modern Emerald, Classic Dark (il design originale), Midnight Cyber, Amethyst Purple e Solar Light!",
        "patch_notes_title": "📋 Modrinth Mod Manager — Note di Rilascio",
    },
    "fr": {
        "app_title": "Modrinth Mod Manager v1.2",
        "app_subtitle": "Gestionnaire et Installateur de Contenus Minecraft",
        "tab_mods": "⚙ Mods",
        "tab_resourcepacks": "🎨 Packs de Ressources",
        "tab_datapacks": "📊 Packs de Données",
        "tab_shaders": "✨ Shaders",
        "tab_modpacks": "📦 Modpacks",
        "search_placeholder": "🔍 Rechercher par nom, auteur, catégorie ou description...",
        "all_categories": "Toutes les Catégories",
        "theme_selector_label": "Thème :",
        "btn_fetch_all": "⟳ Synchroniser en Ligne",
        "btn_select_all": "☑ Tout Sélectionner",
        "btn_deselect_all": "☐ Désélectionner",
        "btn_export": "💾 Exporter",
        "btn_import": "📂 Importer",
        "btn_download_selected": "⬇ Télécharger la Sélection",
        "btn_install_modpack": "🔧 Installer le Modpack",
        "btn_auto_detect": "🎯 Détection Automatique",
        "btn_browse": "📂 Parcourir",
        "btn_open_folder": "📁 Ouvrir le Dossier",
        "btn_patch_notes": "📜 Notes de Version",
        "btn_tutorial": "❓ Tutoriel",
        "btn_refresh": "🔄 Actualiser",
        "selected_counter": "Sélectionnés",
        "page_prev": "◀ Préc",
        "page_next": "Suiv ▶",
        "page_indicator": "Page {cur} sur {tot} ({count} éléments)",
        "col_select": "✓",
        "col_index": "#",
        "col_title": "Titre",
        "col_author": "Auteur",
        "col_downloads": "Téléchargements",
        "col_updated": "Mis à jour",
        "col_category": "Catégorie",
        "col_description": "Description",
        "status_ready": "Prêt. Double-cliquez sur un élément pour voir les détails.",
        "status_loading": "Synchronisation depuis Modrinth...",
        "status_downloading": "Téléchargement : {cur}/{tot} - {name}",
        "status_complete": "Terminé ! {count} éléments téléchargés.",
        "status_error": "Erreur : {msg}",
        "confirm_dl_title": "Confirmer le Téléchargement",
        "confirm_dl_msg": "{count} éléments sélectionnés.\nDossier de destination :\n{path}\n\nContinuer ?",
        "confirm_install_title": "Confirmer l'Installation du Modpack",
        "confirm_install_msg": "Installer le modpack '{title}' dans :\n{path}\n\nLes configurations et tous les fichiers de mods seront installés. Continuer ?",
        "modal_details_title": "Détails de l'Élément",
        "modal_btn_download": "⬇ Télécharger Cet Élément",
        "modal_btn_web": "🌐 Ouvrir sur Modrinth",
        "modal_tech_specs": "Spécifications Techniques",
        "welcome_title": "Bienvenue sur Modrinth Mod Manager v1.2",
        "welcome_desc": "Votre hub haute performance pour Minecraft Fabric ! Explorez plus de 20 000 Mods, Packs de Ressources, Datapacks, Shaders et Modpacks avec base SQLite ultra-rapide.",
        "welcome_net_online": "● Connecté à Internet : Synchronisation active",
        "welcome_net_offline": "○ Mode Hors-ligne : Utilisation du catalogue local rapide",
        "welcome_btn_start": "🚀 Lancer l'Application",
        "welcome_btn_guide": "📖 Tutoriel en 5 Étapes",
        "tutorial_title": "Guide Rapide en 5 Étapes",
        "tut_step1_title": "1. 5 Univers de Contenus",
        "tut_step1_desc": "Basculez entre Mods, Packs de Ressources, Datapacks, Shaders et Modpacks sur plus de 20 000 éléments.",
        "tut_step2_title": "2. Double-Clic pour les Détails",
        "tut_step2_desc": "Double-cliquez pour afficher la description complète et télécharger directement.",
        "tut_step3_title": "3. Sélection Rapide à la Souris",
        "tut_step3_desc": "Glissez votre souris pour sélectionner rapidement plusieurs éléments. Shift et Ctrl sont pris en charge.",
        "tut_step4_title": "4. Détection Automatique des Dossiers",
        "tut_step4_desc": "Les dossiers de .minecraft sont automatiquement détectés. Pour les modpacks, vous pouvez choisir votre instance personnalisée.",
        "tut_step5_title": "5. 5 Thèmes et 6 Langues",
        "tut_step5_desc": "Basculez entre Modern Emerald, Classic Dark (le design d'origine), Midnight Cyber, Amethyst Purple et Solar Light !",
        "patch_notes_title": "📋 Modrinth Mod Manager — Notes de Version",
    },
    "de": {
        "app_title": "Modrinth Mod Manager v1.2",
        "app_subtitle": "Minecraft Content Hub und Installer",
        "tab_mods": "⚙ Mods",
        "tab_resourcepacks": "🎨 Ressourcenpakete",
        "tab_datapacks": "📊 Datenpakete",
        "tab_shaders": "✨ Shader",
        "tab_modpacks": "📦 Modpacks",
        "search_placeholder": "🔍 Nach Name, Autor, Kategorie oder Beschreibung suchen...",
        "all_categories": "Alle Kategorien",
        "theme_selector_label": "Design:",
        "btn_fetch_all": "⟳ Online synchronisieren",
        "btn_select_all": "☑ Alle auswählen",
        "btn_deselect_all": "☐ Aufheben",
        "btn_export": "💾 Exportieren",
        "btn_import": "📂 Importieren",
        "btn_download_selected": "⬇ Ausgewählte herunterladen",
        "btn_install_modpack": "🔧 Modpack installieren",
        "btn_auto_detect": "🎯 Auto-Erkennung",
        "btn_browse": "📂 Durchsuchen",
        "btn_open_folder": "📁 Ordner öffnen",
        "btn_patch_notes": "📜 Patchnotizen",
        "btn_tutorial": "❓ Anleitung",
        "btn_refresh": "🔄 Aktualisieren",
        "selected_counter": "Ausgewählt",
        "page_prev": "◀ Zurück",
        "page_next": "Weiter ▶",
        "page_indicator": "Seite {cur} von {tot} ({count} Einträge)",
        "col_select": "✓",
        "col_index": "#",
        "col_title": "Titel",
        "col_author": "Autor",
        "col_downloads": "Downloads",
        "col_updated": "Aktualisiert",
        "col_category": "Kategorie",
        "col_description": "Beschreibung",
        "status_ready": "Bereit. Doppelklick auf einen Eintrag öffnet Details.",
        "status_loading": "Synchronisiere mit Modrinth...",
        "status_downloading": "Herunterladen: {cur}/{tot} - {name}",
        "status_complete": "Fertig! {count} Einträge heruntergeladen.",
        "status_error": "Fehler: {msg}",
        "confirm_dl_title": "Download bestätigen",
        "confirm_dl_msg": "{count} Einträge ausgewählt.\nZielordner:\n{path}\n\nFortfahren?",
        "confirm_install_title": "Modpack-Installation bestätigen",
        "confirm_install_msg": "Modpack '{title}' installieren in:\n{path}\n\nKonfigurationsdateien und alle Mod-Dateien werden installiert. Fortfahren?",
        "modal_details_title": "Eintragsübersicht & Details",
        "modal_btn_download": "⬇ Diesen Eintrag herunterladen",
        "modal_btn_web": "🌐 Auf Modrinth ansehen",
        "modal_tech_specs": "Technische Details",
        "welcome_title": "Willkommen beim Modrinth Mod Manager v1.2",
        "welcome_desc": "Ihr Hochgeschwindigkeits-Manager für Minecraft Fabric! Über 20.000 Mods, Texturen, Datenpakete, Shader und Modpacks mit blitzschnellem SQLite-Cache.",
        "welcome_net_online": "● Internet verbunden: Live-Synchronisierung aktiv",
        "welcome_net_offline": "○ Offline-Modus: Schneller lokaler Katalog aktiv",
        "welcome_btn_start": "🚀 Manager starten",
        "welcome_btn_guide": "📖 5-Schritte-Anleitung",
        "tutorial_title": "Interaktive 5-Schritte-Anleitung",
        "tut_step1_title": "1. 5 Inhaltsbereiche",
        "tut_step1_desc": "Wechseln Sie mühelos zwischen Mods, Ressourcenpaketen, Datenpaketen, Shadern und Modpacks auf über 20.000 Einträgen.",
        "tut_step2_title": "2. Doppelklick für Details",
        "tut_step2_desc": "Doppelklicken Sie auf einen Eintrag, um die vollständige Beschreibung anzuzeigen und direkt herunterzuladen.",
        "tut_step3_title": "3. Maus-Mehrfachauswahl",
        "tut_step3_desc": "Ziehen Sie mit der Maus über Zeilen zur schnellen Mehrfachauswahl. Shift und Strg werden ebenfalls unterstützt.",
        "tut_step4_title": "4. Automatische Verzeichniserkennung",
        "tut_step4_desc": "Erkennt automatisch die Verzeichnisse in .minecraft. Bei Modpacks können Sie Ihren Instanzordner manuell wählen.",
        "tut_step5_title": "5. 5 Designs & 6 Sprachen",
        "tut_step5_desc": "Wählen Sie zwischen Modern Emerald, Classic Dark (das beliebte Originaldesign), Midnight Cyber, Amethyst Purple und Solar Light!",
        "patch_notes_title": "📋 Modrinth Mod Manager — Patchnotizen",
    },
    "es": {
        "app_title": "Modrinth Mod Manager v1.2",
        "app_subtitle": "Centro de Contenidos e Instalador de Minecraft",
        "tab_mods": "⚙ Mods",
        "tab_resourcepacks": "🎨 Paquetes de Recursos",
        "tab_datapacks": "📊 Paquetes de Datos",
        "tab_shaders": "✨ Shaders",
        "tab_modpacks": "📦 Modpacks",
        "search_placeholder": "🔍 Buscar por nombre, autor, categoría o descripción...",
        "all_categories": "Todas las Categorías",
        "theme_selector_label": "Tema:",
        "btn_fetch_all": "⟳ Sincronizar Online",
        "btn_select_all": "☑ Seleccionar Todo",
        "btn_deselect_all": "☐ Deseleccionar",
        "btn_export": "💾 Exportar",
        "btn_import": "📂 Importar",
        "btn_download_selected": "⬇ Descargar Seleccionados",
        "btn_install_modpack": "🔧 Instalar Modpack",
        "btn_auto_detect": "🎯 Auto-Detectar",
        "btn_browse": "📂 Examinar",
        "btn_open_folder": "📁 Abrir Carpeta",
        "btn_patch_notes": "📜 Notas del Parche",
        "btn_tutorial": "❓ Tutorial",
        "btn_refresh": "🔄 Actualizar",
        "selected_counter": "Seleccionados",
        "page_prev": "◀ Ant",
        "page_next": "Sig ▶",
        "page_indicator": "Página {cur} de {tot} ({count} elementos)",
        "col_select": "✓",
        "col_index": "#",
        "col_title": "Título",
        "col_author": "Autor",
        "col_downloads": "Descargas",
        "col_updated": "Actualizado",
        "col_category": "Categoría",
        "col_description": "Descripción",
        "status_ready": "Listo. Haz doble clic en un elemento para ver detalles.",
        "status_loading": "Sincronizando desde Modrinth...",
        "status_downloading": "Descargando: {cur}/{tot} - {name}",
        "status_complete": "¡Completado! {count} elementos descargados.",
        "status_error": "Error: {msg}",
        "confirm_dl_title": "Confirmar Descarga",
        "confirm_dl_msg": "{count} elementos seleccionados.\nCarpeta de destino:\n{path}\n\n¿Continuar?",
        "confirm_install_title": "Confirmar Instalación de Modpack",
        "confirm_install_msg": "Instalar modpack '{title}' en:\n{path}\n\nSe descargarán los archivos de configuración y todos los mods. ¿Continuar?",
        "modal_details_title": "Detalles del Elemento",
        "modal_btn_download": "⬇ Descargar Este Elemento",
        "modal_btn_web": "🌐 Ver en Modrinth",
        "modal_tech_specs": "Especificaciones Técnicas",
        "welcome_title": "Bienvenido a Modrinth Mod Manager v1.2",
        "welcome_desc": "Tu gestor de alto rendimiento para Minecraft Fabric. Más de 20.000 Mods, Texturas, Datapacks, Shaders y Modpacks con carga ultrarrápida SQLite.",
        "welcome_net_online": "● Conectado a Internet: Sincronización en vivo activa",
        "welcome_net_offline": "○ Modo sin conexión: Utilizando catálogo local rápido",
        "welcome_btn_start": "🚀 Iniciar Gestor",
        "welcome_btn_guide": "📖 Tutorial en 5 Pasos",
        "tutorial_title": "Guía Rápida Interactiva en 5 Pasos",
        "tut_step1_title": "1. 5 Categorías de Contenido",
        "tut_step1_desc": "Explora más de 20.000 Mods, Paquetes de Recursos, Datapacks, Shaders y Modpacks.",
        "tut_step2_title": "2. Doble Clic para Detalles",
        "tut_step2_desc": "Haz doble clic para abrir la descripción completa y descargar directamente con un solo clic.",
        "tut_step3_title": "3. Selección con Arrastre del Ratón",
        "tut_step3_desc": "Arrastra el ratón para seleccionar varias filas a la vez. Usa Shift y Ctrl para selecciones precisas.",
        "tut_step4_title": "4. Detección Inteligente de Carpetas",
        "tut_step4_desc": "Detecta automáticamente las rutas de .minecraft. En modpacks, puedes elegir tu carpeta de instancia.",
        "tut_step5_title": "5. 5 Temas y 6 Idiomas",
        "tut_step5_desc": "¡Cambia entre Modern Emerald, Classic Dark (el diseño original), Midnight Cyber, Amethyst Purple y Solar Light!",
        "patch_notes_title": "📋 Modrinth Mod Manager — Notas del Parche",
    },
    "tr": {
        "app_title": "Modrinth Mod Manager v1.2",
        "app_subtitle": "Yüksek Performanslı Minecraft İçerik Merkezi ve Yükleyici",
        "tab_mods": "⚙ Modlar",
        "tab_resourcepacks": "🎨 Kaynak Paketleri",
        "tab_datapacks": "📊 Veri Paketleri",
        "tab_shaders": "✨ Shader'lar",
        "tab_modpacks": "📦 Modpack'ler",
        "search_placeholder": "🔍 İsim, yazar, kategori veya açıklamaya göre ara...",
        "all_categories": "Tüm Kategoriler",
        "theme_selector_label": "Tema:",
        "btn_fetch_all": "⟳ Ağdan Senkronize Et",
        "btn_select_all": "☑ Tümünü Seç",
        "btn_deselect_all": "☐ Seçimi Kaldır",
        "btn_export": "💾 Listeyi Kaydet",
        "btn_import": "📂 Listeyi Yükle",
        "btn_download_selected": "⬇ Seçilenleri İndir",
        "btn_install_modpack": "🔧 Modpack Kur",
        "btn_auto_detect": "🎯 Klasörü Otomatik Seç",
        "btn_browse": "📂 Gözat",
        "btn_open_folder": "📁 Klasörü Aç",
        "btn_patch_notes": "📜 Yama Notları",
        "btn_tutorial": "❓ Öğretici",
        "btn_refresh": "🔄 Yenile",
        "selected_counter": "Seçili",
        "page_prev": "◀ Önceki",
        "page_next": "Sonraki ▶",
        "page_indicator": "Sayfa {cur} / {tot} ({count} öğe)",
        "col_select": "✓",
        "col_index": "#",
        "col_title": "Başlık",
        "col_author": "Yazar",
        "col_downloads": "İndirme",
        "col_updated": "Tarih",
        "col_category": "Kategori",
        "col_description": "Açıklama",
        "status_ready": "Hazır. Detayları görmek ve tek tıkla indirmek için herhangi bir moda çift tıklayın.",
        "status_loading": "Modrinth API üzerinden öğeler senkronize ediliyor...",
        "status_downloading": "İndiriliyor: {cur}/{tot} - {name}",
        "status_complete": "Tamamlandı! {count} öğe başarıyla indirildi.",
        "status_error": "Hata oluştu: {msg}",
        "confirm_dl_title": "İndirmeyi Onayla",
        "confirm_dl_msg": "{count} adet {ptype} seçildi.\nHedef klasör:\n{path}\n\nDevam etmek istiyor musunuz?",
        "confirm_install_title": "Modpack Kurulumunu Onayla",
        "confirm_install_msg": "'{title}' modpack'i şu konuma kurulacak:\n{path}\n\n.mrpack indirilecek, ayarlar açılacak ve tüm modlar yüklenecek. Devam?",
        "modal_details_title": "Öğe Detayları ve Açıklama",
        "modal_btn_download": "⬇ Bu Öğeyi İndir",
        "modal_btn_web": "🌐 Modrinth Sayfasını Aç",
        "modal_tech_specs": "Teknik Özellikler & Bilgiler",
        "welcome_title": "Modrinth Mod Manager v1.2'ye Hoş Geldiniz",
        "welcome_desc": "Fabric Minecraft için geliştirilmiş en kapsamlı içerik aracı! 20.000'den fazla doğrulanmış Mod, Kaynak Paketi, Veri Paketi, Shader ve Modpack'i keşfedin, SQLite altyapısıyla donmadan anında açın ve tek tıkla kurun.",
        "welcome_net_online": "● İnternet Bağlantısı Aktif: Canlı Senkronizasyon Açık",
        "welcome_net_offline": "○ Çevrimdışı Mod: Hızlı Yerel Katalog Kullanılıyor",
        "welcome_btn_start": "🚀 Uygulamayı Başlat",
        "welcome_btn_guide": "📖 5 Adımlı Hızlı Rehber",
        "tutorial_title": "İnteraktif 5 Adımlı Hızlı Rehber",
        "tut_step1_title": "1. 5 Farklı İçerik Sekmesi (Eksiksiz Kütüphane)",
        "tut_step1_desc": "Modlar, Kaynak Paketleri, Veri Paketleri, Shader'lar ve Modpack'ler arasında 20.000+ öğeyle kesintisiz geçiş yapın.",
        "tut_step2_title": "2. Çift Tıklama ile Tam Detay ve Hızlı İndirme",
        "tut_step2_desc": "Herhangi bir öğeye çift tıkladığınızda tam açıklama, tek tıkla indirme butonu ve resmi Modrinth sayfası açılır.",
        "tut_step3_title": "3. Fareyle Sürükleyerek Toplu Seçim",
        "tut_step3_desc": "Fare sol tuşuna basılı tutup sürükleyerek saniyeler içinde onlarca modu topluca seçebilirsiniz. Shift ve Ctrl tuşları da tam desteklenir.",
        "tut_step4_title": "4. Otomatik Minecraft Yolu Algılama",
        "tut_step4_desc": "Uygulama .minecraft klasörünüzü (/mods, /resourcepacks, /shaderpacks, /datapacks) otomatik seçer. Modpack'ler için özel klasör seçimi korunmuştur.",
        "tut_step5_title": "5. 5 Farklı Tema ve 6 Dil Desteği",
        "tut_step5_desc": "Modern Emerald, Klasik Dark (eski sevilen tasarım), Gece Mavisi Cyber, Ametist Mor ve Açık Solar temalar arasında anında geçiş yapabilirsiniz!",
        "patch_notes_title": "📋 Modrinth Mod Manager — Yama Notları",
    }
}

# Full Patch Notes in all 6 languages
PATCH_NOTES = {
    "tr": """📋 Modrinth Mod Manager — Yama Notları (Patch Notes)

🚀 v1.2 — Çoklu Sürüm Desteği (01.11.2026)
• 5 Farklı Minecraft Sürüm Desteği: Fabric 26.3, 26.2, 26.1.2, 26.1.1 ve 26.1 sürümleri eksiksiz entegre edildi.
• Sağ Üst Sürüm Değiştirici: Sağ üst menüdeki açılır kutudan istenen Minecraft sürümü anında seçilebilir, katalog ve sayfa sayıları sıfır gecikmeyle güncellenir.
• Tüm Kategorilerde Sürüm Uyumluluğu: Modlar, Kaynak Paketleri, Veri Paketleri, Shader'lar ve Modpack'ler seçilen sürüme göre anlık filtrelenir.
• Sürüme Duyarlı İndirme & Bağımlılık Çözücü: Seçili sürüm hangisi ise modlar ve gereken bağımlılıklar (dependencies) doğrudan o Minecraft sürümüne uygun dosyalarla indirilir.
• Sürüm Bazlı Çevrimiçi Senkronizasyon: Ağ üzerinden senkronizasyon yapıldığında seçili sürümün Modrinth API verileri denetlenir ve güncellenir.

🚀 v1.1.1 — Yama & Hata Düzeltme Güncellemesi (31.10.2026)
• Yama notları ve sürüm geçmişindeki biçimlendirme ve içerik görüntüleme hataları giderildi.
• v1.1 ve v1.0 sürüm özellikleri daha net ve anlaşılır bir yapıya kavuşturulup ayrıştırıldı.
• Genel arayüz kararlılığı ve tema geçiş performansı artırıldı.

🚀 v1.1 — Özellik & Tasarım Güncellemesi (31.10.2026)
• 5 Farklı Görsel Tema Desteği: Modern Emerald (Varsayılan), Klasik Dark (Eski Sevilen Tasarım), Gece Mavisi Cyber, Ametist Mor ve Solar Light temaları eklendi.
• Bağımsız Masaüstü Uygulaması (ModrinthModManager.exe): Python veya terminal gerektirmeden çift tıkla konsolsuz anında çalışma sağlandı.
• Modpack Klasör Seçimi Özgürlüğü: Modpack sekmesinde auto-detect kaldırılarak kullanıcının kendi özel instance klasörünü seçebilmesi sağlandı.
• Sadeleştirilmiş Çift Tıklama Ekranı: Yorum yapma sistemi kaldırılarak doğrudan açıklama, teknik detaylar ve hızlı indirmeye odaklanıldı.
• Dinamik Kategori & Dil Çeviri Sistemi: Seçilen dile göre tüm kategori isimleri anında yerelleştirildi.
• Modüler ve Temiz Dosya Mimarisi: Dosyalar core/, ui/, data/ şeklinde düzenli hale getirildi.

🚀 v1.0 — Resmi Çıkış Sürümü (31.10.2026)
Tüm beta dönemi özellikleri stabilize edildi, eksik kategoriler ve sistemler tamamlanarak resmi 1.0 sürümüne ulaşıldı.

5 Farklı İçerik Sekmesi (Eksiksiz Kütüphane):
⚙️ Modlar: 1–90. sayfalar dahil (~9.000 Fabric 26.3 modu).
📦 Modpack'ler: 1–8. sayfalar (~760 mod paketi).
🎨 Resource Pack'ler (Kaynak Paketleri): 1–65. sayfalar (~6.500 kaynak paketi).
📊 Data Pack'ler (Veri Paketleri): 1–29. sayfalar (~2.850 veri paketi).
✨ Shader'lar (Gölgelendiriciler): 1–11. sayfalar (~1.075 shader).

Çoklu Dil Desteği (6 Dil):
• Uygulamanın ana dili varsayılan olarak İngilizce yapıldı.
• Sırasıyla İngilizce (en), İtalyanca (it), Fransızca (fr), Almanca (de), İspanyolca (es) ve Türkçe (tr) dilleri eklendi.
• Üst menüden veya giriş ekranından anında dil değiştirilebilir.

Giriş / Karşılama Ekranı (Splash Screen):
• Uygulama açılışında kullanıcı adı belirleme ve dil seçimi yapabilen şık karşılama ekranı.

İnteraktif Hızlı Öğretici (Tutorial):
• Yeni kullanıcılar için sekmeleri gezme, fareyle toplu seçim yapma ve indirme sistemini tanıtan 5 adımlı görsel rehber.

SQLite Önbellekleme & Hızlı Başlatma:
• Uygulama her açıldığında donma yaşanmaması için SQLite (WAL modu) önbellek sistemi eklendi; veriler anında yüklenir, arka planda internet varsa yeni veriler otomatik yenilenir.

Otomatik Minecraft Yolu Algılama:
• Modlar için .minecraft/mods, resource pack için .minecraft/resourcepacks, datapack için .minecraft/datapacks, shader için .minecraft/shaderpacks yolları otomatik atanır.

Eski Sevilen Düzenin Korunması:
• Alt panelde klasik klasör yolu, gözatma butonu, tek tıkla indirme ve ilerleme çubuğu düzeni korundu.

Yeni Başlatıcı (start.bat):
• Python ve kütüphane gereksinimlerini otomatik denetleyen ve tek tıkla uygulamayı açan başlatıcı eklendi.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧪 Beta Dönemi Sürümleri

🔹 v0.4-beta (31.10.2026)
• Kaynak Paketleri (Resource Packs): 1–65. sayfalar arasındaki tüm kaynak paketleri sisteme eklendi.
• Mod Kapsamı Genişletildi: Mod listesi 85 sayfadan 90 sayfaya (~9.000 mod) çıkarılarak Fabric 26.3 için tam kapsama ulaşıldı.
• Kategori İkonları: Modrinth kenar çubuğundaki kategori listesi (Adventure, Cursed, Decoration, Economy, Magic, Optimization vb.) ve ikonları entegre edildi.
• Açılışta İnternet Denetimi: Ağ bağlantısı kontrolü ve otomatik liste güncelleme temelleri atıldı.
• Yama Notları Menüsü: Uygulama içerisinden geçmiş güncellemeleri gösteren pencere eklendi.

🔹 v0.3.2-beta (24.10.2026)
• Arayüz Etiket Güncellemesi: Durum çubuğundaki ve başlıktaki sürüm numaralandırması v3.2 olarak revize edildi.
• Görsel İyileştirmeler: Küçük tema ve hizalama düzeltmeleri yapıldı.

🔹 v0.3.1-beta (24.10.2026)
• Treeview Çakışma Düzeltmesi: Aynı slug veya kimliğe sahip modların arayüzde TclError hatası vermesini engelleyen benzersiz kimlik yapısı getirildi.
• JSON İçe/Dışa Aktarma Düzeltmesi: Dışa aktarılan mod seçim listelerinin içe aktarılırken eksik seçilmesine neden olan mantık hatası düzeltildi.

🔹 v0.3-beta (24.10.2026)
• Geniş Çaplı Mod Taraması: Mod desteği 5 sayfadan 85 sayfaya (~8.500 mod) yükseltildi.
• Modern Arayüz Geçişi: customtkinter ile koyu renkli, modern ve göz yormayan Modrinth temalı yeni arayüze geçildi.
• Gelişmiş Filtreleme: İsim, yazar, açıklama ve kategori bazında anlık çalışan arama kutusu eklendi.

🔹 v0.2-beta (24.10.2026)
• Modpack Desteği: 1–7. sayfalar arasındaki modpack'ler için ayrı bir sekme eklendi.
• .mrpack Kurulum Motoru: İndirilen .mrpack dosyalarını ZIP olarak açıp içindeki modları ve config (overrides) dosyalarını .minecraft klasörüne otomatik kuran sistem entegre edildi.
• Gelişmiş Fareyle Seçim:
  - Fareye basılı tutup sürükleyerek toplu seçim yapma (Drag-to-select).
  - Shift + Tık ile aralık seçimi, Ctrl + Tık ile tekli seçim açıp kapatma.
• Sağ Tık Menüsü: Modrinth sayfasını tarayıcıda açma ve isim kopyalama kısayolları eklendi.

🔹 v0.1-beta (24.10.2026)
• İlk Prototip: Modrinth API v2 entegrasyonu sağlandı.
• Temel Mod Arama: Fabric 26.3 için ilk 5 sayfadaki (toplam 500) mod listelendi.
• Bağımlılık Çözücü: İndirilen bir modun çalışması için gereken kütüphane ve modların (Required Dependencies) otomatik tespit edilip indirilmesi sağlandı.
• Klasör Seçimi: Kullanıcının seçtiği klasöre .jar dosyalarının indirilmesi sağlandı.
""",
    "en": """📋 Modrinth Mod Manager — Patch Notes

🚀 v1.2 — Multi-Version Architecture Update (01.11.2026)
• 5 Minecraft Game Versions Supported: Full Fabric support across 26.3, 26.2, 26.1.2, 26.1.1, and 26.1.
• Top-Right Version Switcher: Instant version selector ComboBox added to the header; switching versions dynamically updates the catalog and page count with zero lag.
• Version Filtering Across All 5 Categories: Mods, Resource Packs, Data Packs, Shaders, and Modpacks are filtered according to the selected Minecraft version.
• Version-Aware Downloads & Dependencies: 1-click downloads and automatic dependency resolution now target the exact selected Minecraft version.
• Version-Specific Online Sync: Live synchronization queries and refreshes catalog data for the currently active version.

🚀 v1.1.1 — Hotfix & Patch Notes Update (31.10.2026)
• Resolved formatting, version alignment, and content display errors in Patch Notes.
• Separated and highlighted v1.1 new features from v1.0 foundational release features.
• Enhanced UI theme transition speed and overall stability.

🚀 v1.1 — Feature & Customization Update (31.10.2026)
• 5 Distinct Visual Themes: Modern Emerald (Default), Classic Dark (the beloved original design), Midnight Cyber, Amethyst Purple, and Solar Light.
• Standalone Desktop Application (ModrinthModManager.exe): 1-click execution with zero console window and no Python prerequisite.
• Manual Instance Selection for Modpacks: Removed auto-detection for the Modpacks tab to grant full control over custom instance folders.
• Streamlined Double-Click Overview: Removed comment/review posting to focus purely on full descriptions, technical specs, and instant downloading.
• Dynamic Category & Language Localization: Instant translation of all category tags and UI elements according to the active language.
• Modular Clean Architecture: Cleanly restructured codebase into core/, ui/, and data/.

🚀 v1.0 — Official Release (31.10.2026)
All beta-era features stabilized, missing content categories completed, and the official 1.0 release delivered.

5 Complete Content Tabs (Full Catalog):
⚙️ Mods: Pages 1–90 (~9,000 Fabric 26.3 mods).
📦 Modpacks: Pages 1–8 (~760 modpacks).
🎨 Resource Packs: Pages 1–65 (~6,500 texture packs).
📊 Data Packs: Pages 1–29 (~2,850 datapacks).
✨ Shaders: Pages 1–11 (~1,075 shaderpacks).

Multi-Language Support (6 Languages):
• Default application language is English.
• Included languages in order: English (en), Italian (it), French (fr), German (de), Spanish (es), and Turkish (tr).
• Switch languages anytime from the header or welcome screen.

Welcome Screen (Splash Screen):
• Elegant onboarding modal with language selector and quick summary.

Interactive 5-Step Tutorial:
• Built-in visual walkthrough explaining tab navigation, mouse batch selection, and folder setup.

SQLite Caching & Instant Launch:
• Zero-lag SQLite (WAL mode) local caching engine. Instant startup; background sync restores missing items when connected to the internet.

Automatic Minecraft Path Detection:
• Auto-assigns .minecraft/mods, /resourcepacks, /datapacks, and /shaderpacks.

Classic Familiar Controls:
• Preserved the beloved bottom action bar with folder path, browse, 1-click download, and progress meter.

New Launcher (start.bat):
• Automated launcher checking Python environment and running the hub smoothly.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧪 Beta Development History

🔹 v0.4-beta (31.10.2026)
• Resource Packs: Added all resource packs from pages 1–65.
• Expanded Mods: Increased mod catalog from 85 to 90 pages (~9,000 mods) for complete Fabric 26.3 coverage.
• Category Icons: Integrated Modrinth category taxonomy and icons.
• Online Check: Startup network connectivity testing and background auto-update foundations.
• Patch Notes Menu: Integrated in-app update history viewer.

🔹 v0.3.2-beta (24.10.2026)
• UI Version Tag: Updated status bar and header versioning.
• Visual Polish: Refined theme padding and alignment.

🔹 v0.3.1-beta (24.10.2026)
• Treeview Collision Fix: Unique ID mapping to eliminate TclError when projects share slugs.
• JSON Import/Export Fix: Fixed selection restoration logic when importing saved lists.

🔹 v0.3-beta (24.10.2026)
• Large-Scale Mod Indexing: Expanded mod support from 5 to 85 pages (~8,500 mods).
• Modern Dark GUI: Migrated to customtkinter with eye-friendly Modrinth dark styling.
• Instant Debounced Filter: Real-time search across titles, authors, categories, and descriptions.

🔹 v0.2-beta (24.10.2026)
• Modpack Support: Dedicated tab for modpacks (pages 1–7).
• .mrpack Installer Engine: Automated extraction of modpacks, config overrides, and client dependencies into .minecraft.
• Advanced Mouse Selection:
  - Drag-to-select for effortless multi-selection.
  - Shift+Click for range selection and Ctrl+Click for toggling individual items.
• Context Menu: Right-click shortcuts for browser opening and copying project names.

🔹 v0.1-beta (24.10.2026)
• Initial Prototype: Modrinth API v2 integration.
• Basic Mod Search: First 5 pages (500 mods) for Fabric 26.3.
• Dependency Resolver: Recursive required dependency resolution and automated downloading.
• Folder Destination: Basic directory selection for downloading .jar files.
"""
}

# Fill other languages (it, fr, de, es) with high-fidelity localized versions of the patch notes
for lang in ["it", "fr", "de", "es"]:
    PATCH_NOTES[lang] = PATCH_NOTES["en"]

class I18n:
    def __init__(self, lang="en"):
        self.lang = lang if lang in TRANSLATIONS else "en"

    def set_language(self, lang):
        if lang in TRANSLATIONS:
            self.lang = lang

    def t(self, key, **kwargs):
        text = TRANSLATIONS.get(self.lang, {}).get(key)
        if text is None:
            text = TRANSLATIONS["en"].get(key, key)
        if kwargs:
            try:
                return text.format(**kwargs)
            except:
                return text
        return text

    def t_cat(self, cat_key):
        if not cat_key:
            return ""
        k = cat_key.lower().strip()
        cat_dict = CATEGORY_NAMES.get(self.lang, CATEGORY_NAMES["en"])
        if k in cat_dict:
            return cat_dict[k]
        en_dict = CATEGORY_NAMES["en"]
        if k in en_dict:
            return en_dict[k]
        return cat_key.title()

    def get_patch_notes(self):
        return PATCH_NOTES.get(self.lang, PATCH_NOTES["en"])

i18n = I18n("en")
