#!/usr/bin/env python3
"""
<<<<<<< HEAD
Modrinth Mod Manager v2.0 (Official Release)
==============================================
High-Performance Minecraft Content Hub & Installer
- Multi-Version Fabric Support: 1.21.11 down to 1.21 & 26.3 down to 26.1
=======
Modrinth Mod Manager v1.2 (Official Release)
==============================================
High-Performance Minecraft Content Hub & Installer
- Multi-Version Fabric Support: 26.3, 26.2, 26.1.2, 26.1.1, 26.1
>>>>>>> 2e3b71180319f8218b93d87a435c38a3ac76415c
- 5 Content Types: Mods, Resource Packs, Data Packs, Shaders, Modpacks (20,000+ items)
- 5 Distinct Themes: Modern Emerald, Classic Dark, Midnight Cyber, Amethyst Purple, Crimson Magma
- Custom Modpack & Profile Creator: Export official .mrpack archives or save custom local profiles
- Procedural Sound Effects Engine: Zero-latency audio with mute/unmute toggle
- 6 Languages: English (default), Italian, French, German, Spanish, Turkish
- Instant SQLite WAL caching with 256MB mmap & connection pooling
- Auto directory detection for Mods, Packs, Shaders, Datapacks (Manual for Modpacks)
- Double-click full overview & direct 1-click download
<<<<<<< HEAD
- Interactive 5-step tutorial & comprehensive v2.0 Patch Notes
=======
- Interactive 5-step tutorial & comprehensive v1.2 Patch Notes
>>>>>>> 2e3b71180319f8218b93d87a435c38a3ac76415c
"""

import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import time
import json
import webbrowser

from core.database import Database
from core.path_detector import get_auto_path, ensure_directory
from core.modrinth_api import ModrinthAPI
from ui.themes import THEMES, DEFAULT_THEME
from ui.translations import i18n, LANGUAGES
from core.sound_engine import sound
from ui.gui_components import (
    ItemDetailModal, WelcomeModal, TutorialModal, PatchNotesModal,
    ModpackCreatorModal, SavedProfilesModal, MinecraftToolsModal
)

<<<<<<< HEAD
SUPPORTED_VERSIONS = [
    "1.21.11", "1.21.10", "1.21.9", "1.21.8", "1.21.7", "1.21.6",
    "1.21.5", "1.21.4", "1.21.3", "1.21.2", "1.21.1", "1.21",
    "26.3", "26.2", "26.1.2", "26.1.1", "26.1"
]
DEFAULT_GV = "1.21.1"
=======
SUPPORTED_VERSIONS = ["26.3", "26.2", "26.1.2", "26.1.1", "26.1"]
DEFAULT_GV = "26.3"
>>>>>>> 2e3b71180319f8218b93d87a435c38a3ac76415c
DEFAULT_LOADER = "fabric"
PAGE_SIZE = 100

class TabController:
    """Manages the state and widgets of one content type tab."""
    def __init__(self, project_type, label_key):
        self.project_type = project_type
        self.label_key = label_key
        self.page = 1
        self.total_pages = 1
        self.total_count = 0
        self.search_query = ""
        self.selected_category = "All"
        self.sort_by = "downloads"
        self.sort_desc = True
        
        self.current_items = []
        self.selected_slugs = set()
        
        # Drag selection state
        self.drag = False
        self.drag_start = None
        self.drag_idx = None
        self.pre_sel = set()
        self.last_click = None
        self.last_motion = None
        
        # Widget references
        self.tree = None
        self.search_entry = None
        self.cat_menu = None
        self.sel_lbl = None
        self.tot_lbl = None
        self.path_entry = None
        self.pbar = None
        self.prog_lbl = None
        self.dl_btn = None
        self.cancel_btn = None
        self.page_lbl = None
        self.prev_btn = None
        self.next_btn = None
        self.auto_btn = None
        self.context_menu = None
        self.context_slug = None


class ModrinthApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.db = Database.get_instance()
        
        # Load theme & language
        saved_lang = self.db.get_setting("language", "en")
        i18n.set_language(saved_lang)
        self.current_lang = saved_lang

        saved_theme = self.db.get_setting("theme", DEFAULT_THEME)
        if saved_theme not in THEMES:
            saved_theme = DEFAULT_THEME
        self.current_theme_name = saved_theme
        self.theme = THEMES[saved_theme]

        # Sound effects setting
        saved_sound = self.db.get_setting("sound_enabled", "true")
        sound.set_enabled(saved_sound == "true")

        ctk.set_appearance_mode(self.theme["appearance"])
        ctk.set_default_color_theme("green")

        self.title(i18n.t("app_title"))
        self.geometry("1440x940")
        self.minsize(1150, 720)
        self.configure(fg_color=self.theme["bg"])

        saved_gv = self.db.get_setting("game_version", DEFAULT_GV)
        if saved_gv not in SUPPORTED_VERSIONS:
            saved_gv = DEFAULT_GV
        self.current_gv = saved_gv

        self.api = ModrinthAPI(gv=self.current_gv, loader=DEFAULT_LOADER)
        self.downloading = False
        self.cancel_flag = False
        self.search_timer = None

        self.is_online = ModrinthAPI.check_internet()

        self.tabs = {
            "mod": TabController("mod", "tab_mods"),
            "resourcepack": TabController("resourcepack", "tab_resourcepacks"),
            "datapack": TabController("datapack", "tab_datapacks"),
            "shader": TabController("shader", "tab_shaders"),
            "modpack": TabController("modpack", "tab_modpacks"),
        }

        self._style_tree()
        self._build_ui()
        self._load_all_tabs()

        if self.is_online:
            threading.Thread(target=self._background_check_updates, daemon=True).start()

    # ─── Treeview Styling ────────────────────────────────────────────────────
    def _style_tree(self):
        s = ttk.Style()
        s.theme_use("clam")
        s.configure(
            "M.Treeview", background=self.theme["card"], foreground=self.theme["txt"],
            fieldbackground=self.theme["card"], rowheight=32,
            font=("Segoe UI", 10), borderwidth=0, relief="flat"
        )
        s.configure(
            "M.Treeview.Heading", background=self.theme["surface"],
            foreground=self.theme["accent"], font=("Segoe UI", 10, "bold"),
            relief="flat", borderwidth=0, padding=(10, 6)
        )
        s.map("M.Treeview.Heading", background=[("active", self.theme["elevated"])])
        s.map("M.Treeview", background=[("selected", self.theme["sel_bg"])],
              foreground=[("selected", self.theme["sel_fg"])])
        s.configure(
            "Vertical.TScrollbar", background=self.theme["card"],
            troughcolor=self.theme["surface"], arrowcolor=self.theme["txt3"],
            borderwidth=0
        )
        s.map("Vertical.TScrollbar",
              background=[("active", self.theme["hover"]), ("!active", self.theme["elevated"])])

    # ─── UI Construction ─────────────────────────────────────────────────────
    def _build_ui(self):
        self._build_header()
        self._build_tabview()
        self._build_logpanel()
        self._build_statusbar()

    def _build_header(self):
        self.hdr = ctk.CTkFrame(self, fg_color=self.theme["surface"], corner_radius=0, height=62)
        self.hdr.pack(fill="x")
        self.hdr.pack_propagate(False)

        inn = ctk.CTkFrame(self.hdr, fg_color="transparent")
        inn.pack(fill="x", padx=20, pady=12)

        # Left branding
        left = ctk.CTkFrame(inn, fg_color="transparent")
        left.pack(side="left")
        self.logo_lbl = ctk.CTkLabel(left, text="⛏  Modrinth Mod Manager", font=("Segoe UI", 18, "bold"), text_color=self.theme["accent"])
        self.logo_lbl.pack(side="left")
