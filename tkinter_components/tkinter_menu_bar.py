import tkinter as tk
from tkinter import messagebox
from tkinter import font

class menu_bar():
    def __init__(self, root):
        
        self.root = root
        

        menu_cubugu = tk.Menu(self.root)
        
        # Settings Menu
        settings_menu = tk.Menu(menu_cubugu, tearoff=0)
        settings_menu.add_command(label="Settings", command=self.open_settings_window)
        
        # Ana menüye "Settings" menüsünü ekle
        menu_cubugu.add_cascade(label="Settings", menu=settings_menu, font = ("Ariel", 12))
        
        
        # Info Menu
        info_menu = tk.Menu(menu_cubugu, tearoff=0)
        info_menu.add_command(label="Info")
        
        # Ana menüye "Info" menüsünü ekle
        menu_cubugu.add_cascade(label="Info", menu=info_menu, font = ("Ariel", 12))
        

        root.config(menu=menu_cubugu)
        
    def open_settings_window(self):
        settings_win = tk.Toplevel(self.root)
        settings_win.title("Settings")
        settings_win.geometry("400x300")
        
        tk.Label(settings_win, text="Ayarlar Penceresi", font=("Arial", 14)).pack(pady=20)
        # Buraya diğer ayar bileşenlerini ekleyebilirsin