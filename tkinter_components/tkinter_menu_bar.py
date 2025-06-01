# Copyright 2025 Said Emirhan Döke
# Licensed under the Apache License, Version 2.0

import tkinter as ttk
from tkinter import messagebox
from tkinter import font
import os
import sys
import json
from utils import Utils
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import importlib
from tkinter_components.tkinter_info_buttom import *

class menu_bar():
    def __init__(self, root, folder, subfolder):
        
        self.root = root
        self.settings_file = "user_settings.txt"  # Path to the settings file
        self.folder = folder
        self.subfolder = subfolder
        self.language = Utils.load_user_settings("language")
        self.translations = self.load_translations()
        self.show_image_flag = ttk.BooleanVar()
        self.check_image_settings = ttk.BooleanVar()
        self.language_select = ttk.StringVar()
        self.process_position = ttk.StringVar()
        self.infinity_one_line = ttk.BooleanVar()
        self.theme_select = ttk.StringVar()
        self.select_folder_type = ttk.StringVar()
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
        tools_menu.add_command(label="Prepare Dataset", command=self.open_dataset_window)
        menu_line.add_cascade(label="Tools", menu=tools_menu)
        
        # Info Menu
        about_menu = ttk.Menu(menu_line, tearoff=0)
        about_menu.add_command(label="About", command=self.about_window)
        # Add the "About" menu to the main menu
        menu_line.add_cascade(label="About", menu=about_menu)

        root.config(menu=menu_line)
        
    def open_settings_window(self):
        settings_win = ttk.Toplevel(self.root)
        settings_win.title(self.get_translation("Settings_Title"))
        settings_win.geometry("600x400")
        settings_win.resizable(False, False)
        
        upper_frame = ttk.Frame(settings_win)
        upper_frame.pack(side="top", padx=2, pady=2, fill=ttk.X)
        ttk.Label(upper_frame, text=self.get_translation("User_Settings")).pack(side=ttk.LEFT, expand=True, fill=ttk.BOTH, padx=10, pady=10)
        
        self.warning_label = ttk.Label(settings_win, text=self.get_translation("Warning_Label"), foreground="red", font=font.Font(size=12))
        self.warning_label.pack(side="top")
        
        #-----------------------
        
        lowwer_frame = ttk.Frame(settings_win, borderwidth=2, relief="solid")
        lowwer_frame.pack(side = "top", padx=2, pady=2, fill=ttk.X)
        
        show_image = ttk.Checkbutton(lowwer_frame, text=self.get_translation("Show_Load_Image_Details_Settings"), variable=self.show_image_flag, bootstyle="round-toggle")
        show_image.grid(row=1, column=0, padx=5, pady=5)
        
        check_image = ttk.Checkbutton(lowwer_frame, text=self.get_translation("Check_Image_Settings"), variable=self.check_image_settings, bootstyle="round-toggle")
        check_image.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(lowwer_frame, text=self.get_translation("Language_Select_Settings")).grid(row=2, column=0, padx=0, pady=5)
        language_select = ttk.Combobox(lowwer_frame, values=["English", "Turkish"], textvariable=self.language_select)
        language_select.grid(row=2, column=1, padx=5, pady=5)
        
        
        themes = ['cosmo', 'flatly', 'litera', 'minty', 'lumen', 'sandstone', 'yeti', 'pulse',
                  'united', 'morph', 'journal', 'darkly', 'superhero', 'solar', 'cyborg', 'vapor', 'simplex', 'cerculean']
        
        ttk.Label(lowwer_frame, text=self.get_translation("Theme_Select_Settings")).grid(row=3, column=0, padx=0, pady=5)
        theme_select = ttk.Combobox(lowwer_frame, values=themes, textvariable=self.theme_select)
        theme_select.grid(row=3, column=1, padx=5, pady=5)
        
        #-----------------------
        
        process_position_frame = ttk.LabelFrame(settings_win, text=self.get_translation("Process_Position_Settings"), borderwidth=2, relief="solid")
        process_position_frame.pack(side = "top", padx=2, pady=10, fill=ttk.X)
        
        ttk.Label(process_position_frame, text=self.get_translation("Height_Settings")).grid(row=0, column=0, padx=0, pady=5)
        process_position_entry = ttk.Entry(process_position_frame, textvariable=self.process_position, width=10)
        process_position_entry.grid(row=0, column=1, padx=5, pady=5)
    
        infinity_one_line = ttk.Checkbutton(process_position_frame, text=self.get_translation("Infinity_One_Lines_Settings"), variable=self.infinity_one_line, bootstyle="round-toggle")
        infinity_one_line.grid(row=1, column=0, padx=5, pady=5)
        #-----------------------
        
        save_buttom = ttk.Button(settings_win, text=self.get_translation("Save_Button_Settings"), command=self.save_user_settings)
        save_buttom.pack(side=ttk.LEFT, padx=5, pady=5)
        
    def open_dataset_window(self):
        dataset_win = ttk.Toplevel(self.root)
        dataset_win.title(self.get_translation("Dataset_Process_Settings_Title"))
        dataset_win.geometry("600x500")
        dataset_win.resizable(False, False)
        
        pd_upper_frame = ttk.Frame(dataset_win)
        pd_upper_frame.pack(side="top", padx=2, pady=2, fill=ttk.X)
        
        ttk.Label(pd_upper_frame, text=self.get_translation("Dataset_Process_Settings")).grid(row=0, column=0, padx=10, pady=10)
        ImageButtonApp(pd_upper_frame, text=self.get_translation("DatasetProcessInfo"), row=0, col=1)
        
        self.warning_label = ttk.Label(dataset_win, text=self.get_translation("Dataset_Process_Settings_Warning_Label"), foreground="red", font=font.Font(size=12))
        self.warning_label.pack(side="top")
        
        #-----------------------
        
        lowwer_frame = ttk.Frame(dataset_win, borderwidth=2, relief="solid")
        lowwer_frame.pack(side = "top", padx=2, pady=2, fill=ttk.X)
        
        ttk.Label(lowwer_frame, text=self.get_translation("Select_Folder_Layout_Settings")).grid(row=1, column=0, padx=5, pady=5)
        select_folder_type_combobox = ttk.Combobox(lowwer_frame, values=["Single Folder", "Subfolder"], textvariable=self.select_folder_type)
        select_folder_type_combobox.grid(row=1, column=1, padx=5, pady=5)
        
        single_folder_type_str = """
        📁 image_folder
        ├── 1.png
        └── 2.png
        """
        
        subfolder_type_str = """
        📁image_folder/
        ├── subfolder1/
        │   ├── 1.png
        │   └── 2.png
        └── subfolder2/
            └── 1.png
            """
        
        ttk.Label(lowwer_frame, text="Single Folder Type", justify="left").grid(row=2, column=0, padx=5, pady=5)
        ttk.Label(lowwer_frame, text=single_folder_type_str, justify="left").grid(row=3, column=0, padx=5, pady=5)
        
        ttk.Label(lowwer_frame, text="Subfolder Type", justify="left").grid(row=2, column=1, padx=5, pady=5)
        ttk.Label(lowwer_frame, text=subfolder_type_str, justify="left").grid(row=3, column=1, padx=5, pady=5)
        ttk.Label(lowwer_frame, text=self.get_translation("Select_Folder_Layout_Settings_Warning_Label"), foreground="red", font=font.Font(size=12)).grid(row=4, column=0, padx=5, pady=5, columnspan=2)
        
        #-----------------------
        
        bottom_frame = ttk.Frame(dataset_win)
        bottom_frame.pack(side = "bottom", padx=2, pady=2, fill=ttk.X)
        
        save_buttom = ttk.Button(bottom_frame, text=self.get_translation("Save_Button_Settings"), command=self.save_user_settings)
        save_buttom.pack(side=ttk.LEFT, padx=5, pady=5)
        
        apply_buttom = ttk.Button(bottom_frame, text=self.get_translation("Process_Dataset_Button"), command=self.apply_dataset_action)
        apply_buttom.pack(side=ttk.LEFT, padx=5, pady=5)
        
    def about_window(self):
        about_win = ttk.Toplevel(self.root)
        about_win.title("About")
        about_win.geometry("500x200")
        
        about_text = """
        
        Developer: Said Emirhan Döke
        Version: 1.1.3b
        Github: https://github.com/EmirhanDoke
        
        """
        
        about_label = ttk.Label(about_win, text= about_text, font=font.Font(size=12))
        about_label.pack(side="top")

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
        
        settings = {
            "show_image_flag": self.show_image_flag.get(),
            "language": self.language_select.get(),
            "process_position": self.process_position.get(),
            "infinity_one_line": self.infinity_one_line.get(),
            "theme": self.theme_select.get(),
            "folder_type": self.select_folder_type.get(),
            "check_image_settings": self.check_image_settings.get()
        }
        with open(path, "w") as file:
            json.dump(settings, file, indent=4)
        
        messagebox.showinfo(self.get_translation("Save_Button_MessageBox_Title"), self.get_translation("Save_Button_MessageBox_Text"))
    
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
                self.select_folder_type.set(settings.get("folder_type", "Single Folder"))
                self.check_image_settings.set(settings.get("check_image_settings", True))

    def apply_dataset_action(self):
        folder_type = Utils.load_user_settings("folder_type")
        if folder_type == "Single Folder":
            self.folder() # batch_apply_processes callback
        elif folder_type == "Subfolder":
            self.subfolder() # batch_apply_processes_alt callback
        else:
            messagebox.showwarning(self.get_translation("Folder_Type_MessageBox_Title"), self.get_translation("Folder_Type_MessageBox_Text"))

    def load_translations(self):
        # Load translations based on the selected language
        try:
            lang_module = importlib.import_module(f"languages.{self.language.lower()}")
            return lang_module.translations
        except ModuleNotFoundError:
            print(f"Translation file for language '{self.language}' not found.")
            return {}

    def get_translation(self, key):
        # Get the translation for the given key
        return self.translations.get(key, "Translation not available.")