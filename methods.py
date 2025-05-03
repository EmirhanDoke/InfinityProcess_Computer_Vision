import tkinter as tk
from tkinter import ttk
import cv2

class ProcessFrameBase:
    def apply(self, img):
        raise NotImplementedError("apply method must be implemented in subclass.")

class ThresholdingFrame(ProcessFrameBase):
    
    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()

        
    def create_widgets(self):
        tk.Label(self.frame, text="Threshold:").grid(row=1, column=0, padx=2, pady=2)
        self.threshold_entry = tk.Entry(self.frame)
        self.threshold_entry.grid(row=1, column=1, padx=2, pady=2) 

        tk.Label(self.frame, text="Threshold Type:").grid(row=2, column=0, padx=2, pady=2)
        threshold_types = ["Binary", "Binary_Inverse"]
        self.threshold_type_combobox = ttk.Combobox(self.frame, values=threshold_types, width=17)
        self.threshold_type_combobox.grid(row=2, column=1, padx=2, pady=2)
     
    def apply(self, img):
        threshold_value = self.threshold_entry.get()
        threshold_type = self.threshold_type_combobox.get()
        # Functions
        
        if threshold_type == "Binary":
            threshold_type = cv2.THRESH_BINARY
            ret, img = cv2.threshold(img, int(threshold_value), 255, threshold_type)
        
        elif threshold_type == "Binary_Inverse":
            threshold_type = cv2.THRESH_BINARY_INV
            ret, img = cv2.threshold(img, int(threshold_value), 255, threshold_type)
    
        # ADD_ComboBox.images.append(img)
        return img
    
        # cv2.imshow("Original Image",ADD_ComboBox.images[-2])
        # cv2.imshow("Thresholding Image",ADD_ComboBox.images[-1])
        # print(len(ADD_ComboBox.images))
        
        # for imge in range(len(ADD_ComboBox.images)):
        #     cv2.imshow(f"Image{imge}",ADD_ComboBox.images[imge])
        
        # return img
        
class GaborFilterFrame(ProcessFrameBase):
    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.frame, text="Ksize:").grid(row=1, column=0, padx=2, pady=2)
        tk.Entry(self.frame).grid(row=1, column=1, padx=2, pady=2)

        tk.Label(self.frame, text="Sigma:").grid(row=2, column=0, padx=2, pady=2)
        tk.Entry(self.frame).grid(row=2, column=1, padx=2, pady=2)

        tk.Label(self.frame, text="Theta:").grid(row=3, column=0, padx=2, pady=2)
        tk.Entry(self.frame).grid(row=3, column=1, padx=2, pady=2)

        tk.Label(self.frame, text="Lambda:").grid(row=4, column=0, padx=2, pady=2)
        tk.Entry(self.frame).grid(row=4, column=1, padx=2, pady=2)

        tk.Label(self.frame, text="Gamma:").grid(row=5, column=0, padx=2, pady=2)
        tk.Entry(self.frame).grid(row=5, column=1, padx=2, pady=2)

        tk.Label(self.frame, text="Phi:").grid(row=6, column=0, padx=2, pady=2)
        tk.Entry(self.frame).grid(row=6, column=1, padx=2, pady=2)

class MorphologicalFrame(ProcessFrameBase):
    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.frame, text="Kernel Size:").grid(row=1, column=0, padx=2, pady=2)
        self.kernelsize = tk.Entry(self.frame)
        self.kernelsize.grid(row=1, column=1, padx=2, pady=2)

        tk.Label(self.frame, text="Kernel Shape:").grid(row=2, column=0, padx=2, pady=2)
        shapes = ["Rectangular", "Ellipse", "Cross"]
        self.shapes_combobox = ttk.Combobox(self.frame, values=shapes, width=17)
        self.shapes_combobox.grid(row=2, column=1, padx=2, pady=2)

        tk.Label(self.frame, text="Operations:").grid(row=3, column=0, padx=2, pady=2)
        operations = ["Erode", "Dilation", "Opening", "Closing"]
        self.operations_combobox = ttk.Combobox(self.frame, values=operations, width=17)
        self.operations_combobox.grid(row=3, column=1, padx=2, pady=2)

        tk.Label(self.frame, text="Iterations:").grid(row=4, column=0, padx=2, pady=2)
        self.iterations = tk.Entry(self.frame)
        self.iterations.grid(row=4, column=1, padx=2, pady=2)

    def apply(self, img):
        kernel_shape = self.shapes_combobox.get()
        operations = self.operations_combobox.get()
        kernel_size = int(self.kernelsize.get())
        iterations_value = int(self.iterations.get())
        
        
        if kernel_shape == "Rectangular":
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size,kernel_size))
        
        elif kernel_shape == "Ellipse":
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size,kernel_size))
    
        elif kernel_shape == "Cross":
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size,kernel_size))
    
        if operations == "Erode":
            img = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel, iterations = iterations_value) 
        
        elif operations == "Diletion":
            img = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel, iterations = iterations_value)

        elif operations == "Opening":
            img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations = iterations_value)
    
        elif operations == "Closing":
            img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations = iterations_value)
    
        # ADD_ComboBox.images.append(img)
        return img

class GammaTransformFrame(ProcessFrameBase):
    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()
    
    def create_widgets(self):
        
        tk.Label(self.frame, text="Gamma Value:").grid(row=1, column=0, padx=2, pady=2)
        self.gamma_transform_var = tk.StringVar()
        tk.Entry(self.frame, textvariable= self.gamma_transform_var).grid(row=1, column=1, padx=2, pady=2)

    