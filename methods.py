import tkinter as tk
from tkinter import ttk
import cv2
import numpy as np

class ProcessFrameBase:
    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()
    
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
        
        if threshold_type == "Binary":
            threshold_type = cv2.THRESH_BINARY
            ret, img = cv2.threshold(img, int(threshold_value), 255, threshold_type)
        
        elif threshold_type == "Binary_Inverse":
            threshold_type = cv2.THRESH_BINARY_INV
            ret, img = cv2.threshold(img, int(threshold_value), 255, threshold_type)
    
        return img
          
class GaborFilterFrame(ProcessFrameBase):
    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.frame, text="Ksize:").grid(row=1, column=0, padx=2, pady=2)
        self.ksize_entry = tk.Entry(self.frame)
        self.ksize_entry.grid(row=1, column=1, padx=2, pady=2)

        tk.Label(self.frame, text="Sigma:").grid(row=2, column=0, padx=2, pady=2)
        self.sigma_entry = tk.Entry(self.frame)
        self.sigma_entry.grid(row=2, column=1, padx=2, pady=2)

        tk.Label(self.frame, text="Theta:").grid(row=3, column=0, padx=2, pady=2)
        self.theta_entry = tk.Entry(self.frame)
        self.theta_entry.grid(row=3, column=1, padx=2, pady=2)
        
        tk.Label(self.frame, text="Lambda:").grid(row=4, column=0, padx=2, pady=2)
        self.lambda_frame = tk.Entry(self.frame)
        self.lambda_frame.grid(row=4, column=1, padx=2, pady=2)

        tk.Label(self.frame, text="Gamma:").grid(row=5, column=0, padx=2, pady=2)
        self.gamma_entry = tk.Entry(self.frame)
        self.gamma_entry.grid(row=5, column=1, padx=2, pady=2)
        
        tk.Label(self.frame, text="Phi:").grid(row=6, column=0, padx=2, pady=2)
        self.phi_entry = tk.Entry(self.frame)
        self.phi_entry.grid(row=6, column=1, padx=2, pady=2)

    def apply(self, img):
        
        ksize = int(self.ksize_entry.get())
        sigma = int(self.sigma_entry.get())
        theta = int(self.theta_entry.get())
        lamda = int(self.lambda_frame.get())
        gamma = int(self.gamma_entry.get())
        phi = int(self.phi_entry.get())
                
        ht_kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lamda, gamma, phi, ktype=cv2.CV_32F)
        img = cv2.filter2D(img, cv2.CV_8UC3, ht_kernel)
        return img

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
        
        match kernel_shape:
            case "Rectangular":
                kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size,kernel_size))
        
            case "Ellipse":
                kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size,kernel_size))
    
            case "Cross":
                kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size,kernel_size))
    
        match operations:
            case "Erode":
                img = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel, iterations = iterations_value) 
        
            case  "Diletion":
                img = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel, iterations = iterations_value)

            case "Opening":
                img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations = iterations_value)
    
            case "Closing":
                img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations = iterations_value)
    
        return img

#! Maybe Not working
class GammaTransformFrame(ProcessFrameBase):
    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()
    
    def create_widgets(self):
        
        tk.Label(self.frame, text="Gamma Value:").grid(row=1, column=0, padx=2, pady=2)
        self.gamma_transform_entry = tk.Entry(self.frame)
        self.gamma_transform_entry.grid(row=1, column=1, padx=2, pady=2)

    def apply(self, img):
        gamma_transform_entry = int(self.gamma_transform_entry.get())

        # Normalize the image to the range [0, 1]
        normalized_image = img / 255.0
        
        # Apply gamma transform
        gamma_corrected = np.power(normalized_image, gamma_transform_entry)
        
        # Convert back to range [0, 255] and convert to uint8
        gamma_corrected = np.uint8(gamma_corrected * 255)
        
        return img
    
