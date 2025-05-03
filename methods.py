import tkinter as tk
from tkinter import ttk
import cv2
import numpy as np
import matplotlib.pyplot as plt

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
        operations = ["Erode", "Dilation", "Opening", "Closing", "Gradient", "Top Hat", "Black Hat",]
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
    
            case "Gradient":
                img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel, iterations = iterations_value)
    
            case "Top Hat":
                img = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel, iterations = iterations_value)
    
            case "Black Hat":
                img =  cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel, iterations = iterations_value)
                
        return img

#! May be Not working
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
        
class GaussianBlurFrame(ProcessFrameBase):
        
    def create_widgets(self):
        
        tk.Label(self.frame, text="Kernel Size:").grid(row=1, column=0, padx=2, pady=2)
        self.ksize_entry = tk.Entry(self.frame)
        self.ksize_entry.grid(row=1, column=1, padx=2, pady=2)
        
        tk.Label(self.frame, text="Sigma_X:").grid(row=2, column=0, padx=2, pady=2)
        self.sigmax_entry = tk.Entry(self.frame)
        self.sigmax_entry.grid(row=2, column=1, padx=2, pady=2)
        
        tk.Label(self.frame, text="Sigma_Y:").grid(row=3, column=0, padx=2, pady=2)
        self.sigmay_entry = tk.Entry(self.frame)
        self.sigmay_entry.grid(row=3, column=1, padx=2, pady=2)
    
    def apply(self, img):
        
        ksize = int(self.ksize_entry.get())
        sigmax = float(self.sigmax_entry.get())
        sigmay = float(self.sigmay_entry.get())
        
        img = cv2.GaussianBlur(img, (ksize, ksize), sigmax, sigmay)
    
        return img

class KitterIllingworthFrame(ProcessFrameBase):
    
    def create_widgets(self):
        
        tk.Label(self.frame, text="Optimum Threshold:").grid(row=1, column=0, padx=2, pady=2)
        self.optimum_threshold_label = tk.Label(self.frame)
        self.optimum_threshold_label.grid(row=1, column=1, padx=2, pady=2)
        
    def apply(self, img):
        
        # Görüntünün histogramını hesapla
        hist = cv2.calcHist([img], [0], None, [256], [0,256])
        hist_norm = hist.ravel()/hist.sum()
        thresholds = np.array(range(256))

        # Eşik değerleri için Kittler-Illingworth hesaplama
        def calculate_cost(t):
            background = hist_norm[:t]
            foreground = hist_norm[t:]
            background_mean = np.sum(thresholds[:t]*background)
            foreground_mean = np.sum(thresholds[t:]*foreground)
            background_variance = np.sum(((thresholds[:t] - background_mean) ** 2) * background)
            foreground_variance = np.sum(((thresholds[t:] - foreground_mean) ** 2) * foreground)
            cost = background_variance * np.log(background_variance if background_variance > 0 else 1) + \
                foreground_variance * np.log(foreground_variance if foreground_variance > 0 else 1)
            return cost

        costs = [calculate_cost(t) for t in range(1, 256)]
        optimal_threshold = np.argmin(costs) + 1
        print(optimal_threshold)
        return optimal_threshold
    
    def update_result(self, img):
        threshold = self.apply(img)
        self.optimum_threshold_label.config(text=str(threshold))

class DrawHistogramFrame(ProcessFrameBase):
    
    def create_widgets(self):
        pass
    
    def apply(self, img):
        
        histogram, bins = np.histogram(img.flatten(), bins=256, range=[0,256])
    
        return histogram, bins
    
    def update_result(self, img):
        
        histogram, bins = self.apply(img)
        
        plt.figure(figsize=(10,6))
        plt.plot(bins[:-1], histogram, color='black')
        plt.title('Image Histogram')
        plt.xlabel('Pixel Intensity')
        plt.ylabel('Frequency')
        plt.show()

