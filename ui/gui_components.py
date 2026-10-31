"""
GUI Modals & Dialog Components for Modrinth Mod Manager
Includes:
- ItemDetailModal (Full Description, Direct Download, Modrinth Link - Comments removed)
- WelcomeModal (Splash / Intro Screen with Language Selector)
- TutorialModal (5-step interactive feature tour)
- PatchNotesModal (v1.1 Release & Complete Beta History)
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from ui.translations import i18n
from ui.themes import THEMES

# ═══════════════════════════════════════════════════════════════════════════════
# Item Detail Modal (Comments removed as requested)
# ═══════════════════════════════════════════════════════════════════════════════
class ItemDetailModal(ctk.CTkToplevel):
    def __init__(self, parent, item_data, theme, on_download=None):
        super().__init__(parent)
        self.item = item_data
        self.theme = theme
        self.on_download = on_download
        
        slug = item_data.get("slug", "item")
        title = item_data.get("title", slug)
        self.title(f"{title} - {i18n.t('modal_details_title')}")
        self.geometry("820x620")
        self.minsize(720, 500)
        self.configure(fg_color=self.theme["bg"])
        
        self.lift()
        self.focus_force()
        self.grab_set()

        self._build_ui()

    def _build_ui(self):
        # Header banner
        hdr = ctk.CTkFrame(self, fg_color=self.theme["surface"], corner_radius=12, border_width=1, border_color=self.theme["border"])
        hdr.pack(fill="x", padx=16, pady=(16, 10))

        top_row = ctk.CTkFrame(hdr, fg_color="transparent")
        top_row.pack(fill="x", padx=16, pady=(14, 6))

        ptype = self.item.get("project_type", "mod").upper()
        type_color = {
            "MOD": self.theme["accent"],
            "RESOURCEPACK": self.theme["purple"],
            "DATAPACK": self.theme["orange"],
            "SHADER": self.theme["blue"],
            "MODPACK": "#ff7b72"
        }.get(ptype, self.theme["accent"])

        ctk.CTkLabel(
            top_row, text=f" {ptype} ", font=("Segoe UI", 11, "bold"),
            fg_color=type_color, text_color="#000000" if self.theme["name"] == "Solar Light" else "#ffffff",
            corner_radius=6
        ).pack(side="left", padx=(0, 10))

        title_text = self.item.get("title", self.item.get("slug", ""))
        ctk.CTkLabel(
            top_row, text=title_text, font=("Segoe UI", 18, "bold"),
            text_color=self.theme["txt"], anchor="w"
        ).pack(side="left", fill="x", expand=True)

        meta_row = ctk.CTkFrame(hdr, fg_color="transparent")
        meta_row.pack(fill="x", padx=16, pady=(0, 14))

        author = self.item.get("author", "Unknown")
        dls = self.item.get("downloads", 0)
        cat_key = self.item.get("primary_category", "utility")
        cat_display = i18n.t_cat(cat_key)

        ctk.CTkLabel(meta_row, text=f"👤 {author}", font=("Segoe UI", 11), text_color=self.theme["txt2"]).pack(side="left", padx=(0, 16))
        ctk.CTkLabel(meta_row, text=f"⬇ {dls:,} downloads", font=("Segoe UI", 11), text_color=self.theme["txt2"]).pack(side="left", padx=(0, 16))
        ctk.CTkLabel(meta_row, text=f"🏷 {cat_display}", font=("Segoe UI", 11, "bold"), text_color=self.theme["accent_tx"]).pack(side="left")

        # Content Box
        body_frame = ctk.CTkFrame(self, fg_color=self.theme["card"], corner_radius=10, border_width=1, border_color=self.theme["border"])
        body_frame.pack(fill="both", expand=True, padx=16, pady=4)

        box = ctk.CTkTextbox(
            body_frame, fg_color=self.theme["card"], text_color=self.theme["txt"],
            font=("Segoe UI", 12), corner_radius=8, wrap="word"
        )
        box.pack(fill="both", expand=True, padx=12, pady=12)

        desc = self.item.get("description", "No description provided.")
        date_mod = self.item.get("date_modified", "—")
        client = self.item.get("client_side", "optional")
        server = self.item.get("server_side", "optional")

        content = (
            f"{desc}\n\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"{i18n.t('modal_tech_specs').upper()}:\n"
            f"• Slug: {self.item.get('slug', '—')}\n"
            f"• Project ID: {self.item.get('project_id', '—')}\n"
            f"• Category: {cat_display}\n"
            f"• Client Support: {client}\n"
            f"• Server Support: {server}\n"
            f"• Last Updated: {date_mod}\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"Ready for instant 1-click installation to your target directory."
        )
        box.insert("1.0", content)
        box.configure(state="disabled")

        # Footer actions
        ftr = ctk.CTkFrame(self, fg_color=self.theme["surface"], corner_radius=0, height=54)
        ftr.pack(fill="x", side="bottom")
        ftr.pack_propagate(False)

        inn_ftr = ctk.CTkFrame(ftr, fg_color="transparent")
        inn_ftr.pack(fill="x", padx=16, pady=10)

        if self.on_download:
            ctk.CTkButton(
                inn_ftr, text=f"⬇ {i18n.t('modal_btn_download')}", font=("Segoe UI", 12, "bold"),
                fg_color=self.theme["accent"], hover_color=self.theme["accent_h"],
                text_color="#000000" if self.theme["name"] == "Solar Light" else "#ffffff",
                width=190, height=34, corner_radius=8,
                command=self._do_download
            ).pack(side="left", padx=(0, 10))

        ctk.CTkButton(
            inn_ftr, text=f"🌐 {i18n.t('modal_btn_web')}", font=("Segoe UI", 11),
            fg_color=self.theme["elevated"], hover_color=self.theme["hover"], text_color=self.theme["txt"],
            width=160, height=34, corner_radius=8,
            command=self._open_web
        ).pack(side="left", padx=(0, 10))

        ctk.CTkButton(
            inn_ftr, text="✖ Close", font=("Segoe UI", 11),
            fg_color=self.theme["elevated"], hover_color=self.theme["hover"], text_color=self.theme["txt3"],
            width=90, height=34, corner_radius=8,
            command=self.destroy
        ).pack(side="right")

    def _open_web(self):
        slug = self.item.get("slug", "")
        ptype = self.item.get("project_type", "mod")
        url = f"https://modrinth.com/{ptype}/{slug}"
        webbrowser.open(url)

    def _do_download(self):
        self.destroy()
        if self.on_download:
            self.on_download(self.item)


# ═══════════════════════════════════════════════════════════════════════════════
# Welcome Modal (Splash / Intro Screen)
# ═══════════════════════════════════════════════════════════════════════════════
class WelcomeModal(ctk.CTkToplevel):
    def __init__(self, parent, theme, on_start=None, on_open_tutorial=None, is_online=True):
        super().__init__(parent)
        self.theme = theme
        self.on_start = on_start
        self.on_open_tutorial = on_open_tutorial
        
        self.title(i18n.t("welcome_title"))
        self.geometry("640x510")
        self.resizable(False, False)
        self.configure(fg_color=self.theme["bg"])

        self.lift()
        self.focus_force()
        self.grab_set()

        self._build_ui(is_online)

    def _build_ui(self, is_online):
        body = ctk.CTkFrame(self, fg_color=self.theme["surface"], corner_radius=14, border_width=1, border_color=self.theme["border"])
        body.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(body, text="⛏", font=("Segoe UI", 48)).pack(pady=(18, 0))
        ctk.CTkLabel(body, text=i18n.t("welcome_title"), font=("Segoe UI", 16, "bold"), text_color=self.theme["accent"]).pack(pady=(4, 4))
        ctk.CTkLabel(body, text=i18n.t("app_subtitle"), font=("Segoe UI", 11), text_color=self.theme["txt2"]).pack(pady=(0, 10))

        desc_box = ctk.CTkFrame(body, fg_color=self.theme["card"], corner_radius=10)
        desc_box.pack(fill="x", padx=24, pady=6)
        ctk.CTkLabel(
            desc_box, text=i18n.t("welcome_desc"), font=("Segoe UI", 10),
            text_color=self.theme["txt"], wraplength=520, justify="center"
        ).pack(padx=16, pady=10)

        status_text = i18n.t("welcome_net_online") if is_online else i18n.t("welcome_net_offline")
        status_color = self.theme["accent_tx"] if is_online else self.theme["orange"]
        ctk.CTkLabel(body, text=status_text, font=("Segoe UI", 10, "bold"), text_color=status_color).pack(pady=6)

        f_grid = ctk.CTkFrame(body, fg_color="transparent")
        f_grid.pack(pady=8)

        features = [
            ("⚙ 9,000+ Fabric Mods", "🎨 6,500+ Resource Packs"),
            ("✨ 1,075+ Shaders", "📊 2,850+ Data Packs"),
            ("📦 760+ Modpacks (.mrpack)", "⚡ High-Speed SQLite Caching")
        ]
        for left, right in features:
            row = ctk.CTkFrame(f_grid, fg_color="transparent")
            row.pack(fill="x", pady=2)
            ctk.CTkLabel(row, text=f"• {left}", font=("Segoe UI", 10), text_color=self.theme["txt2"], width=190, anchor="w").pack(side="left")
            ctk.CTkLabel(row, text=f"• {right}", font=("Segoe UI", 10), text_color=self.theme["txt2"], width=190, anchor="w").pack(side="left")

        btn_row = ctk.CTkFrame(body, fg_color="transparent")
        btn_row.pack(pady=(16, 12))

        ctk.CTkButton(
            btn_row, text=i18n.t("welcome_btn_start"), font=("Segoe UI", 12, "bold"),
            fg_color=self.theme["accent"], hover_color=self.theme["accent_h"],
            text_color="#000000" if self.theme["name"] == "Solar Light" else "#ffffff",
            width=170, height=38, corner_radius=8,
            command=self._start
        ).pack(side="left", padx=8)

        ctk.CTkButton(
            btn_row, text=i18n.t("welcome_btn_guide"), font=("Segoe UI", 11),
            fg_color=self.theme["elevated"], hover_color=self.theme["hover"], text_color=self.theme["txt"],
            width=160, height=38, corner_radius=8,
            command=self._guide
        ).pack(side="left", padx=8)

    def _start(self):
        self.destroy()
        if self.on_start:
            self.on_start()

    def _guide(self):
        self.destroy()
        if self.on_open_tutorial:
            self.on_open_tutorial()


# ═══════════════════════════════════════════════════════════════════════════════
# Tutorial Modal (Öğretici)
# ═══════════════════════════════════════════════════════════════════════════════
class TutorialModal(ctk.CTkToplevel):
    def __init__(self, parent, theme):
        super().__init__(parent)
        self.theme = theme
        self.title(i18n.t("tutorial_title"))
        self.geometry("740x620")
        self.minsize(680, 500)
        self.configure(fg_color=self.theme["bg"])

        self.lift()
        self.focus_force()
        self.grab_set()

        self._build_ui()

    def _build_ui(self):
        hdr = ctk.CTkFrame(self, fg_color=self.theme["surface"], corner_radius=0, height=54)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)
        ctk.CTkLabel(hdr, text=f"❓ {i18n.t('tutorial_title')}", font=("Segoe UI", 16, "bold"), text_color=self.theme["accent"]).pack(side="left", padx=20)

        scroll = ctk.CTkScrollableFrame(self, fg_color=self.theme["bg"])
        scroll.pack(fill="both", expand=True, padx=16, pady=12)

        steps = [
            ("tut_step1_title", "tut_step1_desc", "📂"),
            ("tut_step2_title", "tut_step2_desc", "🖱"),
            ("tut_step3_title", "tut_step3_desc", "☑"),
            ("tut_step4_title", "tut_step4_desc", "🎯"),
            ("tut_step5_title", "tut_step5_desc", "🎨"),
        ]

        for title_key, desc_key, icon in steps:
            card = ctk.CTkFrame(scroll, fg_color=self.theme["card"], corner_radius=10, border_width=1, border_color=self.theme["border"])
            card.pack(fill="x", pady=6)

            top = ctk.CTkFrame(card, fg_color="transparent")
            top.pack(fill="x", padx=14, pady=(10, 4))
            ctk.CTkLabel(top, text=f"{icon}  {i18n.t(title_key)}", font=("Segoe UI", 13, "bold"), text_color=self.theme["txt"]).pack(side="left")

            ctk.CTkLabel(
                card, text=i18n.t(desc_key), font=("Segoe UI", 11),
                text_color=self.theme["txt2"], wraplength=640, justify="left", anchor="w"
            ).pack(fill="x", padx=14, pady=(0, 12))

        ctk.CTkButton(
            self, text="Got It! Close Guide", font=("Segoe UI", 11, "bold"),
            fg_color=self.theme["accent"], hover_color=self.theme["accent_h"],
            text_color="#000000" if self.theme["name"] == "Solar Light" else "#ffffff",
            width=160, height=36, corner_radius=8,
            command=self.destroy
        ).pack(pady=12)


# ═══════════════════════════════════════════════════════════════════════════════
# Patch Notes Modal (Yama Notları v1.1 & Beta Dönemi)
# ═══════════════════════════════════════════════════════════════════════════════
class PatchNotesModal(ctk.CTkToplevel):
    def __init__(self, parent, theme):
        super().__init__(parent)
        self.theme = theme
        self.title(i18n.t("patch_notes_title"))
        self.geometry("820x680")
        self.minsize(720, 520)
        self.configure(fg_color=self.theme["bg"])

        self.lift()
        self.focus_force()
        self.grab_set()

        self._build_ui()

    def _build_ui(self):
        hdr = ctk.CTkFrame(self, fg_color=self.theme["surface"], corner_radius=0, height=54)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)
        ctk.CTkLabel(hdr, text=i18n.t("patch_notes_title"), font=("Segoe UI", 15, "bold"), text_color=self.theme["accent"]).pack(side="left", padx=20)

        body_frame = ctk.CTkFrame(self, fg_color=self.theme["card"], corner_radius=10, border_width=1, border_color=self.theme["border"])
        body_frame.pack(fill="both", expand=True, padx=16, pady=12)

        box = ctk.CTkTextbox(
            body_frame, fg_color=self.theme["card"], text_color=self.theme["txt"],
            font=("Segoe UI", 11), corner_radius=8, wrap="word"
        )
        box.pack(fill="both", expand=True, padx=10, pady=10)

        notes_text = i18n.get_patch_notes()
        box.insert("1.0", notes_text)
        box.configure(state="disabled")

        ctk.CTkButton(
            self, text="Close", font=("Segoe UI", 11),
            fg_color=self.theme["elevated"], hover_color=self.theme["hover"], text_color=self.theme["txt"],
            width=120, height=34, corner_radius=8,
            command=self.destroy
        ).pack(pady=(0, 12))
