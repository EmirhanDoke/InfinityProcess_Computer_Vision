# Copyright 2025 Said Emirhan Döke
# Licensed under the Apache License, Version 2.0

from tkinter import Toplevel
from PIL import Image, ImageTk
import sys
import os
from utils import Utils
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ImageButtonApp:
    def __init__(self, frame, text, row=0, col=1):
        
        self.frame = frame
        self.text = text
        self.row = row
        self.col = col
        # Görüntüyü yükle
        self.load_image(r"tkinter_components\info.png")  # Bu dosyanın yolunu uygun şekilde güncelle
        # Resimli butonu oluştur
        self.create_image_button()

    def load_image(self, path):
        """Buton için resmi yükler."""
        try:
            
            path = ImageButtonApp.resource_path("tkinter_components\info.png")
            
            image = Image.open(path)
            image = image.resize((24, 24))  # Boyutu isteğe göre ayarlayabilirsin
            self.button_image = ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Görüntü yükleme hatası: {e}")
            self.button_image = None

    def create_image_button(self):
        """Resimli butonu oluşturur."""
        self.button = ttk.Button(
            self.frame,
            image=self.button_image,
            command=self.open_top_layer,
            bootstyle="default-outline",
            text= " Info",
            compound="left"
        )
        self.button.grid(row=self.row, column=self.col, padx=2, pady=2)

    def open_top_layer(self):
        """Yeni bir üst pencere (top-level) açar."""
        top = Toplevel(self.frame)
        top.title("Info Window")
        
        ttk.Label(top, text=self.text, font=("Arial", 12, "bold"), wraplength=750, justify="left").pack(padx=20, pady=20)
    
    @classmethod
    def resource_path(cls, relative_path):
        try:
            base_path = sys._MEIPASS  # pyinstaller'ın geçici klasörü
        except Exception:
            base_path = os.path.abspath(".")  # normal çalışma
        return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    root = ttk.ttk()
    app = ImageButtonApp(root)
    root.mainloop()