class ColorConvertFrame(ProcessFrameBase):

    def create_widgets(self):
        tk.Label(self.frame, text="Select Color Conversion:").grid(row=1, column=0, padx=2, pady=2)
        
        # Combobox for color conversion type
        self.color_convert_combobox = ttk.Combobox(self.frame, values=["RGB to Grayscale", "Grayscale to RGB", "RGB to HSV", "HSV to RGB"])
        self.color_convert_combobox.grid(row=1, column=1, padx=2, pady=2)
        self.color_convert_combobox.set("RGB to Grayscale")

    def apply(self, img):
        conversion_type = self.color_convert_combobox.get()

        match conversion_type:
            case "RGB to Grayscale":
                # Convert image from RGB to Grayscale
                converted_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            case "Grayscale to RGB":
                # Convert image from Grayscale to RGB
                converted_image = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            case "RGB to HSV":
                # Convert image from RGB to HSV
                converted_image = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
            case "HSV to RGB":
                # Convert image from HSV to RGB
                converted_image = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
            case _:
                # Default case if no match
                converted_image = img

        return converted_image

class ResizeFrame(ProcessFrameBase):

    def create_widgets(self):
        tk.Label(self.frame, text="Width:").grid(row=1, column=0, padx=2, pady=2)
        self.width_entry = tk.Entry(self.frame)
        self.width_entry.grid(row=1, column=1, padx=2, pady=2)
        
        tk.Label(self.frame, text="Height:").grid(row=2, column=0, padx=2, pady=2)
        self.height_entry = tk.Entry(self.frame)
        self.height_entry.grid(row=2, column=1, padx=2, pady=2)

    def apply(self, img):
        width = int(self.width_entry.get())
        height = int(self.height_entry.get())

        # Resize the image
        resized_image = cv2.resize(img, (width, height))

        return resized_image

class RotateFrame(ProcessFrameBase):

    def create_widgets(self):
        tk.Label(self.frame, text="Select Rotation Angle:").grid(row=1, column=0, padx=2, pady=2)
        
        # Combobox for rotation angles
        self.rotation_combobox = ttk.Combobox(self.frame, values=["90", "180", "270"])
        self.rotation_combobox.grid(row=1, column=1, padx=2, pady=2)
        self.rotation_combobox.set("90")

    def apply(self, img):
        rotation_angle = int(self.rotation_combobox.get())

        match rotation_angle:
            case 90:
                rotated_image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            case 180:
                rotated_image = cv2.rotate(img, cv2.ROTATE_180)
            case 270:
                rotated_image = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            case _:
                rotated_image = img

        return rotated_image

class FlipFrame(ProcessFrameBase):

    def create_widgets(self):
        tk.Label(self.frame, text="Select Flip Direction:").grid(row=1, column=0, padx=2, pady=2)
        
        # Combobox for flip directions
        self.flip_combobox = ttk.Combobox(self.frame, values=["Horizontal", "Vertical", "Both"])
        self.flip_combobox.grid(row=1, column=1, padx=2, pady=2)
        self.flip_combobox.set("Horizontal")

    def apply(self, img):
        flip_direction = self.flip_combobox.get()

        match flip_direction:
            case "Horizontal":
                flipped_image = cv2.flip(img, 1)  # Flip horizontally
            case "Vertical":
                flipped_image = cv2.flip(img, 0)  # Flip vertically
            case "Both":
                flipped_image = cv2.flip(img, -1)  # Flip both horizontally and vertically
            case _:
                flipped_image = img

        return flipped_image
    
class MedianBlurFrame(ProcessFrameBase):

    def create_widgets(self):
        tk.Label(self.frame, text="Kernel Size:").grid(row=1, column=0, padx=2, pady=2)
        self.kernel_size_entry = tk.Entry(self.frame)
        self.kernel_size_entry.grid(row=1, column=1, padx=2, pady=2)

    def apply(self, img):
        kernel_size = int(self.kernel_size_entry.get())

        # Apply Median Blur
        blurred_image = cv2.medianBlur(img, kernel_size)

        return blurred_image

#! May be not working
class BilateralFilterFrame(ProcessFrameBase):

    def create_widgets(self):
        tk.Label(self.frame, text="Diameter:").grid(row=1, column=0, padx=2, pady=2)
        self.d_entry = tk.Entry(self.frame)
        self.d_entry.grid(row=1, column=1, padx=2, pady=2)

        tk.Label(self.frame, text="Sigma Color:").grid(row=2, column=0, padx=2, pady=2)
        self.sigma_color_entry = tk.Entry(self.frame)
        self.sigma_color_entry.grid(row=2, column=1, padx=2, pady=2)

        tk.Label(self.frame, text="Sigma Space:").grid(row=3, column=0, padx=2, pady=2)
        self.sigma_space_entry = tk.Entry(self.frame)
        self.sigma_space_entry.grid(row=3, column=1, padx=2, pady=2)

    def apply(self, img):
        d = int(self.d_entry.get())
        sigma_color = float(self.sigma_color_entry.get())
        sigma_space = float(self.sigma_space_entry.get())

        # Apply Bilateral Filter
        filtered_image = cv2.bilateralFilter(img, d, sigma_color, sigma_space)

        return filtered_image

