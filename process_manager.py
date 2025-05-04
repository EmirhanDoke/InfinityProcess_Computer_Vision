import tkinter as tk
from tkinter import ttk, filedialog
import cv2
from PIL import Image
from methods import *
import matplotlib.pyplot as plt

class ADD_ComboBox:
    
    images = []
    file_path = None
    hist_list = []
    
    def __init__(self, frame):
        self.frame = frame
        self.processor = None
        self.add()
        
    def add(self):
        available_process = [ "-----Delete The Process-----", "OFF",
                             "-----Basic Image Operations-----","Color Convert" ,"Resize Image" ,"Rotate Image", "Flip Image", 
                             "-----Image Filtering Operations-----", "Gaussian Blur", "Median Blur", "Bilateral Filter", "Filter2D",
                             "2D-Gabor Filter", "Morphological", 
                             "-----Edge and Corner Detection-----", "Sobel Filter", "Scharr Filter", "Laplacian", "Canny Edge Detection",
                             "Harris Corner Detection", "Shi-Tomasi Corner Detection",
                             "-----Thresholding Operations-----", "Thresholding", "Adaptive Thresholding", "Otsu Thresholding", "Kitter Illingworth", "Gamma Transform",
                             "-----Contour Operations-----", "Find Contours", "Draw Contours",
                             "---Edge Detection and Linear Detection---", "Hough Circular Transform", "Hough Lines Transform",
                             "-----Fourier Transform-----", "DFT Transform", "Inverse DFT Transform", "FFT with Numpy",
                             "-----Histogram Operations-----", "Draw Histogram", "Equalize Histogram","CLAHE Adaptive Equalization",
                             
                             ]
        
        self.combo = ttk.Combobox(self.frame, values=available_process, width=35)
        self.combo.bind("<<ComboboxSelected>>", self.selected_process)
        self.combo.grid(row=0, column=0, padx=2, pady=2)
        
    def selected_process(self, event):
        self.selected_operator = event.widget.get()
        print(f"Selected operator: {self.selected_operator}")

        # Remove old widgets
        for widget in self.frame.winfo_children():
            if widget != self.combo:                                                            #! Bug olma ihtimali var.
                widget.destroy()

        # Create new Widget
        match self.selected_operator:
            case "2D-Gabor Filter":
                self.processor = GaborFilterFrame(self.frame)
            case "Morphological":
                self.processor = MorphologicalFrame(self.frame)
            case "Thresholding":
                self.processor = ThresholdingFrame(self.frame)
            case "Gamma Transform":
                self.processor = GammaTransformFrame(self.frame)
            case "Canny Edge Detection":
                self.processor = CannyEdgeDetectorFrame(self.frame)
            case "Hough Circular Transform":
                self.processor = HoughTransformFrame(self.frame)
            case "Gaussian Blur":
                self.processor = GaussianBlurFrame(self.frame)
            case "Kitter Illingworth":
                self.processor_np = KitterIllingworthFrame(self.frame)
            case "Draw Histogram":
                self.processor_np = DrawHistogramFrame(self.frame)
            case "Color Convert":
                self.processor = ColorConvertFrame(self.frame)
            case "Resize Image":
                self.processor = ResizeFrame(self.frame)    
            case "Rotate Image":
                self.processor = RotateFrame(self.frame)
            case "Flip Image":
                self.processor = FlipFrame(self.frame)    
            case "Median Blur":
                self.processor = MedianBlurFrame(self.frame)    
            case "Bilateral Filter":
                self.processor = BilateralFilterFrame(self.frame)
            case "Filter2D":
                self.processor = Filter2DFrame(self.frame)    
            case "Sobel Filter":
                self.processor = SobelFrame(self.frame)    
            case "Scharr Filter":
                self.processor = ScharrFrame(self.frame)    
            case "Laplacian":
                self.processor = LaplacianFrame(self.frame)    
            case "Harris Corner Detection":
                self.processor = CornerHarrisFrame(self.frame)
            case "Shi-Tomasi Corner Detection":
                self.processor = GoodFeaturesToTrackFrame(self.frame)
            case "Adaptive Thresholding":
                self.processor = AdaptiveThresholdFrame(self.frame)
            case "Otsu Thresholding":
                self.processor = OtsuThresholdFrame(self.frame)
            case "Find Contours":
                self.processor = FindContoursFrame(self.frame)
            case "Draw Contours":
                self.processor = DrawContoursFrame(self.frame)
            case "Hough Lines Transform":
                self.processor = HoughLinesFrame(self.frame)
            case "DFT Transform":
                self.processor = DFTFrame(self.frame)
            case "Inverse DFT Transform":
                self.processor = IDFTFrame(self.frame)  
            case "FFT with Numpy":
                self.processor = NumpyFFTFrame(self.frame)
            case "Equalize Histogram":
                self.processor_np = EqualizeHistFrame(self.frame)
            case "CLAHE Adaptive Equalization":
                self.processor = CLAHEFrame(self.frame)
            case "OFF":
                    
                self.processor = None
                self.processor_np = None
                print("Deleted the process.")
                
                # Clear widgets of the process
                for widget in self.frame.winfo_children():
                    if widget != self.combo:
                        widget.destroy()
        
              

    def apply_process(self):
        if self.processor:
            
            result = self.processor.apply(self.read_img())
            ADD_ComboBox.images.append(result)
  
        else:
            print("No valid processor found.")

        if hasattr(self, 'processor_np'):
            if self.processor_np:
                self.processor_np.update_result(self.read_img())
                ADD_ComboBox.images.append(self.read_img())

#! Utils

    @classmethod
    def file_path_selecter(cls):
        
        ADD_ComboBox.images = []
        cls.file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.bmp *.jpeg")])
        print(cls.file_path)
        return cls.file_path
    
    @classmethod
    def read_img(cls):
        
        
        if ADD_ComboBox.file_path is None:
            ADD_ComboBox.file_path = ADD_ComboBox.file_path_selecter()
        
        if not ADD_ComboBox.images:
            img = cv2.imread(ADD_ComboBox.file_path)
            print("Resim Okundu")
            ADD_ComboBox.images.append(img)
        
        return ADD_ComboBox.images[-1]
    
    @classmethod
    def show_image(cls):
        if len(ADD_ComboBox.images) <= 4:
            cols = 2
        else:
            cols = 3    
        
        rows = (len(ADD_ComboBox.images) + cols - 1) // cols
        
        # Show with Subplot
        plt.figure(figsize=(10, 5))
        for i, img in enumerate(ADD_ComboBox.images):

            plt.subplot(rows, cols, i + 1)
            
            if len(img.shape) == 2:
                if isinstance(img, np.ndarray) and img.size > 0:
                    # if image is grayscale
                    plt.imshow(img, cmap='gray')
                
            elif len(img.shape) == 3 and img.shape[2] == 3:
                if isinstance(img, np.ndarray) and img.size > 0:
                    # Renkli görüntü
                    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    plt.imshow(img_rgb)
            
            else:
                if isinstance(img, np.ndarray) and img.size > 0:
                    plt.imshow(img) 
            
            plt.axis('off') 
            plt.title(f"Image {i+1}")  
        
        plt.tight_layout()
        plt.show()
        