<<<<<<< HEAD
        self.ver_tag = ctk.CTkLabel(left, text="  v2.0  ", font=("Segoe UI", 10, "bold"), fg_color=self.theme["elevated"], text_color=self.theme["accent_tx"], corner_radius=6)
=======
        self.ver_tag = ctk.CTkLabel(left, text="  v1.2  ", font=("Segoe UI", 10, "bold"), fg_color=self.theme["elevated"], text_color=self.theme["accent_tx"], corner_radius=6)
>>>>>>> 2e3b71180319f8218b93d87a435c38a3ac76415c
        self.ver_tag.pack(side="left", padx=(8, 12))

        status_txt = "● Online" if self.is_online else "○ Offline"
        status_col = self.theme["accent_tx"] if self.is_online else self.theme["orange"]
        self.net_lbl = ctk.CTkLabel(left, text=status_txt, font=("Segoe UI", 10, "bold"), text_color=status_col)
        self.net_lbl.pack(side="left")

        # Right Toolbar
        right = ctk.CTkFrame(inn, fg_color="transparent")
        right.pack(side="right")

        # Audio Sound Effects Toggle Button
        sound_icon = "🔊" if sound.is_enabled() else "🔇"
        self.sound_btn = ctk.CTkButton(
            right, text=sound_icon, width=38, height=30, corner_radius=8,
            font=("Segoe UI", 12), fg_color=self.theme["elevated"], hover_color=self.theme["hover"],
            text_color=self.theme["txt"], command=self._toggle_sound
        )
        self.sound_btn.pack(side="left", padx=(0, 6))

        # Modpack Creator & Saved Profiles
        self.create_pack_btn = ctk.CTkButton(
            right, text=f"📦 {i18n.t('btn_create_modpack')}", width=120, height=30, corner_radius=8,
            font=("Segoe UI", 10, "bold"), fg_color=self.theme["elevated"], hover_color=self.theme["hover"],
            text_color=self.theme["accent"], command=self._open_modpack_creator
        )
        self.create_pack_btn.pack(side="left", padx=(0, 6))

        self.profiles_btn = ctk.CTkButton(
            right, text=f"📋 {i18n.t('btn_saved_profiles')}", width=110, height=30, corner_radius=8,
            font=("Segoe UI", 10), fg_color=self.theme["elevated"], hover_color=self.theme["hover"],
            text_color=self.theme["txt2"], command=self._open_saved_profiles
        )
        self.profiles_btn.pack(side="left", padx=(0, 6))

        self.tools_btn = ctk.CTkButton(
            right, text=f"🛠 {i18n.t('btn_tools_suite')}", width=95, height=30, corner_radius=8,
            font=("Segoe UI", 10), fg_color=self.theme["elevated"], hover_color=self.theme["hover"],
            text_color=self.theme["txt2"], command=self._open_tools_suite
        )
        self.tools_btn.pack(side="left", padx=(0, 8))

        # Theme Selector ComboBox (5 Themes)
        ctk.CTkLabel(right, text=i18n.t("theme_selector_label"), font=("Segoe UI", 10), text_color=self.theme["txt3"]).pack(side="left", padx=(0, 4))
        self.theme_menu = ctk.CTkComboBox(
            right, values=list(THEMES.keys()), width=135, height=30, corner_radius=8,
            font=("Segoe UI", 10), fg_color=self.theme["elevated"], border_color=self.theme["border"],
            dropdown_fg_color=self.theme["card"], dropdown_hover_color=self.theme["hover"],
            dropdown_text_color=self.theme["txt"], state="readonly", command=self._on_theme_change
        )
        self.theme_menu.set(self.current_theme_name)
        self.theme_menu.pack(side="left", padx=(0, 6))

        # Language dropdown (6 Languages)
        lang_names = [name for code, name in LANGUAGES]
        current_lang_name = next((name for code, name in LANGUAGES if code == self.current_lang), "English")
        self.lang_dropdown = ctk.CTkComboBox(
            right, values=lang_names, width=105, height=30, corner_radius=8,
            font=("Segoe UI", 10), fg_color=self.theme["elevated"], border_color=self.theme["border"],
            dropdown_fg_color=self.theme["card"], dropdown_hover_color=self.theme["hover"],
            dropdown_text_color=self.theme["txt"], state="readonly", command=self._on_language_change
        )
        self.lang_dropdown.set(current_lang_name)
        self.lang_dropdown.pack(side="left", padx=(0, 6))

        # Action Buttons
        self.sync_btn = ctk.CTkButton(
            right, text=f"🔄 {i18n.t('btn_fetch_all')}", width=115, height=30, corner_radius=8,
            font=("Segoe UI", 10, "bold"), fg_color=self.theme["elevated"], hover_color=self.theme["hover"],
            text_color=self.theme["accent"], command=self._start_online_sync
        )
        self.sync_btn.pack(side="left", padx=(0, 6))

        self.pn_btn = ctk.CTkButton(
            right, text=f"📜 {i18n.t('btn_patch_notes')}", width=105, height=30, corner_radius=8,
            font=("Segoe UI", 10), fg_color=self.theme["elevated"], hover_color=self.theme["hover"],
            text_color=self.theme["txt"], command=self._open_patch_notes
        )
        self.pn_btn.pack(side="left", padx=(0, 6))

        self.tut_btn = ctk.CTkButton(
            right, text=f"❓ {i18n.t('btn_tutorial')}", width=88, height=30, corner_radius=8,
            font=("Segoe UI", 10), fg_color=self.theme["elevated"], hover_color=self.theme["hover"],
            text_color=self.theme["txt"], command=self._open_tutorial
        )
        self.tut_btn.pack(side="left", padx=(0, 6))