class Filter2DFrame(ProcessFrameBase):

    def create_widgets(self):
        tk.Label(self.frame, text="3x3 Kernel Values (row-wise):").grid(row=1, column=0, columnspan=2, padx=2, pady=2)

        inner_frame = tk.Frame(self.frame)
        inner_frame.grid(row=2, column=0)
        
        # 3x3 Entry grid for kernel values
        self.kernel_entries = []
        for i in range(3):
            row_entries = []
            for j in range(3):
                entry = tk.Entry(inner_frame, width=5)
                entry.grid(row=i+2, column=j, padx=1, pady=1)
                entry.insert(0, "0")
                row_entries.append(entry)
            self.kernel_entries.append(row_entries)

    def apply(self, img):
        # Read kernel values from Entry widgets and convert to float
        kernel = []
        for row in self.kernel_entries:
            row_values = [float(entry.get()) for entry in row]
            kernel.append(row_values)
        kernel = np.array(kernel, dtype=np.float32)

        # Apply filter2D
        filtered_image = cv2.filter2D(img, -1, kernel)

        return filtered_image

class SobelFrame(ProcessFrameBase):

    def create_widgets(self):
        # dx selecting
        tk.Label(self.frame, text="dx:").grid(row=1, column=0, padx=2, pady=2)
        self.dx_combobox = ttk.Combobox(self.frame, values=[0, 1])
        self.dx_combobox.grid(row=1, column=1, padx=2, pady=2)

        # dy selecting
        tk.Label(self.frame, text="dy:").grid(row=2, column=0, padx=2, pady=2)
        self.dy_combobox = ttk.Combobox(self.frame, values=[0, 1])
        self.dy_combobox.grid(row=2, column=1, padx=2, pady=2)

        # Ksize
        tk.Label(self.frame, text="Kernel Size (odd, e.g. 1, 3, 5):").grid(row=3, column=0, padx=2, pady=2)
        self.ksize_entry = tk.Entry(self.frame)
        self.ksize_entry.grid(row=3, column=1, padx=2, pady=2)

    def apply(self, img):
        dx = int(self.dx_combobox.get())
        dy = int(self.dy_combobox.get())
        ksize = int(self.ksize_entry.get())

        # Apply
        sobel_image = cv2.Sobel(img, cv2.CV_64F, dx, dy, ksize=ksize)

        # Normalize image and convert to uint8
        sobel_image = cv2.convertScaleAbs(sobel_image)

        return sobel_image

class ScharrFrame(ProcessFrameBase):

    def create_widgets(self):
        # dx selecting
        tk.Label(self.frame, text="dx:").grid(row=1, column=0, padx=2, pady=2)
        self.dx_combobox = ttk.Combobox(self.frame, values=[0, 1])
        self.dx_combobox.grid(row=1, column=1, padx=2, pady=2)

        # dy selecting
        tk.Label(self.frame, text="dy:").grid(row=2, column=0, padx=2, pady=2)
        self.dy_combobox = ttk.Combobox(self.frame, values=[0, 1])
        self.dy_combobox.grid(row=2, column=1, padx=2, pady=2)

    def apply(self, img):
        dx = int(self.dx_combobox.get())
        dy = int(self.dy_combobox.get())

        # Apply
        scharr_image = cv2.Scharr(img, cv2.CV_64F, dx, dy)

        # Normalize image and convert to uint8
        scharr_image = cv2.convertScaleAbs(scharr_image)

        return scharr_image

class LaplacianFrame(ProcessFrameBase):

    def create_widgets(self):
        # Entry for kernel size (must be odd and positive)
        tk.Label(self.frame, text="Kernel Size (e.g., 1, 3, 5):").grid(row=1, column=0, padx=2, pady=2)
        self.ksize_entry = tk.Entry(self.frame)
        self.ksize_entry.grid(row=1, column=1, padx=2, pady=2)

    def apply(self, img):
        ksize = int(self.ksize_entry.get())

        # Apply Laplacian operator using 64-bit float depth
        laplacian_image = cv2.Laplacian(img, cv2.CV_64F, ksize=ksize)

        # Convert the result to 8-bit absolute values for display
        laplacian_image = cv2.convertScaleAbs(laplacian_image)

        return laplacian_image

