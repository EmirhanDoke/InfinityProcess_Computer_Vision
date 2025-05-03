import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk

class ImageButtonApp:
    def __init__(self, frame, text):
        
        self.frame = frame
        self.text = text
        # Görüntüyü yükle
        self.load_image(r"tkinter_components\info.png")  # Bu dosyanın yolunu uygun şekilde güncelle
        # Resimli butonu oluştur
        self.create_image_button()

    def load_image(self, path):
        """Buton için resmi yükler."""
        try:
            image = Image.open(path)
            image = image.resize((24, 24))  # Boyutu isteğe göre ayarlayabilirsin
            self.button_image = ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Görüntü yükleme hatası: {e}")
            self.button_image = None

    def create_image_button(self):
        """Resimli butonu oluşturur."""
        self.button = tk.Button(
            self.frame,
            image=self.button_image,
            command=self.open_top_layer
        )
        self.button.grid(row=0, column=1, padx=2, pady=2)

    def open_top_layer(self):
        """Yeni bir üst pencere (top-level) açar."""
        top = Toplevel(self.frame)
        top.title("Info Window")
        tk.Label(top, text=self.text, font=("Arial", 12, "bold")).pack(padx=20, pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageButtonApp(root)
    root.mainloop()
