import tkinter as ttk
from tkinter import messagebox
from tkinter import font
import os
import sys
import json
from utils import Utils
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class menu_bar():
    def __init__(self, root):
        
        self.root = root
        self.settings_file = "user_settings.txt"  # Path to the settings file
        self.show_image_flag = ttk.BooleanVar()
        self.language_select = ttk.StringVar()
        self.process_position = ttk.StringVar()
        self.infinity_one_line = ttk.BooleanVar()
        self.theme_select = ttk.StringVar()
        self.load_user_settings()
        
        
        menu_line = ttk.Menu(self.root)
        
        # Settings Menu
        settings_menu = ttk.Menu(menu_line, tearoff=0)
        settings_menu.add_command(label="Settings", command=self.open_settings_window)
        
        menu_line.add_cascade(label="Settings", menu=settings_menu)
        
        restart_menu = ttk.Menu(menu_line, tearoff=0)
        restart_menu.add_command(label="Are you sure for restart?", command=self.restart_app)
        menu_line.add_cascade(label="Restart", menu=restart_menu)
        
        tools_menu = ttk.Menu(menu_line, tearoff=0)
        tools_menu.add_command(label="Tool 1")
        menu_line.add_cascade(label="Tools", menu=tools_menu)
        
        # Info Menu
        about_menu = ttk.Menu(menu_line, tearoff=0)
        about_menu.add_command(label="About")
        # Add the "About" menu to the main menu
        menu_line.add_cascade(label="About", menu=about_menu)

        root.config(menu=menu_line)
        
    def open_settings_window(self):
        settings_win = ttk.Toplevel(self.root)
        settings_win.title("Settings")
        settings_win.geometry("600x400")
        settings_win.resizable(False, False)
        
        upper_frame = ttk.Frame(settings_win)
        upper_frame.pack(side="top", padx=2, pady=2, fill=ttk.X)
        ttk.Label(upper_frame, text="User Settings").pack(side=ttk.LEFT, expand=True, fill=ttk.BOTH, padx=10, pady=10)
        
        #-----------------------
        
        lowwer_frame = ttk.Frame(settings_win, borderwidth=2, relief="solid")
        lowwer_frame.pack(side = "top", padx=2, pady=2, fill=ttk.X)
        
        show_image = ttk.Checkbutton(lowwer_frame, text="Show Load Image Details", variable=self.show_image_flag, bootstyle="round-toggle")
        show_image.grid(row=1, column=0, padx=5, pady=5)
        
        ttk.Label(lowwer_frame, text="Language Select").grid(row=2, column=0, padx=0, pady=5)
        language_select = ttk.Combobox(lowwer_frame, values=["English", "Turkish"], textvariable=self.language_select)
        language_select.grid(row=2, column=1, padx=5, pady=5)
        
        
        themes = ['cosmo', 'flatly', 'litera', 'minty', 'lumen', 'sandstone', 'yeti', 'pulse',
                  'united', 'morph', 'journal', 'darkly', 'superhero', 'solar', 'cyborg', 'vapor', 'simplex', 'cerculean']
        
        ttk.Label(lowwer_frame, text="Theme Select").grid(row=3, column=0, padx=0, pady=5)
        theme_select = ttk.Combobox(lowwer_frame, values=themes, textvariable=self.theme_select)
        theme_select.grid(row=3, column=1, padx=5, pady=5)
        #-----------------------
        
        process_position_frame = ttk.LabelFrame(settings_win, text="Process Position", borderwidth=2, relief="solid")
        process_position_frame.pack(side = "top", padx=2, pady=10, fill=ttk.X)
        
        ttk.Label(process_position_frame, text="Height").grid(row=0, column=0, padx=0, pady=5)
        process_position_entry = ttk.Entry(process_position_frame, textvariable=self.process_position, width=10)
        process_position_entry.grid(row=0, column=1, padx=5, pady=5)
    
        infinity_one_line = ttk.Checkbutton(process_position_frame, text="Infinity One Line", variable=self.infinity_one_line, bootstyle="round-toggle")
        infinity_one_line.grid(row=1, column=0, padx=5, pady=5)
        #-----------------------
        
        save_buttom = ttk.Button(settings_win, text="Save", command=self.save_user_settings)
        save_buttom.pack(side=ttk.BOTTOM, padx=5, pady=5)
        
    def restart_app(self):
        # Restart the application
        python = sys.executable
        os.execl(python, python, *sys.argv)
        
        # Move to the top of the screen
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.attributes('-topmost', False)
        
    def save_user_settings(self):
        
        path = Utils.resource_path(Utils.settings_file)
        
        # Checkbutton durumunu bir dict olarak kaydet
        settings = {
            "show_image_flag": self.show_image_flag.get(),
            "language": self.language_select.get(),
            "process_position": self.process_position.get(),
            "infinity_one_line": self.infinity_one_line.get(),
            "theme": self.theme_select.get()
        }
        with open(path, "w") as file:
            json.dump(settings, file, indent=4)
    
    def load_user_settings(self):
        
        path = Utils.resource_path(Utils.settings_file)
        
        # Ayarları dosyadan yükle
        if os.path.exists(path):
            with open(path, "r") as file:
                settings = json.load(file)
                self.show_image_flag.set(settings.get("show_image_flag", True))
                self.language_select.set(settings.get("language", "English"))
                self.process_position.set(settings.get("process_position", "5"))
                self.infinity_one_line.set(settings.get("infinity_one_line", False))
                self.theme_select.set(settings.get("theme", "litera"))