class CornerHarrisFrame(ProcessFrameBase):

    def create_widgets(self):
        # Entry for block size (neighborhood size)
        tk.Label(self.frame, text="Block Size:").grid(row=1, column=0, padx=2, pady=2)
        self.block_size_entry = tk.Entry(self.frame)
        self.block_size_entry.grid(row=1, column=1, padx=2, pady=2)

        # Entry for ksize (aperture parameter of Sobel)
        tk.Label(self.frame, text="Sobel Kernel Size:").grid(row=2, column=0, padx=2, pady=2)
        self.ksize_entry = tk.Entry(self.frame)
        self.ksize_entry.grid(row=2, column=1, padx=2, pady=2)

        # Entry for Harris detector free parameter k
        tk.Label(self.frame, text="Harris k value (e.g., 0.04):").grid(row=3, column=0, padx=2, pady=2)
        self.k_entry = tk.Entry(self.frame)
        self.k_entry.grid(row=3, column=1, padx=2, pady=2)

    def apply(self, img):
        block_size = int(self.block_size_entry.get())
        ksize = int(self.ksize_entry.get())
        k = float(self.k_entry.get())

        # Convert image to grayscale if not already
        if len(img.shape) == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img.copy()

        # Convert grayscale to float32 as required by cornerHarris
        gray = np.float32(gray)

        # Apply Harris corner detection
        dst = cv2.cornerHarris(gray, block_size, ksize, k)

        # Dilate result for marking the corners (visual enhancement)
        dst = cv2.dilate(dst, None)

        # Create a copy of original image for marking corners
        result_img = img.copy()

        # Threshold to mark strong corners in red
        result_img[dst > 0.01 * dst.max()] = [0, 0, 255]

        return result_img

class GoodFeaturesToTrackFrame(ProcessFrameBase):

    def create_widgets(self):
        # Entry for maxCorners (maximum number of corners to return)
        tk.Label(self.frame, text="Max Corners:").grid(row=1, column=0, padx=2, pady=2)
        self.max_corners_entry = tk.Entry(self.frame)
        self.max_corners_entry.grid(row=1, column=1, padx=2, pady=2)

        # Entry for qualityLevel (minimum accepted quality of corners)
        tk.Label(self.frame, text="Quality Level (0 to 1):").grid(row=2, column=0, padx=2, pady=2)
        self.quality_level_entry = tk.Entry(self.frame)
        self.quality_level_entry.grid(row=2, column=1, padx=2, pady=2)

        # Entry for minDistance (minimum possible Euclidean distance between corners)
        tk.Label(self.frame, text="Min Distance:").grid(row=3, column=0, padx=2, pady=2)
        self.min_distance_entry = tk.Entry(self.frame)
        self.min_distance_entry.grid(row=3, column=1, padx=2, pady=2)

    def apply(self, img):
        max_corners = int(self.max_corners_entry.get())
        quality_level = float(self.quality_level_entry.get())
        min_distance = float(self.min_distance_entry.get())

        # Convert to grayscale if needed
        if len(img.shape) == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img.copy()

        # Detect good features to track
        corners = cv2.goodFeaturesToTrack(gray, max_corners, quality_level, min_distance)

        # Copy image to draw results
        result_img = img.copy()

        # Draw detected corners
        if corners is not None:
            for corner in corners:
                x, y = corner.ravel()
                cv2.circle(result_img, (int(x), int(y)), 4, (0, 255, 0), -1)

        return result_img

