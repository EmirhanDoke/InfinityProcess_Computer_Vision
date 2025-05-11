import tkinter as ttk
from process_manager import ADD_ComboBox
from tkinter_components.tkinter_menu_bar import menu_bar
from utils import Utils
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Ana uygulama sınıfı
class Application:
    
    counter = 0
    column = 0
    
    def __init__(self, root):
        self.root = root
        self.root.title("Quick Setup for Computer Vision")
        self.root.geometry("800x600")
        
        self.process_frame_data = []
        
        self.menu_bar = menu_bar(self.root)
        
        self.buttom_frame = ttk.Frame(self.root)
        self.buttom_frame.pack(side = "top", fill=ttk.X, ipadx=20, ipady=20)
        
        # GUI bileşenlerini oluştur
        self.button = ttk.Button(self.buttom_frame, text="Create New Process", command = self.create_frames)
        self.button.pack(side=ttk.LEFT, expand=True, fill=ttk.BOTH, padx=10, pady=10)
        
        self.button = ttk.Button(self.buttom_frame, text="Load Image", command= ADD_ComboBox.file_path_selecter)
        self.button.pack(side=ttk.LEFT, expand=True, fill=ttk.BOTH, padx=10, pady=10)
   
        # "Uygula" butonunu ekliyoruz
        self.apply_button = ttk.Button(self.buttom_frame, text="Apply", command=self.apply_all_processes)
        self.apply_button.pack(side=ttk.LEFT, expand=True, fill=ttk.BOTH, padx=10, pady=10)
   
   
        #? Process Frame Area
   
        # Canvas
        self.canvas = ttk.Canvas(self.root)
        self.canvas.pack(side=ttk.LEFT, fill=ttk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side=ttk.RIGHT, fill=ttk.Y)
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
   
        self.canvas.configure(yscrollcommand=scrollbar.set)
   
        self.process_frame = ttk.Frame(self.canvas, borderwidth=2, relief="solid")
        self.canvas.create_window((0, 0), window=self.process_frame, anchor="nw")
        self.process_frame.bind("<Configure>", self.on_frame_configure)
    
    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
       
    def create_frames(self):
        
        row, column = Application.frame_placer()
        
        # Frame oluştur
        self.frame = ttk.Frame(self.process_frame, borderwidth=2, relief="solid")
        self.frame.grid(row= row, column= column, padx=5, pady=10)
        
        self.combobox_frame = ADD_ComboBox(self.frame)
        self.process_frame_data.append(self.combobox_frame)
    
    def apply_all_processes(self):
        
        process_names = ["Original Image"]
        
        ADD_ComboBox.images[-(len(ADD_ComboBox.images) - 1):] = []
        # print(f"Number of eleman in images list: {len(ADD_ComboBox.images)}")
        for process_box in self.process_frame_data:
            if process_box.processor is None and process_box.processor_np is None and process_box.processor_both is None:  # if OFF process is selected, skip it
                continue
            process_box.apply_process()
            if process_box.processor and hasattr(process_box.processor, 'name'):
                process_names.append(process_box.processor.name)
            
            elif process_box.processor_both and hasattr(process_box.processor_both, 'name'):
                process_names.append(process_box.processor_both.name)
            
            else:
                process_names.append("Nameless")

        ADD_ComboBox.show_image(names = process_names)
        
    @classmethod
    def frame_placer(cls):
        
        process_position = Utils.load_user_settings("process_position")
        infinity_one_line = Utils.load_user_settings("infinity_one_line")
        
        if process_position:
            Height = int(process_position[0])
        else:
            Height = 5
            print("No height value found in settings, using default value of 5.")

        if infinity_one_line == False:
            if cls.counter % (Height + 1) == 0:
                cls.column += 1
                cls.counter = 1
            
            cls.counter += 1
        
        else:
            cls.counter += 1
        
        return cls.counter, cls.column