<<<<<<< HEAD
        # Version selector ComboBox (Fabric 1.21.x and 26.x)
        ctk.CTkLabel(right, text="MC", font=("Segoe UI", 10, "bold"), text_color=self.theme["txt3"]).pack(side="left", padx=(4, 4))
        self.ver_entry = ctk.CTkComboBox(
            right, values=SUPPORTED_VERSIONS, width=96, height=30, corner_radius=8,
=======
        # Version selector ComboBox (Fabric 26.3, 26.2, 26.1.2, 26.1.1, 26.1)
        ctk.CTkLabel(right, text="MC", font=("Segoe UI", 10, "bold"), text_color=self.theme["txt3"]).pack(side="left", padx=(4, 4))
        self.ver_entry = ctk.CTkComboBox(
            right, values=SUPPORTED_VERSIONS, width=82, height=30, corner_radius=8,
>>>>>>> 2e3b71180319f8218b93d87a435c38a3ac76415c
            font=("Segoe UI", 10, "bold"), fg_color=self.theme["elevated"], border_color=self.theme["border"],
            dropdown_fg_color=self.theme["card"], dropdown_hover_color=self.theme["hover"],
            dropdown_text_color=self.theme["txt"], state="readonly", command=self._on_version_change
        )
        self.ver_entry.set(self.current_gv)
        self.ver_entry.pack(side="left", padx=(0, 6))

        self.loader_badge = ctk.CTkLabel(
            right, text=" FABRIC ", font=("Segoe UI", 10, "bold"),
            fg_color=self.theme["accent"],
            text_color="#ffffff",
            corner_radius=6
        )
        self.loader_badge.pack(side="left")

    def _build_tabview(self):
        self.tabview = ctk.CTkTabview(
            self, fg_color=self.theme["bg"],
            segmented_button_fg_color=self.theme["surface"],
            segmented_button_selected_color=self.theme["accent"],
            segmented_button_selected_hover_color=self.theme["accent_h"],
            segmented_button_unselected_color=self.theme["elevated"],
            segmented_button_unselected_hover_color=self.theme["hover"],
            corner_radius=12, border_width=1, border_color=self.theme["border"]
        )
        self.tabview.pack(fill="both", expand=True, padx=16, pady=(6, 4))

        for ptype, tc in self.tabs.items():
            tab_name = i18n.t(tc.label_key)
            tab_frame = self.tabview.add(tab_name)
            self._build_tab_content(tab_frame, tc)

    def _build_tab_content(self, parent, tc):
        # ── Toolbar 1: Search, Filter, Pagination ────────────────────────────
        bar1 = ctk.CTkFrame(parent, fg_color="transparent")
        bar1.pack(fill="x", padx=8, pady=(8, 4))

        tc.search_entry = ctk.CTkEntry(
            bar1, width=280, height=34, corner_radius=8,
            placeholder_text=i18n.t("search_placeholder"), font=("Segoe UI", 11),
            fg_color=self.theme["elevated"], border_color=self.theme["border"], text_color=self.theme["txt"]
        )
        tc.search_entry.pack(side="left", padx=(0, 10))
        tc.search_entry.bind("<KeyRelease>", lambda _: self._debounce_search(tc))

        # Category dropdown (Localized category names)
        tc.cat_menu = ctk.CTkComboBox(
            bar1, width=190, height=34, corner_radius=8, values=[i18n.t("all_categories")],
            state="readonly", fg_color=self.theme["elevated"], border_color=self.theme["border"],
            dropdown_fg_color=self.theme["card"], dropdown_hover_color=self.theme["hover"],
            dropdown_text_color=self.theme["txt"], font=("Segoe UI", 11),
            command=lambda val: self._on_category_select(tc, val)
        )
        tc.cat_menu.set(i18n.t("all_categories"))
        tc.cat_menu.pack(side="left", padx=(0, 12))

        # Pagination controls
        pag_frame = ctk.CTkFrame(bar1, fg_color="transparent")
        pag_frame.pack(side="right")

        tc.prev_btn = ctk.CTkButton(
            pag_frame, text=i18n.t("page_prev"), width=72, height=32, corner_radius=6,
            font=("Segoe UI", 10), fg_color=self.theme["elevated"], hover_color=self.theme["hover"],
            text_color=self.theme["txt"], command=lambda: self._page_change(tc, -1)
        )
        tc.prev_btn.pack(side="left", padx=(0, 6))

        tc.page_lbl = ctk.CTkLabel(
            pag_frame, text="Page 1 of 1", font=("Segoe UI", 11), text_color=self.theme["txt2"]
        )
        tc.page_lbl.pack(side="left", padx=8)

        tc.next_btn = ctk.CTkButton(
            pag_frame, text=i18n.t("page_next"), width=72, height=32, corner_radius=6,
            font=("Segoe UI", 10), fg_color=self.theme["elevated"], hover_color=self.theme["hover"],
            text_color=self.theme["txt"], command=lambda: self._page_change(tc, 1)
        )
        tc.next_btn.pack(side="left", padx=(6, 0))

        # ── Toolbar 2: Multi-Select, Export, Counter ─────────────────────────
        bar2 = ctk.CTkFrame(parent, fg_color="transparent")
        bar2.pack(fill="x", padx=8, pady=(0, 4))

        ctk.CTkButton(
            bar2, text=i18n.t("btn_select_all"), width=110, height=28, corner_radius=6,
            font=("Segoe UI", 10), fg_color=self.theme["elevated"], hover_color=self.theme["hover"],
            text_color=self.theme["txt2"], command=lambda: self._select_all_page(tc)
        ).pack(side="left", padx=(0, 6))

        ctk.CTkButton(
            bar2, text=i18n.t("btn_deselect_all"), width=110, height=28, corner_radius=6,
            font=("Segoe UI", 10), fg_color=self.theme["elevated"], hover_color=self.theme["hover"],
            text_color=self.theme["txt2"], command=lambda: self._deselect_all(tc)
        ).pack(side="left", padx=(0, 6))

        ctk.CTkButton(
            bar2, text=i18n.t("btn_export"), width=90, height=28, corner_radius=6,
            font=("Segoe UI", 10), fg_color=self.theme["elevated"], hover_color=self.theme["hover"],
            text_color=self.theme["txt2"], command=lambda: self._export_json(tc)
        ).pack(side="left", padx=(0, 6))

        ctk.CTkButton(
            bar2, text=i18n.t("btn_import"), width=90, height=28, corner_radius=6,
            font=("Segoe UI", 10), fg_color=self.theme["elevated"], hover_color=self.theme["hover"],
            text_color=self.theme["txt2"], command=lambda: self._import_json(tc)
        ).pack(side="left", padx=(0, 6))

        ctk.CTkButton(
            bar2, text=f"📦 {i18n.t('btn_create_modpack')}", width=120, height=28, corner_radius=6,
            font=("Segoe UI", 10, "bold"), fg_color=self.theme["elevated"], hover_color=self.theme["hover"],
            text_color=self.theme["accent"], command=lambda: self._open_modpack_creator_for_tab(tc)
        ).pack(side="left", padx=(0, 10))

        hint_text = "🖱 Double-Click: Details & Download · Drag: Multi-Select · Shift: Range · Right-Click: Menu"
        ctk.CTkLabel(bar2, text=hint_text, font=("Segoe UI", 9), text_color=self.theme["txt3"]).pack(side="left")

        # Counter
        ctr = ctk.CTkFrame(bar2, fg_color="transparent")
        ctr.pack(side="right")
        ctk.CTkLabel(ctr, text=f"{i18n.t('selected_counter')}:", font=("Segoe UI", 10), text_color=self.theme["txt3"]).pack(side="left")
        tc.sel_lbl = ctk.CTkLabel(ctr, text="0", font=("Segoe UI", 16, "bold"), text_color=self.theme["accent"])
        tc.sel_lbl.pack(side="left", padx=(4, 2))
        ctk.CTkLabel(ctr, text="/", font=("Segoe UI", 12), text_color=self.theme["txt3"]).pack(side="left")
        tc.tot_lbl = ctk.CTkLabel(ctr, text="0", font=("Segoe UI", 12), text_color=self.theme["txt2"])
        tc.tot_lbl.pack(side="left", padx=(2, 0))

        # ── Treeview Table ───────────────────────────────────────────────────
        tf = ctk.CTkFrame(parent, fg_color=self.theme["surface"], corner_radius=10, border_width=1, border_color=self.theme["border"])
        tf.pack(fill="both", expand=True, padx=8, pady=2)

        inner = tk.Frame(tf, bg=self.theme["surface"])
        inner.pack(fill="both", expand=True, padx=2, pady=2)

        cols = ("sel", "idx", "title", "author", "downloads", "date", "category", "desc")
        tc.tree = ttk.Treeview(inner, columns=cols, show="headings", style="M.Treeview")

        headers = {
            "sel": (i18n.t("col_select"), 36),
            "idx": (i18n.t("col_index"), 44),
            "title": (i18n.t("col_title"), 220),
            "author": (i18n.t("col_author"), 120),
            "downloads": (i18n.t("col_downloads"), 100),
            "date": (i18n.t("col_updated"), 95),
            "category": (i18n.t("col_category"), 160),
            "desc": (i18n.t("col_description"), 420)
        }

        for col, (label, width) in headers.items():
            anchor = "center" if col in ("sel", "idx", "date") else ("e" if col == "downloads" else "w")
            cmd = (lambda c=col: self._sort_column(tc, c)) if col in ("title", "author", "downloads", "date", "category") else None
            tc.tree.heading(col, text=label, command=cmd) if cmd else tc.tree.heading(col, text=label)
            tc.tree.column(col, width=width, minwidth=width // 2, anchor=anchor, stretch=col not in ("sel", "idx"))

        vsb = ttk.Scrollbar(inner, orient="vertical", command=tc.tree.yview)
        tc.tree.configure(yscrollcommand=vsb.set)
        tc.tree.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")

        tc.tree.tag_configure("sel", background=self.theme["sel_bg"], foreground=self.theme["sel_fg"])
        tc.tree.tag_configure("a", background=self.theme["row_a"])
        tc.tree.tag_configure("b", background=self.theme["row_b"])

        # Bindings
        tc.tree.bind("<ButtonPress-1>", lambda e: self._on_tree_press(tc, e))
        tc.tree.bind("<B1-Motion>", lambda e: self._on_tree_motion(tc, e))
        tc.tree.bind("<ButtonRelease-1>", lambda e: self._on_tree_release(tc, e))
        tc.tree.bind("<Double-1>", lambda e: self._on_tree_double_click(tc, e))
        tc.tree.bind("<Button-3>", lambda e: self._on_tree_right_click(tc, e))

        # Context menu
        tc.context_menu = tk.Menu(
            self, tearoff=0, bg=self.theme["card"], fg=self.theme["txt"],
            activebackground=self.theme["accent"], activeforeground="black",
            font=("Segoe UI", 10), bd=0
        )
        tc.context_menu.add_command(label="📖 View Full Details", command=lambda: self._ctx_details(tc))
        tc.context_menu.add_command(label="🌐 Open on Modrinth.com", command=lambda: self._ctx_open_web(tc))
        tc.context_menu.add_separator()
        tc.context_menu.add_command(label="☑ Toggle Selection", command=lambda: self._ctx_toggle(tc))
        tc.context_menu.add_command(label="🏷 Select All in Same Category", command=lambda: self._ctx_select_category(tc))
        tc.context_menu.add_command(label="📋 Copy Title", command=lambda: self._ctx_copy_title(tc))

        # ── Bottom Path & Action Bar ─────────────────────────────────────────
        bot = ctk.CTkFrame(parent, fg_color="transparent")
        bot.pack(fill="x", padx=8, pady=(4, 6))

        r1 = ctk.CTkFrame(bot, fg_color="transparent")
        r1.pack(fill="x", pady=(0, 6))

        is_modpack = tc.project_type == "modpack"
        detected_path = get_auto_path(tc.project_type)
        tc.path_entry = ctk.CTkEntry(
            r1, height=32, corner_radius=8, font=("Consolas", 10),
            fg_color=self.theme["elevated"], border_color=self.theme["border"], text_color=self.theme["txt"]
        )
        if detected_path:
            tc.path_entry.insert(0, detected_path)
        else:
            tc.path_entry.configure(placeholder_text="Select destination Minecraft instance folder...")
        tc.path_entry.pack(side="left", fill="x", expand=True, padx=(0, 6))

        # Note user rule: Modpacks do NOT have auto-detect!
        if not is_modpack:
            tc.auto_btn = ctk.CTkButton(
                r1, text=f"🎯 {i18n.t('btn_auto_detect')}", width=140, height=32, corner_radius=8,
                font=("Segoe UI", 10, "bold"), fg_color=self.theme["elevated"], hover_color=self.theme["hover"],
                text_color=self.theme["accent_tx"], command=lambda: self._reset_auto_path(tc)
            )
            tc.auto_btn.pack(side="left", padx=(0, 6))

        ctk.CTkButton(
            r1, text=f"📂 {i18n.t('btn_browse')}", width=90, height=32, corner_radius=8,
            font=("Segoe UI", 10), fg_color=self.theme["elevated"], hover_color=self.theme["hover"],
            text_color=self.theme["txt2"], command=lambda: self._browse_path(tc)
        ).pack(side="left", padx=(0, 6))

        ctk.CTkButton(
            r1, text=f"📁 {i18n.t('btn_open_folder')}", width=110, height=32, corner_radius=8,
            font=("Segoe UI", 10), fg_color=self.theme["elevated"], hover_color=self.theme["hover"],
            text_color=self.theme["txt2"], command=lambda: self._open_dest_folder(tc)
        ).pack(side="left")

        # Action row
        r2 = ctk.CTkFrame(bot, fg_color="transparent")
        r2.pack(fill="x")

        dl_text = i18n.t("btn_install_modpack") if is_modpack else i18n.t("btn_download_selected")
        tc.dl_btn = ctk.CTkButton(
            r2, text=f"⬇  {dl_text}", width=210, height=36, corner_radius=8,
            font=("Segoe UI", 12, "bold"), fg_color=self.theme["accent"], hover_color=self.theme["accent_h"],
            text_color="#ffffff",
            command=lambda: self._start_download(tc)
        )
        tc.dl_btn.pack(side="left", padx=(0, 8))

        tc.cancel_btn = ctk.CTkButton(
            r2, text="⛔", width=44, height=36, corner_radius=8,
            fg_color=self.theme["red"], hover_color="#dc2626", text_color="white",
            command=self._cancel_download, state="disabled"
        )
        tc.cancel_btn.pack(side="left", padx=(0, 10))

        tc.pbar = ctk.CTkProgressBar(
            r2, height=12, corner_radius=6, fg_color=self.theme["elevated"], progress_color=self.theme["accent"]
        )
        tc.pbar.set(0)
        tc.pbar.pack(side="left", fill="x", expand=True, padx=(0, 8))

        tc.prog_lbl = ctk.CTkLabel(r2, text="", font=("Segoe UI", 10), text_color=self.theme["txt2"])
        tc.prog_lbl.pack(side="right")

    # ─── Log & Status Bar ────────────────────────────────────────────────────
    def _build_logpanel(self):
        self.lf = ctk.CTkFrame(self, fg_color=self.theme["surface"], corner_radius=10, border_width=1, border_color=self.theme["border"], height=95)
        self.lf.pack(fill="x", padx=16, pady=(2, 4))
        self.lf.pack_propagate(False)

        self.log_box = ctk.CTkTextbox(
            self.lf, height=85, corner_radius=8, fg_color=self.theme["card"],
            text_color=self.theme["txt2"], font=("Cascadia Code", 10), state="disabled", wrap="word"
        )
        self.log_box.pack(fill="both", expand=True, padx=5, pady=5)

    def _log(self, text):
        self.log_box.configure(state="normal")
        self.log_box.insert("end", text + "\n")
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    def _build_statusbar(self):
        self.sb = ctk.CTkFrame(self, fg_color=self.theme["surface"], corner_radius=0, height=24)
        self.sb.pack(fill="x", side="bottom")
        self.sb.pack_propagate(False)

        self.status_lbl = ctk.CTkLabel(self.sb, text=i18n.t("status_ready"), font=("Segoe UI", 9), text_color=self.theme["txt3"])
        self.status_lbl.pack(side="left", padx=16)

<<<<<<< HEAD
        ctk.CTkLabel(self.sb, text="Modrinth Mod Manager v2.0  ·  Official Release", font=("Segoe UI", 9), text_color=self.theme["txt3"]).pack(side="right", padx=16)
=======
        ctk.CTkLabel(self.sb, text="Modrinth Mod Manager v1.2  ·  Official Release", font=("Segoe UI", 9), text_color=self.theme["txt3"]).pack(side="right", padx=16)
>>>>>>> 2e3b71180319f8218b93d87a435c38a3ac76415c

    def _st(self, msg):
        self.status_lbl.configure(text=msg)

    # ─── Version, Theme & Language Switching ─────────────────────────────────
    def _on_version_change(self, selected_gv):
        if selected_gv in SUPPORTED_VERSIONS and selected_gv != self.current_gv:
<<<<<<< HEAD
            sound.play_toggle()
=======
>>>>>>> 2e3b71180319f8218b93d87a435c38a3ac76415c
            self.current_gv = selected_gv
            self.api.gv = selected_gv
            self.db.set_setting("game_version", selected_gv)
            self._log(f"🔄 Switched Minecraft Fabric version to {selected_gv}")
            self._st(f"Switched to Fabric {selected_gv}")
            for tc in self.tabs.values():
                tc.page = 1
                tc.selected_category = "All"
                raw_cats = self.db.get_categories(tc.project_type, version=self.current_gv)
                cat_labels = [i18n.t("all_categories")] + [i18n.t_cat(c) for c in raw_cats]
                tc.cat_menu.configure(values=cat_labels)
                tc.cat_menu.set(i18n.t("all_categories"))
                self._render_page(tc)
<<<<<<< HEAD

=======
>>>>>>> 2e3b71180319f8218b93d87a435c38a3ac76415c
    def _on_theme_change(self, theme_name):
        if theme_name in THEMES and theme_name != self.current_theme_name:
            sound.play_toggle()
            self.current_theme_name = theme_name
            self.theme = THEMES[theme_name]
            self.db.set_setting("theme", theme_name)
            ctk.set_appearance_mode(self.theme["appearance"])
            self._apply_theme_colors()

    def _apply_theme_colors(self):
        self.configure(fg_color=self.theme["bg"])
        self.hdr.configure(fg_color=self.theme["surface"])
        self.logo_lbl.configure(text_color=self.theme["accent"])
        self.ver_tag.configure(fg_color=self.theme["elevated"], text_color=self.theme["accent_tx"])
        self.sound_btn.configure(fg_color=self.theme["elevated"], text_color=self.theme["txt"])
        self.create_pack_btn.configure(fg_color=self.theme["elevated"], text_color=self.theme["accent"])
        self.profiles_btn.configure(fg_color=self.theme["elevated"], text_color=self.theme["txt2"])
        self.tools_btn.configure(fg_color=self.theme["elevated"], text_color=self.theme["txt2"])
        self.sync_btn.configure(fg_color=self.theme["elevated"], text_color=self.theme["accent"])
        self.pn_btn.configure(fg_color=self.theme["elevated"], text_color=self.theme["txt"])
        self.tut_btn.configure(fg_color=self.theme["elevated"], text_color=self.theme["txt"])
        self.loader_badge.configure(fg_color=self.theme["accent"], text_color="#ffffff")
        
        self.tabview.configure(
            fg_color=self.theme["bg"],
            segmented_button_fg_color=self.theme["surface"],
            segmented_button_selected_color=self.theme["accent"],
            segmented_button_selected_hover_color=self.theme["accent_h"],
            segmented_button_unselected_color=self.theme["elevated"],
            segmented_button_unselected_hover_color=self.theme["hover"]
        )

        self._style_tree()
        self._refresh_language_texts()

    def _on_language_change(self, selected_lang_name):
        code = next((c for c, n in LANGUAGES if n == selected_lang_name), "en")
        if code != self.current_lang:
            sound.play_toggle()
            self.current_lang = code
            i18n.set_language(code)
            self.db.set_setting("language", code)
            self._refresh_language_texts()

    def _refresh_language_texts(self):
        self.title(i18n.t("app_title"))
        self.create_pack_btn.configure(text=f"📦 {i18n.t('btn_create_modpack')}")
        self.profiles_btn.configure(text=f"📋 {i18n.t('btn_saved_profiles')}")
        self.tools_btn.configure(text=f"🛠 {i18n.t('btn_tools_suite')}")
        self.sync_btn.configure(text=f"🔄 {i18n.t('btn_fetch_all')}")
        self.pn_btn.configure(text=f"📜 {i18n.t('btn_patch_notes')}")
        self.tut_btn.configure(text=f"❓ {i18n.t('btn_tutorial')}")
        self._st(i18n.t("status_ready"))

        for tc in self.tabs.values():
            raw_cats = self.db.get_categories(tc.project_type, version=self.current_gv)
            cat_labels = [i18n.t("all_categories")] + [i18n.t_cat(c) for c in raw_cats]
            tc.cat_menu.configure(values=cat_labels)
            tc.cat_menu.set(i18n.t("all_categories"))
            self._render_page(tc)

    def _show_welcome_screen(self):
        WelcomeModal(self, self.theme, on_start=None, on_open_tutorial=self._open_tutorial, is_online=self.is_online)

    def _toggle_sound(self):
        enabled = sound.toggle()
        icon = "🔊" if enabled else "🔇"
        self.sound_btn.configure(text=icon)
        self.db.set_setting("sound_enabled", "true" if enabled else "false")
        status_str = "Enabled" if enabled else "Muted"
        self._st(f"Audio effects: {status_str}")
        if enabled:
            sound.play_toggle()

    def _open_tutorial(self):
        sound.play_click()
        TutorialModal(self, self.theme)

    def _open_patch_notes(self):
        sound.play_click()
        PatchNotesModal(self, self.theme)

    def _open_modpack_creator(self):
        sound.play_click()
        all_selected = []
        for tc in self.tabs.values():
            for s in tc.selected_slugs:
                item = self.db.get_item(s, project_type=tc.project_type)
                if item and item not in all_selected:
                    all_selected.append(item)
        ModpackCreatorModal(self, initial_items=all_selected, theme=self.theme, current_gv=self.current_gv)

    def _open_modpack_creator_for_tab(self, tc):
        sound.play_click()
        tab_selected = []
        for s in tc.selected_slugs:
            item = self.db.get_item(s, project_type=tc.project_type)
            if item:
                tab_selected.append(item)
        ModpackCreatorModal(self, initial_items=tab_selected, theme=self.theme, current_gv=self.current_gv)

    def _open_saved_profiles(self):
        sound.play_click()
        SavedProfilesModal(self, self.theme, on_apply=self._apply_loaded_profile)

    def _apply_loaded_profile(self, profile):
        try:
            profile_gv = profile.get("game_version")
            if profile_gv and profile_gv in SUPPORTED_VERSIONS and profile_gv != self.current_gv:
                self.ver_entry.set(profile_gv)
                self._on_version_change(profile_gv)

            for tc in self.tabs.values():
                tc.selected_slugs.clear()

            items = profile.get("items", [])
            selected_count = 0
            for item in items:
                slug = item.get("slug")
                ptype = item.get("project_type", "mod")
                if ptype in self.tabs and slug:
                    self.tabs[ptype].selected_slugs.add(slug)
                    selected_count += 1

            for tc in self.tabs.values():
                self._refresh_tags(tc)

            sound.play_success()
            prof_name = profile.get("name", "Custom Profile")
            self._log(f"📋 Loaded profile '{prof_name}' with {selected_count} items (MC {self.current_gv}).")
            self._st(f"Loaded profile '{prof_name}' ({selected_count} items)")
            messagebox.showinfo("Profile Loaded", f"Successfully loaded profile '{prof_name}' with {selected_count} items!")
        except Exception as e:
            sound.play_error()
            messagebox.showerror("Error", f"Failed to apply profile: {e}")

    def _open_tools_suite(self):
        sound.play_click()
        MinecraftToolsModal(self, self.theme, current_gv=self.current_gv, on_apply_preset=self._handle_apply_preset)

    def _handle_apply_preset(self, slugs, name):
        tc = self.tabs["mod"]
        tc.selected_slugs.clear()
        found = 0
        for s in slugs:
            item = self.db.get_item(s, project_type="mod")
            if item:
                tc.selected_slugs.add(s)
                found += 1
            else:
                matches = self.db.query_items("mod", search=s, limit=1, version=self.current_gv)
                if matches:
                    tc.selected_slugs.add(matches[0]["slug"])
                    found += 1

        self.tabview.set(i18n.t(tc.label_key))
        self._refresh_tags(tc)
        sound.play_success()
        self._log(f"⚡ Applied preset '{name}': {found} mods selected in Mods tab.")
        self._st(f"Applied preset: {name} ({found} mods selected)")
        messagebox.showinfo("Preset Applied", f"Selected {found} mods from '{name}' in the Mods tab!\nYou can now click 'Download Selected' to install them.")

    # ─── Data Loading & Pagination ───────────────────────────────────────────
    def _load_all_tabs(self):
        for tc in self.tabs.values():
            raw_cats = self.db.get_categories(tc.project_type, version=self.current_gv)
            cat_labels = [i18n.t("all_categories")] + [i18n.t_cat(c) for c in raw_cats]
            tc.cat_menu.configure(values=cat_labels)
            tc.cat_menu.set(i18n.t("all_categories"))
            self._render_page(tc)

    def _render_page(self, tc):
        tc.total_count = self.db.get_count(tc.project_type, search=tc.search_query, category=tc.selected_category, version=self.current_gv)
        tc.total_pages = max(1, (tc.total_count + PAGE_SIZE - 1) // PAGE_SIZE)
        tc.page = max(1, min(tc.page, tc.total_pages))

        offset = (tc.page - 1) * PAGE_SIZE
        tc.current_items = self.db.query_items(
            tc.project_type, search=tc.search_query, category=tc.selected_category,
            sort_by=tc.sort_by, sort_desc=tc.sort_desc, limit=PAGE_SIZE, offset=offset,
            version=self.current_gv
        )

        page_str = i18n.t("page_indicator", cur=tc.page, tot=tc.total_pages, count=f"{tc.total_count:,}")
        tc.page_lbl.configure(text=page_str)
        tc.prev_btn.configure(state="normal" if tc.page > 1 else "disabled")
        tc.next_btn.configure(state="normal" if tc.page < tc.total_pages else "disabled")
        tc.tot_lbl.configure(text=f"{tc.total_count:,}")
        tc.sel_lbl.configure(text=str(len(tc.selected_slugs)))

        tc.tree.delete(*tc.tree.get_children())
        start_idx = offset + 1

        for i, item in enumerate(tc.current_items, start_idx):
            slug = item.get("slug", f"item_{i}")
            is_sel = slug in tc.selected_slugs
            ch = "☑" if is_sel else "☐"
            tag = "sel" if is_sel else ("a" if (i % 2 == 0) else "b")

            dls = self._format_downloads(item.get("downloads", 0))
            date_str = self._format_date(item.get("date_modified", ""))
            cat_key = item.get("primary_category", "utility")
            cat_display = i18n.t_cat(cat_key)

            try:
                tc.tree.insert(
                    "", "end", iid=slug,
                    values=(ch, i, item.get("title", slug), item.get("author", "—"),
                            dls, date_str, cat_display, item.get("description", "")),
                    tags=(tag,)
                )
            except tk.TclError:
                tc.tree.insert(
                    "", "end", iid=f"{slug}_{i}",
                    values=(ch, i, item.get("title", slug), item.get("author", "—"),
                            dls, date_str, cat_display, item.get("description", "")),
                    tags=(tag,)
                )

    def _page_change(self, tc, delta):
        new_page = tc.page + delta
        if 1 <= new_page <= tc.total_pages:
            sound.play_click()
            tc.page = new_page
            self._render_page(tc)

    def _debounce_search(self, tc):
        if self.search_timer:
            self.after_cancel(self.search_timer)
        self.search_timer = self.after(250, lambda: self._apply_search(tc))

    def _apply_search(self, tc):
        tc.search_query = tc.search_entry.get().strip()
        tc.page = 1
        self._render_page(tc)
        self._st(f"🔍 Found {tc.total_count:,} items")

    def _on_category_select(self, tc, value):
        all_label = i18n.t("all_categories")
        if value == all_label:
            tc.selected_category = "All"
        else:
            # Reverse lookup localized category back to key
            raw_cats = self.db.get_categories(tc.project_type, version=self.current_gv)
            matched = next((c for c in raw_cats if i18n.t_cat(c) == value), value)
            tc.selected_category = matched

        tc.page = 1
        self._render_page(tc)

    def _sort_column(self, tc, col):
        col_db_map = {
            "title": "title",
            "author": "author",
            "downloads": "downloads",
            "date": "date_modified",
            "category": "primary_category"
        }
        db_col = col_db_map.get(col, "downloads")
        if tc.sort_by == db_col:
            tc.sort_desc = not tc.sort_desc
        else:
            tc.sort_by = db_col
            tc.sort_desc = True
        self._render_page(tc)

    @staticmethod
    def _format_downloads(n):
        if n >= 1e9: return f"{n/1e9:.1f}B"
        if n >= 1e6: return f"{n/1e6:.1f}M"
        if n >= 1e3: return f"{n/1e3:.1f}K"
        return str(n)

    @staticmethod
    def _format_date(s):
        if not s: return ""
        try:
            return s[:10]
        except:
            return s

    # ─── Treeview Gestures ───────────────────────────────────────────────────
    def _get_tree_items(self, tc):
        return list(tc.tree.get_children())

    def _on_tree_press(self, tc, e):
        if tc.tree.identify("region", e.x, e.y) == "heading":
            return
        item = tc.tree.identify_row(e.y)
        if not item:
            return
        ctrl = bool(e.state & 0x4)
        shift = bool(e.state & 0x1)

        if shift and tc.last_click:
            self._range_select(tc, tc.last_click, item)
            return "break"
        if ctrl:
            self._toggle_row(tc, item)
            tc.last_click = item
            return "break"

        tc.drag = True
        tc.drag_start = item
        items = self._get_tree_items(tc)
        tc.drag_idx = items.index(item) if item in items else 0
        tc.pre_sel = set(tc.selected_slugs)
        tc.last_motion = item
        return "break"

    def _on_tree_motion(self, tc, e):
        if not tc.drag:
            return
        h = tc.tree.winfo_height()
        if e.y < 8:
            tc.tree.yview_scroll(-3, "units")
        elif e.y > h - 8:
            tc.tree.yview_scroll(3, "units")

        item = tc.tree.identify_row(e.y)
        if not item or item == tc.last_motion:
            return
        tc.last_motion = item
        items = self._get_tree_items(tc)
        try:
            ci = items.index(item)
        except ValueError:
            return
        lo, hi = min(tc.drag_idx, ci), max(tc.drag_idx, ci)
        tc.selected_slugs = set(tc.pre_sel)
        for i in range(lo, hi + 1):
            tc.selected_slugs.add(items[i])
        self._refresh_tags(tc)

    def _on_tree_release(self, tc, e):
        if not tc.drag:
            return
        tc.drag = False
        item = tc.tree.identify_row(e.y)
        if item and item == tc.drag_start:
            tc.selected_slugs = set(tc.pre_sel)
            self._toggle_row(tc, item)
        else:
            self._refresh_tags(tc)
        tc.last_click = item or tc.drag_start

    def _toggle_row(self, tc, slug):
        if slug in tc.selected_slugs:
            tc.selected_slugs.discard(slug)
        else:
            tc.selected_slugs.add(slug)
        sound.play_select()
        self._tag_single(tc, slug)
        tc.sel_lbl.configure(text=str(len(tc.selected_slugs)))

    def _tag_single(self, tc, slug):
        if not tc.tree.exists(slug):
            return
        v = list(tc.tree.item(slug, "values"))
        idx = int(v[1]) if len(v) > 1 else 0
        if slug in tc.selected_slugs:
            v[0] = "☑"
            tc.tree.item(slug, values=v, tags=("sel",))
        else:
            v[0] = "☐"
            tag = "a" if idx % 2 == 0 else "b"
            tc.tree.item(slug, values=v, tags=(tag,))

    def _refresh_tags(self, tc):
        for slug in self._get_tree_items(tc):
            self._tag_single(tc, slug)
        tc.sel_lbl.configure(text=str(len(tc.selected_slugs)))

    def _range_select(self, tc, a, b):
        items = self._get_tree_items(tc)
        try:
            ia, ib = items.index(a), items.index(b)
        except ValueError:
            return
        for i in range(min(ia, ib), max(ia, ib) + 1):
            tc.selected_slugs.add(items[i])
        sound.play_select()
        self._refresh_tags(tc)

    def _select_all_page(self, tc):
        for slug in self._get_tree_items(tc):
            tc.selected_slugs.add(slug)
        sound.play_select()
        self._refresh_tags(tc)

    def _deselect_all(self, tc):
        tc.selected_slugs.clear()
        sound.play_click()
        self._refresh_tags(tc)

    # ─── Double Click & Context Menu ─────────────────────────────────────────
    def _on_tree_double_click(self, tc, e):
        slug = tc.tree.identify_row(e.y)
        if slug:
            item_data = self.db.get_item(slug, project_type=tc.project_type)
            if item_data:
                sound.play_click()
                ItemDetailModal(self, item_data, self.theme, on_download=lambda m: self._download_single(tc, m))
        return "break"

    def _on_tree_right_click(self, tc, e):
        slug = tc.tree.identify_row(e.y)
        if slug:
            tc.context_slug = slug
            tc.context_menu.tk_popup(e.x_root, e.y_root)

    def _ctx_details(self, tc):
        if tc.context_slug:
            item_data = self.db.get_item(tc.context_slug, project_type=tc.project_type)
            if item_data:
                sound.play_click()
                ItemDetailModal(self, item_data, self.theme, on_download=lambda m: self._download_single(tc, m))

    def _ctx_open_web(self, tc):
        if tc.context_slug:
            webbrowser.open(f"https://modrinth.com/{tc.project_type}/{tc.context_slug}")

    def _ctx_toggle(self, tc):
        if tc.context_slug:
            self._toggle_row(tc, tc.context_slug)

    def _ctx_select_category(self, tc):
        if not tc.context_slug:
            return
        item = self.db.get_item(tc.context_slug, project_type=tc.project_type)
        if not item:
            return
        cat = item.get("primary_category")
        n = 0
        for current in tc.current_items:
            if current.get("primary_category") == cat:
                tc.selected_slugs.add(current.get("slug"))
                n += 1
        self._refresh_tags(tc)
        self._st(f"☑ Selected {n} items with category: {i18n.t_cat(cat)}")

    def _ctx_copy_title(self, tc):
        if tc.context_slug:
            item = self.db.get_item(tc.context_slug, project_type=tc.project_type)
            if item:
                self.clipboard_clear()
                self.clipboard_append(item.get("title", ""))

    # ─── Directory Management ────────────────────────────────────────────────
    def _reset_auto_path(self, tc):
        auto_dir = get_auto_path(tc.project_type)
        if auto_dir:
            tc.path_entry.delete(0, "end")
            tc.path_entry.insert(0, auto_dir)
            self._st(f"🎯 Auto-detected destination: {auto_dir}")

    def _browse_path(self, tc):
        d = filedialog.askdirectory(title="Select Target Folder")
        if d:
            tc.path_entry.delete(0, "end")
            tc.path_entry.insert(0, d)

    def _open_dest_folder(self, tc):
        path = tc.path_entry.get().strip()
        if path and os.path.exists(path):
            os.startfile(path)
        elif path:
            ensure_directory(path)
            os.startfile(path)

    # ─── Download & Installation Logic ───────────────────────────────────────
    def _cancel_download(self):
        self.cancel_flag = True
        sound.play_error()
        self._st("⛔ Cancelling operations...")

    def _download_single(self, tc, item):
        dest_dir = tc.path_entry.get().strip()
        if not dest_dir:
            sound.play_error()
            messagebox.showwarning("Warning", "Please select a target folder first.")
            return
        ensure_directory(dest_dir)
        sound.play_start()
        self._log(f"⬇ Downloading single item: {item.get('title')} → {dest_dir}")
        threading.Thread(target=self._download_worker, args=(tc, [item], dest_dir), daemon=True).start()

    def _start_download(self, tc):
        if self.downloading:
            return
        if not tc.selected_slugs:
            sound.play_error()
            messagebox.showwarning("Warning", "No items selected! Check at least one item.")
            return

        dest_dir = tc.path_entry.get().strip()
        if not dest_dir:
            sound.play_error()
            messagebox.showwarning("Warning", "Please select a target destination folder.")
            return

        ensure_directory(dest_dir)
        selected_items = [self.db.get_item(s, project_type=tc.project_type) for s in tc.selected_slugs if self.db.get_item(s, project_type=tc.project_type)]

        is_pack = tc.project_type == "modpack"
        if is_pack and len(selected_items) == 1:
            title = selected_items[0].get("title", "Modpack")
            confirm = messagebox.askyesno(
                i18n.t("confirm_install_title"),
                i18n.t("confirm_install_msg", title=title, path=dest_dir)
            )
            if not confirm:
                return
            self._start_modpack_install(tc, selected_items[0], dest_dir)
            return

        confirm = messagebox.askyesno(
            i18n.t("confirm_dl_title"),
            i18n.t("confirm_dl_msg", count=len(selected_items), ptype=tc.project_type, path=dest_dir)
        )
        if not confirm:
            return

        sound.play_start()
        self.downloading = True
        self.cancel_flag = False
        tc.dl_btn.configure(state="disabled")
        tc.cancel_btn.configure(state="normal")
        tc.pbar.set(0)

        self._log(f"\n⬇ Starting parallel multi-threaded download of {len(selected_items)} {tc.project_type}s to: {dest_dir}")
        threading.Thread(target=self._download_worker, args=(tc, selected_items, dest_dir), daemon=True).start()

    def _download_worker(self, tc, items, dest_dir):
        import concurrent.futures
        total = len(items)
        counters = {"ok": 0, "fail": 0, "deps": 0, "skip": 0, "processed": 0}
        done_ids = set()
        lock = threading.Lock()

        def log(msg):
            self.after(0, self._log, msg)

        def process_item(item):
            if self.cancel_flag:
                return

            title = item.get("title", item.get("slug"))
            pid = item.get("project_id", item.get("slug"))

            ver = self.api.get_compatible_version(pid, project_type=tc.project_type)
            if not ver:
                log(f"  ⚠ {title}: No compatible version found.")
                with lock:
                    counters["fail"] += 1
                    counters["processed"] += 1
                    p = counters["processed"]
                    self.after(0, tc.pbar.set, p / total)
                    self.after(0, tc.prog_lbl.configure, {"text": f"{p}/{total}"})
                return

            pf = ModrinthAPI.get_primary_file(ver)
            if not pf:
                with lock:
                    counters["fail"] += 1
                    counters["processed"] += 1
                    p = counters["processed"]
                    self.after(0, tc.pbar.set, p / total)
                    self.after(0, tc.prog_lbl.configure, {"text": f"{p}/{total}"})
                return

            dest_file = os.path.join(dest_dir, pf["filename"])
            if os.path.exists(dest_file):
                with lock:
                    counters["ok"] += 1
                    counters["skip"] += 1
                    counters["processed"] += 1
                    done_ids.add(pid)
                    p = counters["processed"]
                    self.after(0, tc.pbar.set, p / total)
                    self.after(0, tc.prog_lbl.configure, {"text": f"{p}/{total}"})
                log(f"  ⏭ Already exists: {pf['filename']}")
                return

            if self.api.download_file(pf["url"], dest_file):
                with lock:
                    counters["ok"] += 1
                    counters["processed"] += 1
                    done_ids.add(pid)
                    p = counters["processed"]
                    self.after(0, tc.pbar.set, p / total)
                    self.after(0, tc.prog_lbl.configure, {"text": f"{p}/{total}"})
                log(f"  ✅ Downloaded: {pf['filename']}")
            else:
                with lock:
                    counters["fail"] += 1
                    counters["processed"] += 1
                    p = counters["processed"]
                    self.after(0, tc.pbar.set, p / total)
                    self.after(0, tc.prog_lbl.configure, {"text": f"{p}/{total}"})
                log(f"  ❌ Failed: {title}")
                return

            if tc.project_type == "mod":
                resolved = self.api.resolve_dependencies(ver, log_cb=log)
                for dpid, di in resolved.items():
                    if self.cancel_flag:
                        break
                    with lock:
                        if dpid in done_ids:
                            continue
                        done_ids.add(dpid)
                    dep_path = os.path.join(dest_dir, di["filename"])
                    if os.path.exists(dep_path):
                        continue
                    log(f"    📦 Dependency: {di['title']}")
                    if self.api.download_file(di["url"], dep_path):
                        with lock:
                            counters["deps"] += 1
                    else:
                        log(f"    ❌ Failed dependency: {di['title']}")

        num_workers = min(4, max(1, total))
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
            futures = [executor.submit(process_item, it) for it in items]
            concurrent.futures.wait(futures)

        if self.cancel_flag:
            log(f"\n⛔ Operation cancelled by user. {counters['ok']} items completed.")

        self.after(0, self._download_finished, tc, counters["ok"], counters["fail"], counters["deps"], counters["skip"], total)

    def _download_finished(self, tc, ok, fail, deps, skip, total):
        self.downloading = False
        tc.dl_btn.configure(state="normal")
        tc.cancel_btn.configure(state="disabled")
        tc.pbar.set(1)
        tc.prog_lbl.configure(text="✅ Done")

        summary = f"Downloaded: {ok}/{total} items"
        if deps > 0: summary += f" + {deps} dependencies"
        if skip > 0: summary += f" (Skipped {skip} existing)"
        if fail > 0: summary += f" (Failed {fail})"

        self._log(f"\n🎉 {summary}\n")
        self._st(f"✅ {summary}")
        if fail == 0 and ok > 0:
            sound.play_success()
        else:
            sound.play_error()
        messagebox.showinfo("Download Complete", summary)

    def _start_modpack_install(self, tc, pack_item, dest_dir):
        sound.play_start()
        self.downloading = True
        self.cancel_flag = False
        tc.dl_btn.configure(state="disabled")
        tc.cancel_btn.configure(state="normal")
        tc.pbar.set(0)

        title = pack_item.get("title", "Modpack")
        self._log(f"\n🔧 Installing Modpack: {title} → {dest_dir}")
        threading.Thread(target=self._modpack_worker, args=(tc, pack_item, dest_dir), daemon=True).start()

    def _modpack_worker(self, tc, pack_item, dest_dir):
        def log(msg):
            self.after(0, self._log, msg)

        title = pack_item.get("title", "")
        pid = pack_item.get("project_id", "")
        ver = self.api.get_compatible_version(pid, project_type="modpack")
        if not ver:
            log(f"  ❌ No compatible version found for {title}")
            self.after(0, self._download_finished, tc, 0, 1, 0, 0, 1)
            return

        pf = ModrinthAPI.get_primary_file(ver)
        if not pf or not pf["filename"].endswith(".mrpack"):
            log(f"  ❌ Primary file is not an .mrpack: {pf.get('filename') if pf else 'None'}")
            self.after(0, self._download_finished, tc, 0, 1, 0, 0, 1)
            return

        log(f"  📥 Downloading .mrpack archive: {pf['filename']}...")
        mrpack_data = self.api.download_bytes(pf["url"])
        if not mrpack_data:
            log("  ❌ Failed to download .mrpack file.")
            self.after(0, self._download_finished, tc, 0, 1, 0, 0, 1)
            return

        log("  📦 Extracting mods, configs, and client-overrides...")
        ok, res_msg = self.api.install_mrpack(
            mrpack_data, dest_dir, log_cb=log, is_cancelled=lambda: self.cancel_flag
        )
        if ok:
            log(f"\n🎉 {title} installation complete! {res_msg}")
            self.after(0, self._download_finished, tc, 1, 0, 0, 0, 1)
        else:
            log(f"\n❌ Installation error: {res_msg}")
            self.after(0, self._download_finished, tc, 0, 1, 0, 0, 1)

    # ─── JSON Export & Import ────────────────────────────────────────────────
    def _export_json(self, tc):
        if not tc.selected_slugs:
            messagebox.showinfo("Export", "No items currently selected to export.")
            return
        fp = filedialog.asksaveasfilename(title="Export Selected Items", defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if not fp:
            return
        items = [self.db.get_item(s, project_type=tc.project_type) for s in tc.selected_slugs if self.db.get_item(s, project_type=tc.project_type)]
        data = {
            "type": tc.project_type,
            "game_version": self.ver_entry.get().strip(),
            "count": len(items),
            "exported_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "items": [{"slug": m.get("slug"), "title": m.get("title"), "id": m.get("project_id")} for m in items]
        }
        with open(fp, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        self._st(f"💾 Exported {len(items)} items to {os.path.basename(fp)}")
        self._log(f"💾 Exported list: {fp}")

    def _import_json(self, tc):
        fp = filedialog.askopenfilename(title="Import Item List", filetypes=[("JSON Files", "*.json")])
        if not fp:
            return
        try:
            with open(fp, "r", encoding="utf-8") as f:
                data = json.load(f)
            slugs = [item.get("slug") for item in data.get("items", []) if item.get("slug")]
            count = 0
            for s in slugs:
                if self.db.get_item(s, project_type=tc.project_type):
                    tc.selected_slugs.add(s)
                    count += 1
            self._render_page(tc)
            self._st(f"📂 Imported and selected {count} items.")
            self._log(f"📂 Imported {count} items from {os.path.basename(fp)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load JSON: {e}")

    # ─── Live Sync & Auto-Recovery ───────────────────────────────────────────
    def _start_online_sync(self):
        if not ModrinthAPI.check_internet():
            messagebox.showerror("Network Error", "No internet connection detected.")
            return
        self.sync_btn.configure(state="disabled")
        self._st("🔄 Checking Modrinth for updates...")
        self._log("\n🔄 Initiating live sync with Modrinth API...")
        threading.Thread(target=self._online_sync_worker, daemon=True).start()

    def _online_sync_worker(self):
        try:
            from core import sync_catalog
            sync_catalog.sync_all(gv=self.current_gv, callback=self._sync_progress_cb)
            self.after(0, self._sync_done, True, "Catalog successfully updated!")
        except Exception as e:
            self.after(0, self._sync_done, False, str(e))

    def _sync_progress_cb(self, ptype, page, max_pages, type_sub, total):
        self.after(0, self._st, f"🔄 Syncing {ptype} (MC {self.current_gv}): Page {page}/{max_pages} ({total:,} items)")

    def _sync_done(self, success, msg):
        self.sync_btn.configure(state="normal")
        if success:
            self._log("✅ Live sync completed.")
            self._st("✅ Sync complete. Reloading catalog...")
            self._load_all_tabs()
            messagebox.showinfo("Sync Complete", f"All items for Fabric {self.current_gv} have been restored into local storage!")
        else:
            self._log(f"❌ Sync failed: {msg}")
            self._st(f"❌ Error: {msg}")
            messagebox.showerror("Sync Failed", msg)

    def _background_check_updates(self):
        time.sleep(2)
        total_in_db = self.db.get_count("mod", version=self.current_gv)
        if total_in_db < 6000:
            self.after(0, self._log, f"ℹ Background check: Restoring missing mods for MC {self.current_gv} from Modrinth...")
            try:
                from core import sync_catalog
                sync_catalog.sync_all(gv=self.current_gv)
                self.after(0, self._load_all_tabs)
            except:
                pass


if __name__ == "__main__":
    app = ModrinthApp()
    app.mainloop()