class AdaptiveThresholdFrame(ProcessFrameBase):

    def create_widgets(self):
        # Entry for max value (maximum intensity value to be assigned to pixels)
        tk.Label(self.frame, text="Max Value:").grid(row=1, column=0, padx=2, pady=2)
        self.max_value_entry = tk.Entry(self.frame)
        self.max_value_entry.grid(row=1, column=1, padx=2, pady=2)

        # Combobox for adaptive method (Mean or Gaussian)
        tk.Label(self.frame, text="Adaptive Method:").grid(row=2, column=0, padx=2, pady=2)
        self.adaptive_method_combobox = ttk.Combobox(self.frame, values=['Mean', 'Gaussian'])
        self.adaptive_method_combobox.grid(row=2, column=1, padx=2, pady=2)

        # Combobox for threshold type (Binary or Binary Inverted)
        tk.Label(self.frame, text="Threshold Type:").grid(row=3, column=0, padx=2, pady=2)
        self.threshold_type_combobox = ttk.Combobox(self.frame, values=['Binary', 'Binary Inverted'])
        self.threshold_type_combobox.grid(row=3, column=1, padx=2, pady=2)

        # Entry for block size (size of local region for thresholding)
        tk.Label(self.frame, text="Block Size (odd > 1):").grid(row=4, column=0, padx=2, pady=2)
        self.block_size_entry = tk.Entry(self.frame)
        self.block_size_entry.grid(row=4, column=1, padx=2, pady=2)

        # Entry for C value (constant to subtract from mean or weighted mean)
        tk.Label(self.frame, text="C (constant):").grid(row=5, column=0, padx=2, pady=2)
        self.c_entry = tk.Entry(self.frame)
        self.c_entry.grid(row=5, column=1, padx=2, pady=2)

    def apply(self, img):
        max_value = int(self.max_value_entry.get())
        adaptive_method = self.adaptive_method_combobox.get()
        threshold_type = self.threshold_type_combobox.get()
        block_size = int(self.block_size_entry.get())
        c = int(self.c_entry.get())

        # Convert to grayscale if needed
        if len(img.shape) == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img.copy()

        # Apply adaptive thresholding
        if adaptive_method == 'Mean':
            adaptive_method_cv = cv2.ADAPTIVE_THRESH_MEAN_C
        else:
            adaptive_method_cv = cv2.ADAPTIVE_THRESH_GAUSSIAN_C

        if threshold_type == 'Binary':
            threshold_type_cv = cv2.THRESH_BINARY
        else:
            threshold_type_cv = cv2.THRESH_BINARY_INV

        # Apply adaptive thresholding with specified parameters
        thresholded_image = cv2.adaptiveThreshold(gray, max_value, adaptive_method_cv,
                                                 threshold_type_cv, block_size, c)

        return thresholded_image

class OtsuThresholdFrame(ProcessFrameBase):

    def create_widgets(self):
        # Entry for max value (maximum intensity value to be assigned to pixels)
        tk.Label(self.frame, text="Max Value:").grid(row=1, column=0, padx=2, pady=2)
        self.max_value_entry = tk.Entry(self.frame)
        self.max_value_entry.grid(row=1, column=1, padx=2, pady=2)

        # Combobox for threshold type (Binary or Binary Inverted)
        tk.Label(self.frame, text="Threshold Type:").grid(row=2, column=0, padx=2, pady=2)
        self.threshold_type_combobox = ttk.Combobox(self.frame, values=['Binary', 'Binary Inverted'])
        self.threshold_type_combobox.grid(row=2, column=1, padx=2, pady=2)

    def apply(self, img):
        max_value = int(self.max_value_entry.get())
        threshold_type = self.threshold_type_combobox.get()

        # Convert to grayscale if needed
        if len(img.shape) == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img.copy()

        # Apply Otsu's thresholding
        if threshold_type == 'Binary':
            threshold_type_cv = cv2.THRESH_BINARY
        else:
            threshold_type_cv = cv2.THRESH_BINARY_INV

        # Apply threshold using Otsu's method
        _, otsu_thresholded_image = cv2.threshold(gray, 0, max_value, threshold_type_cv + cv2.THRESH_OTSU)

        return otsu_thresholded_image
