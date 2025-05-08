import tkinter as tk
from tkinter import messagebox
from tkinter import font
import os
import sys

class menu_bar():
    def __init__(self, root):
        
        self.root = root
        

        menu_cubugu = tk.Menu(self.root)
        
        # Settings Menu
        settings_menu = tk.Menu(menu_cubugu, tearoff=0)
        settings_menu.add_command(label="Settings", command=self.open_settings_window)
        # Ana menüye "Settings" menüsünü ekle
        menu_cubugu.add_cascade(label="Settings", menu=settings_menu, font = ("Ariel", 12))
        
        restart_menu = tk.Menu(menu_cubugu, tearoff=0)
        restart_menu.add_command(label="Are you sure for restart?", command=self.restart_app)
        menu_cubugu.add_cascade(label="Restart", menu=restart_menu, font = ("Ariel", 12))
        
        tools_menu = tk.Menu(menu_cubugu, tearoff=0)
        tools_menu.add_command(label="Tool 1")
        menu_cubugu.add_cascade(label="Tools", menu=tools_menu, font = ("Ariel", 12))
        
        # Info Menu
        About_menu = tk.Menu(menu_cubugu, tearoff=0)
        About_menu.add_command(label="About")
        # Ana menüye "About" menüsünü ekle
        menu_cubugu.add_cascade(label="About", menu=About_menu, font = ("Ariel", 12))
        

        root.config(menu=menu_cubugu)
        
    def open_settings_window(self):
        settings_win = tk.Toplevel(self.root)
        settings_win.title("Settings")
        settings_win.geometry("400x300")
        
        tk.Label(settings_win, text="Ayarlar Penceresi", font=("Arial", 14)).pack(pady=20)
        
    
    def restart_app(self):
        # Restart the application
        python = sys.executable
        os.execl(python, python, *sys.argv)
        
        # Move to the top of the screen
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.attributes('-topmost', False)