import tkinter as tk
from tkinter import ttk
from process_manager import ADD_ComboBox
from tkinter_components.tkinter_menu_bar import menu_bar

# Ana uygulama sınıfı
class Application:
    
    counter = 1
    column = 0
    
    def __init__(self, root):
        self.root = root
        self.root.title("Quick Setup for Computer Vision")
        self.root.geometry("800x600")
        
        self.process_frame_data = []
        
        self.menu_bar = menu_bar(self.root)
        
        
        self.buttom_frame = tk.Frame(self.root, bg="lightblue")
        self.buttom_frame.pack(side = "top", fill=tk.X, ipadx=20, ipady=20)
        
        # GUI bileşenlerini oluştur
        self.button = tk.Button(self.buttom_frame, text="Create New Process", bg = "yellow", fg = "black", command = self.create_frames, font = ("Helvetica", 14, "bold"))
        self.button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        self.button = tk.Button(self.buttom_frame, text="Load Image", bg = "orange", fg = "black", command= ADD_ComboBox.file_path_selecter, font = ("Helvetica", 14, "bold"))
        self.button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10, pady=10)
   
        # "Uygula" butonunu ekliyoruz
        self.apply_button = tk.Button(self.buttom_frame, text="Apply", bg="green", fg="white", command=self.apply_all_processes, font = ("Helvetica", 14, "bold"))
        self.apply_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10, pady=10)
   
   
        #? Process Frame Area
   
        # Canvas
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
   
        self.canvas.configure(yscrollcommand=scrollbar.set)
   
        self.process_frame = tk.Frame(self.canvas, borderwidth=2, relief="solid")
        self.canvas.create_window((0, 0), window=self.process_frame, anchor="nw")
        self.process_frame.bind("<Configure>", self.on_frame_configure)
    
    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
       
    def create_frames(self):
        
        row, column = Application.frame_placer()
        
        # Frame oluştur
        self.frame = tk.Frame(self.process_frame, borderwidth=2, relief="solid")
        self.frame.grid(row= row, column= column, padx=5, pady=10)
        
        self.combobox_frame = ADD_ComboBox(self.frame)
        self.process_frame_data.append(self.combobox_frame)
    
    def apply_all_processes(self):
        
        ADD_ComboBox.images[-(len(ADD_ComboBox.images) - 1):] = []
        # print(f"Number of eleman in images list: {len(ADD_ComboBox.images)}")
        for process_box in self.process_frame_data:
            process_box.apply_process()
        
        ADD_ComboBox.show_image()
        
    @classmethod
    def frame_placer(cls):
        
        if cls.counter % 6 == 0:
            cls.column += 1
            cls.counter = 1
        
        cls.counter += 1
        
        return cls.counter, cls.column