#! Needed update for contours    
class FindContoursFrame(ProcessFrameBase):

    def create_widgets(self):
        # Combobox for contour retrieval mode (e.g., external or all)
        tk.Label(self.frame, text="Retrieval Mode:").grid(row=1, column=0, padx=2, pady=2)
        self.retrieval_mode_combobox = ttk.Combobox(self.frame, values=['RETR_EXTERNAL', 'RETR_LIST', 'RETR_TREE'])
        self.retrieval_mode_combobox.grid(row=1, column=1, padx=2, pady=2)

        # Combobox for contour approximation method (e.g., simple or accurate)
        tk.Label(self.frame, text="Approximation Method:").grid(row=2, column=0, padx=2, pady=2)
        self.approximation_method_combobox = ttk.Combobox(self.frame, values=['CHAIN_APPROX_SIMPLE', 'CHAIN_APPROX_NONE'])
        self.approximation_method_combobox.grid(row=2, column=1, padx=2, pady=2)

    def apply(self, img):
        # Get user selections for retrieval mode and approximation method
        retrieval_mode = self.retrieval_mode_combobox.get()
        approximation_method = self.approximation_method_combobox.get()

        # Convert to grayscale if needed
        if len(img.shape) == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img.copy()

        # Apply binary thresholding to create a binary image for contour detection
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        # Convert user input into OpenCV constants
        retrieval_mode_cv = getattr(cv2, retrieval_mode)
        approximation_method_cv = getattr(cv2, approximation_method)

        # Find contours in the binary image
        contours, hierarchy = cv2.findContours(thresh, retrieval_mode_cv, approximation_method_cv)

        # Draw the contours on the original image
        result_img = img.copy()
        cv2.drawContours(result_img, contours, -1, (0, 255, 0), 2)

        return result_img    
    
class DrawContoursFrame(ProcessFrameBase):

    def create_widgets(self):
        # Entry for contour thickness (thickness of contour lines)
        tk.Label(self.frame, text="Contour Thickness:").grid(row=1, column=0, padx=2, pady=2)
        self.thickness_entry = tk.Entry(self.frame)
        self.thickness_entry.grid(row=1, column=1, padx=2, pady=2)

        # Combobox for contour color (select a color for the contours)
        tk.Label(self.frame, text="Contour Color:").grid(row=2, column=0, padx=2, pady=2)
        self.color_combobox = ttk.Combobox(self.frame, values=['Green', 'Red', 'Blue'])
        self.color_combobox.grid(row=2, column=1, padx=2, pady=2)

    def apply(self, img):
        # Get user input for thickness and color
        thickness = int(self.thickness_entry.get())
        contour_color_str = self.color_combobox.get()

        # Set color based on user selection
        if contour_color_str == 'Green':
            contour_color = (0, 255, 0)
        elif contour_color_str == 'Red':
            contour_color = (0, 0, 255)
        else:
            contour_color = (255, 0, 0)

        # Convert to grayscale if needed
        if len(img.shape) == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img.copy()

        # Apply binary thresholding to create a binary image for contour detection
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw the contours on the original image
        result_img = img.copy()
        cv2.drawContours(result_img, contours, -1, contour_color, thickness)

        return result_img    
