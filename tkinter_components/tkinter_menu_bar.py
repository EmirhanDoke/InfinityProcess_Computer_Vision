import tkinter as tk
from tkinter import messagebox
from tkinter import font
import os
import sys
import json
from tkinter import ttk
from utils import Utils

class menu_bar():
    def __init__(self, root):
        
        self.root = root
        self.settings_file = "user_settings.txt"  # Path to the settings file
        self.show_image_flag = tk.BooleanVar()
        self.language_select = tk.StringVar()
        self.process_position = tk.StringVar()
        self.infinity_one_line = tk.BooleanVar()
        self.load_user_settings()
        
        
        menu_line = tk.Menu(self.root)
        
        # Settings Menu
        settings_menu = tk.Menu(menu_line, tearoff=0)
        settings_menu.add_command(label="Settings", command=self.open_settings_window)
        
        menu_line.add_cascade(label="Settings", menu=settings_menu, font = ("Ariel", 12))
        
        restart_menu = tk.Menu(menu_line, tearoff=0)
        restart_menu.add_command(label="Are you sure for restart?", command=self.restart_app)
        menu_line.add_cascade(label="Restart", menu=restart_menu, font = ("Ariel", 12))
        
        tools_menu = tk.Menu(menu_line, tearoff=0)
        tools_menu.add_command(label="Tool 1")
        menu_line.add_cascade(label="Tools", menu=tools_menu, font = ("Ariel", 12))
        
        # Info Menu
        about_menu = tk.Menu(menu_line, tearoff=0)
        about_menu.add_command(label="About")
        # Add the "About" menu to the main menu
        menu_line.add_cascade(label="About", menu=about_menu, font = ("Ariel", 12))

        root.config(menu=menu_line)
        
    def open_settings_window(self):
        settings_win = tk.Toplevel(self.root)
        settings_win.title("Settings")
        settings_win.geometry("600x400")
        settings_win.resizable(False, False)
        
        upper_frame = tk.Frame(settings_win, bg="lightblue")
        upper_frame.pack(side="top", padx=2, pady=2, fill=tk.X)
        tk.Label(upper_frame, text="User Settings", font=("Arial", 12), bg="lightblue").pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        #-----------------------
        
        lowwer_frame = tk.Frame(settings_win, borderwidth=2, relief="solid")
        lowwer_frame.pack(side = "top", padx=2, pady=2, fill=tk.X)
        
        show_image = tk.Checkbutton(lowwer_frame, text="Show Load Image Details", font=("Arial", 10), variable=self.show_image_flag)
        show_image.grid(row=1, column=0, padx=5, pady=5)
        
        language_select = ttk.Combobox(lowwer_frame, values=["English", "Turkish"], font=("Arial", 10), textvariable=self.language_select)
        language_select.grid(row=2, column=0, padx=5, pady=5)
        
        #-----------------------
        
        process_position_frame = tk.LabelFrame(settings_win, text="Process Position", font=("Arial", 9), borderwidth=2, relief="solid")
        process_position_frame.pack(side = "top", padx=2, pady=10, fill=tk.X)
        
        tk.Label(process_position_frame, text="Height", font=("Arial", 10)).grid(row=0, column=0, padx=0, pady=5)
        process_position_entry = tk.Entry(process_position_frame, font=("Arial", 10), textvariable=self.process_position, width=10)
        process_position_entry.grid(row=0, column=1, padx=5, pady=5)
    
        infinity_one_line = tk.Checkbutton(process_position_frame, text="Infinity One Line", font=("Arial", 10), variable=self.infinity_one_line)
        infinity_one_line.grid(row=1, column=0, padx=5, pady=5)
        #-----------------------
        
        save_buttom = tk.Button(settings_win, text="Save", font=("Arial", 14), command=self.save_user_settings)
        save_buttom.pack(side=tk.BOTTOM, padx=5, pady=5)
        
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
            "infinity_one_line": self.infinity_one_line.get()
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