class CannyEdgeDetectorFrame(ProcessFrameBase):
    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()
        
    def create_widgets(self):
        
        tk.Label(self.frame, text="Kernel Size:").grid(row=1, column=0, padx=2, pady=2)
        self.ksize_entry = tk.Entry(self.frame)
        self.ksize_entry.grid(row=1, column=1, padx=2, pady=2)
        
        tk.Label(self.frame, text="Low Threshold:").grid(row=2, column=0, padx=2, pady=2)
        self.low_threshold_entry = tk.Entry(self.frame)
        self.low_threshold_entry.grid(row=2, column=1, padx=2, pady=2)
        
        tk.Label(self.frame, text="Max Threshold:").grid(row=3, column=0, padx=2, pady=2)
        self.max_threshold_entry = tk.Entry(self.frame)
        self.max_threshold_entry.grid(row=3, column=1, padx=2, pady=2)
        
        tk.Label(self.frame, text="L2gradient:").grid(row=4, column=0, padx=2, pady=2)
        shape = ["True", "False"]
        self.l2gradient_combobox = ttk.Combobox(self.frame, values=shape, width=17)
        self.l2gradient_combobox .grid(row=4, column=1, padx=2, pady=2)
    
    def apply(self, img):
        
        ksize = int(self.ksize_entry.get())
        low_threshold = int(self.low_threshold_entry.get())
        max_threshold = int(self.max_threshold_entry.get())
        l2gradient = bool(self.l2gradient_combobox.get())
        
        detected_edges = cv2.Canny(img, low_threshold, max_threshold, ksize, L2gradient= l2gradient)
    
        mask = detected_edges != 0
        img = img[:,:,None]
        dst = img * (mask[:,:,None].astype(img.dtype))
        
        img = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
        
        return img

class HoughTransformFrame(ProcessFrameBase):
        
    def create_widgets(self):
        
        tk.Label(self.frame, text="Dp:").grid(row=1, column=0, padx=2, pady=2)
        self.dp_entry = tk.Entry(self.frame)
        self.dp_entry.grid(row=1, column=1, padx=2, pady=2)
        
        tk.Label(self.frame, text="Minimum Distance:").grid(row=2, column=0, padx=2, pady=2)
        self.minimum_distance_entry = tk.Entry(self.frame)
        self.minimum_distance_entry.grid(row=2, column=1, padx=2, pady=2)
        
        tk.Label(self.frame, text="Param1:").grid(row=3, column=0, padx=2, pady=2)
        self.param1_entry = tk.Entry(self.frame)
        self.param1_entry.grid(row=3, column=1, padx=2, pady=2)
        
        tk.Label(self.frame, text="Param2:").grid(row=4, column=0, padx=2, pady=2)
        self.param2_entry = tk.Entry(self.frame)
        self.param2_entry.grid(row=4, column=1, padx=2, pady=2)
        
        tk.Label(self.frame, text="Minimum Radius:").grid(row=5, column=0, padx=2, pady=2)
        self.minimum_radius_entry = tk.Entry(self.frame)
        self.minimum_radius_entry.grid(row=5, column=1, padx=2, pady=2)
        
        tk.Label(self.frame, text="Maximum Radius:").grid(row=6, column=0, padx=2, pady=2)
        self.maximum_radius_entry = tk.Entry(self.frame)
        self.maximum_radius_entry.grid(row=6, column=1, padx=2, pady=2)
        
        tk.Label(self.frame, text="Mark Color:").grid(row=7, column=0, padx=2, pady=2)
        ope2 = ["Red", "Blue"]
        self.mark_color_combobox = ttk.Combobox(self.frame, values=ope2, width=17)
        self.mark_color_combobox.grid(row=7, column=1, padx=2, pady=2)
    
    def apply(self, img):
        
        dp = int(self.dp_entry.get())
        minimum_distance = int(self.minimum_distance_entry.get())
        param1 = int(self.param1_entry.get())
        param2 = int(self.param2_entry.get())
        minimum_radius = int(self.minimum_radius_entry.get())
        maximum_radius = int(self.maximum_radius_entry.get())
        mark_color = str(self.mark_color_combobox.get())
        copy_img = img.copy()
        
        
        if mark_color == "Red":
            mark_color1 = 0
            mark_color2 = 0
            mark_color3 = 255
        
        elif mark_color == "Blue":
            mark_color1 = 255
            mark_color2 = 0
            mark_color3 = 0
        
        circles = cv2.HoughCircles(
        img, 
        cv2.HOUGH_GRADIENT, dp = dp, minDist = minimum_distance, param1 = param1, param2 = param2, minRadius = minimum_radius, maxRadius = maximum_radius 
    )
    
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for circle in circles[0, :]:
                center = (circle[0], circle[1])
                radius = circle[2]
                cv2.circle(copy_img, center, radius, (mark_color1, mark_color2, mark_color3), 2)
        
        return copy_img
        
    
    
    