#! Del canny side of houghlines    
class HoughLinesFrame(ProcessFrameBase):

    def create_widgets(self):
        # Entry for rho (distance resolution of the accumulator in pixels)
        tk.Label(self.frame, text="Rho (Distance Resolution):").grid(row=1, column=0, padx=2, pady=2)
        self.rho_entry = tk.Entry(self.frame)
        self.rho_entry.grid(row=1, column=1, padx=2, pady=2)

        # Entry for theta (angle resolution of the accumulator in radians)
        tk.Label(self.frame, text="Theta (Angle Resolution):").grid(row=2, column=0, padx=2, pady=2)
        self.theta_entry = tk.Entry(self.frame)
        self.theta_entry.grid(row=2, column=1, padx=2, pady=2)

        # Entry for threshold (threshold for line detection)
        tk.Label(self.frame, text="Threshold (Line Detection Threshold):").grid(row=3, column=0, padx=2, pady=2)
        self.threshold_entry = tk.Entry(self.frame)
        self.threshold_entry.grid(row=3, column=1, padx=2, pady=2)

    def apply(self, img):
        # Get user input for rho, theta, and threshold
        rho = float(self.rho_entry.get())
        theta = float(self.theta_entry.get())
        threshold = int(self.threshold_entry.get())

        # Convert to grayscale if needed
        if len(img.shape) == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img.copy()

        # Apply Canny edge detection to get edges for line detection
        edges = cv2.Canny(gray, 50, 150, apertureSize=3)

        # Use HoughLines to detect lines
        lines = cv2.HoughLines(edges, rho, theta, threshold)

        # Draw the detected lines on the original image
        result_img = img.copy()

        if lines is not None:
            for line in lines:
                rho_line, theta_line = line[0]
                x1 = int(rho_line * np.cos(theta_line) + 1000 * (-np.sin(theta_line)))
                y1 = int(rho_line * np.sin(theta_line) + 1000 * (np.cos(theta_line)))
                x2 = int(rho_line * np.cos(theta_line) - 1000 * (-np.sin(theta_line)))
                y2 = int(rho_line * np.sin(theta_line) - 1000 * (np.cos(theta_line)))
                cv2.line(result_img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        return result_img    
    
class DFTFrame(ProcessFrameBase):

    def create_widgets(self):
        # Entry for the size of the image (size of the DFT result)
        tk.Label(self.frame, text="DFT Size:").grid(row=1, column=0, padx=2, pady=2)
        self.size_entry = tk.Entry(self.frame)
        self.size_entry.grid(row=1, column=1, padx=2, pady=2)

        # Combobox for selecting whether to shift the zero frequency component
        tk.Label(self.frame, text="Shift Zero Frequency (Yes/No):").grid(row=2, column=0, padx=2, pady=2)
        self.shift_combobox = ttk.Combobox(self.frame, values=['Yes', 'No'])
        self.shift_combobox.grid(row=2, column=1, padx=2, pady=2)

    def apply(self, img):
        # Get user input for the size and shift option
        dft_size = int(self.size_entry.get())
        shift_zero_freq = self.shift_combobox.get() == 'Yes'

        # Convert to grayscale if needed
        if len(img.shape) == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img.copy()

        # Perform Discrete Fourier Transform (DFT)
        # Padding the image to a larger size if necessary
        padded_img = cv2.copyMakeBorder(gray, 0, dft_size - gray.shape[0], 0, dft_size - gray.shape[1], cv2.BORDER_CONSTANT, value=0)
        
        # Perform DFT
        dft = cv2.dft(np.float32(padded_img), flags=cv2.DFT_COMPLEX_OUTPUT)

        # Shift zero frequency to the center of the spectrum if needed
        if shift_zero_freq:
            dft_shift = np.fft.fftshift(dft)
        else:
            dft_shift = dft

        # Convert DFT result to magnitude for display
        magnitude = cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1])

        # Normalize the magnitude image for display
        magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

        # Convert magnitude to uint8 for display
        result_img = np.uint8(magnitude)

        return result_img    
    
class IDFTFrame(ProcessFrameBase):

    def create_widgets(self):
        # Entry for the size of the image (size of the IDFT result)
        tk.Label(self.frame, text="IDFT Size:").grid(row=1, column=0, padx=2, pady=2)
        self.size_entry = tk.Entry(self.frame)
        self.size_entry.grid(row=1, column=1, padx=2, pady=2)

        # Combobox for selecting whether to shift the zero frequency component
        tk.Label(self.frame, text="Shift Zero Frequency (Yes/No):").grid(row=2, column=0, padx=2, pady=2)
        self.shift_combobox = ttk.Combobox(self.frame, values=['Yes', 'No'])
        self.shift_combobox.grid(row=2, column=1, padx=2, pady=2)

    def apply(self, img):
        # Get user input for the size and shift option
        idft_size = int(self.size_entry.get())
        shift_zero_freq = self.shift_combobox.get() == 'Yes'

        # Convert to grayscale if needed
        if len(img.shape) == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img.copy()

        # Apply Canny edge detection to get edges for line detection
        edges = cv2.Canny(gray, 50, 150, apertureSize=3)

        # Perform DFT
        dft = cv2.dft(np.float32(edges), flags=cv2.DFT_COMPLEX_OUTPUT)

        # Shift zero frequency to the center of the spectrum if needed
        if shift_zero_freq:
            dft_shift = np.fft.fftshift(dft)
        else:
            dft_shift = dft

        # Inverse Discrete Fourier Transform (IDFT)
        idft_shift = np.fft.ifftshift(dft_shift) if shift_zero_freq else dft_shift
        idft = cv2.idft(idft_shift)
        idft_magnitude = cv2.magnitude(idft[:, :, 0], idft[:, :, 1])

        # Normalize the magnitude image for display
        idft_magnitude = cv2.normalize(idft_magnitude, None, 0, 255, cv2.NORM_MINMAX)

        # Convert magnitude to uint8 for display
        result_img = np.uint8(idft_magnitude)

        return result_img    
    
class NumpyFFTFrame(ProcessFrameBase):

    def create_widgets(self):
        # Combobox for selecting FFT or IFFT
        tk.Label(self.frame, text="Transform Type:").grid(row=1, column=0, padx=2, pady=2)
        self.transform_combobox = ttk.Combobox(self.frame, values=["FFT", "IFFT"])
        self.transform_combobox.grid(row=1, column=1, padx=2, pady=2)

    def apply(self, img):
        # Get transform type from combobox
        transform_type = self.transform_combobox.get()

        # Convert image to grayscale if needed
        if len(img.shape) == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img.copy()

        # Convert image to float32
        gray_float = np.float32(gray)

        # Apply selected transform
        match transform_type:
            case "FFT":
                # Apply FFT and shift zero frequency to center
                fft = np.fft.fft2(gray_float)
                fft_shifted = np.fft.fftshift(fft)

                # Calculate magnitude spectrum and normalize
                magnitude = 20 * np.log(np.abs(fft_shifted) + 1)
                result_img = np.uint8(cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX))
                return result_img

            case "IFFT":
                # Apply FFT and then IFFT (reverse back to spatial domain)
                fft = np.fft.fft2(gray_float)
                img_reconstructed = np.fft.ifft2(fft)
                img_reconstructed = np.abs(img_reconstructed)

                # Normalize result for display
                result_img = np.uint8(cv2.normalize(img_reconstructed, None, 0, 255, cv2.NORM_MINMAX))
                return result_img

            case _:
                return img  # No change if invalid selection    

class EqualizeHistFrame(ProcessFrameBase):
    
    def create_widgets(self):
        pass
    
    def apply(self, img):
        
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        equalized_img = cv2.equalizeHist(img)
        return equalized_img
    
    def update_result(self, img):
        result = self.apply(img)
        
        
        plt.figure(figsize=(12,5))
        
        plt.subplot(1, 2, 1)
        plt.title("Original Histogram")
        plt.hist(img.ravel(), bins=256, range=[0,256], color='gray')
        
        plt.subplot(1, 2, 2)
        plt.title("Equalized Histogram")
        plt.hist(result.ravel(), bins=256, range=[0,256], color='black')
        
        plt.tight_layout()
        plt.show() 
#! may be malfunctioning
class CLAHEFrame(ProcessFrameBase):
    
    def create_widgets(self):
        self.clip_limit = tk.DoubleVar(value=2.0)
        self.tile_grid_size = tk.IntVar(value=8)
        
        tk.Label(self.frame, text="Clip Limit:").grid(row=1, column=0, padx=2, pady=2)
        tk.Scale(self.frame, from_=1.0, to=16.0, resolution=0.1,
                variable=self.clip_limit, orient="horizontal").grid(row=1, column=1, padx=2, pady=2)
        
        tk.Label(self.frame, text="Tile Grid Size:").grid(row=2, column=0, padx=2, pady=2)
        tk.Scale(self.frame, from_=1, to=32, variable=self.tile_grid_size,
                orient="horizontal").grid(row=2, column=1, padx=2, pady=2)
    
    def apply(self, img):
        # Convert color image to LAB color space if needed
        is_color = len(img.shape) == 3 and img.shape[2] == 3
        
        # Create CLAHE object
        clahe = cv2.createCLAHE(
            clipLimit=self.clip_limit.get(),
            tileGridSize=(self.tile_grid_size.get(), self.tile_grid_size.get())
        )
        
        if is_color:
            # Convert BGR to LAB
            lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
            l, a, b = cv2.split(lab)
            # Apply CLAHE to the L channel
            l_clahe = clahe.apply(l)
            # Merge and convert back to BGR
            lab_clahe = cv2.merge((l_clahe, a, b))
            result = cv2.cvtColor(lab_clahe, cv2.COLOR_LAB2BGR)
        else:
            # For grayscale image, apply CLAHE directly
            result = clahe.apply(img)
        
        return result
    
    def update_result(self, img):
        result = self.apply(img)
        
        # Show input and output images side by side
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        plt.title("Original Image")
        if len(img.shape) == 2:
            plt.imshow(img, cmap='gray')
        else:
            plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        
        plt.subplot(1, 2, 2)
        plt.title("CLAHE Result")
        if len(result.shape) == 2:
            plt.imshow(result, cmap='gray')
        else:
            plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        
        plt.tight_layout()
        plt.show()



   