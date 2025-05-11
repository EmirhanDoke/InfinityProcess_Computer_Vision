import tkinter as tk
from tkinter import ttk, filedialog
import cv2
from PIL import Image, ImageTk
from methods import *
import matplotlib.pyplot as plt
from utils import Utils

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
        
        self.combo = ttk.Combobox(self.frame, values=available_process, width=35, height=25)
        self.combo.bind("<<ComboboxSelected>>", self.selected_process)
        self.combo.grid(row=0, column=0, padx=2, pady=2)
        
    def selected_process(self, event):
        self.selected_operator = event.widget.get()
        print(f"Selected operator: {self.selected_operator}")

        self.processor = None
        self.processor_np = None
        self.processor_both = None
        # print("Deleted the old process.")

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
                self.processor_np = OtsuThresholdFrame(self.frame)
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
                self.processor_both = EqualizeHistFrame(self.frame)
            case "CLAHE Adaptive Equalization":
                self.processor = CLAHEFrame(self.frame)
            case "OFF":
                    
                self.processor = None
                self.processor_np = None
                self.processor_both = None
                print("Deleted the process.")
                
                # Clear widgets of the process
                for widget in self.frame.winfo_children():
                    if widget != self.combo:
                        widget.destroy()
                                        
    def apply_process(self):
        if self.processor:
            result = self.processor.apply(self.read_img())
            ADD_ComboBox.images.append(result)


        elif self.processor_np:
            self.processor_np.update_result(self.read_img())
            # ADD_ComboBox.images.append(self.read_img())
        

        elif self.processor_both:
            result = self.processor_both.apply(self.read_img())
            ADD_ComboBox.images.append(result)
            self.processor_both.update_result(self.read_img())
                
        else:
            print("No process selected.")


#! Utils

    @classmethod
    def file_path_selecter(cls):
        
        ADD_ComboBox.images = []
        cls.file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.bmp *.jpeg")])
        print(cls.file_path)
        
        if Utils.load_user_settings("show_image_flag") == True:
            ADD_ComboBox.show_image_details(cls.file_path)
        
        return cls.file_path
    
    @classmethod
    def read_img(cls):
        
        if ADD_ComboBox.file_path is None:
            ADD_ComboBox.file_path = ADD_ComboBox.file_path_selecter()
        
        if not ADD_ComboBox.images:
            img = cv2.imread(ADD_ComboBox.file_path)
            print("The Image is read")
            ADD_ComboBox.images.append(img)
        
        return ADD_ComboBox.images[-1]
    
    @classmethod
    def show_image(cls, names=None):
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
            plt.title(names[i])  
        
        plt.tight_layout()
        plt.show()
    
    @classmethod
    def show_image_details(cls, path):
        
        img = cv2.imread(path)
        
        if img is None:
            print("No image loaded.")
            return
        
        # Get image details
        height, width = img.shape[:2]
        channels = img.shape[2] if len(img.shape) == 3 else 1
        img_type = "Grayscale" if channels == 1 else "Color"
        
        # Create a new tkinter window
        details_window = tk.Toplevel()
        details_window.title("Image Details")
        details_window.resizable(False, False)
        
        # Display image details
        details_label = tk.Label(details_window, justify="left" , font=("Ariel",14) ,text=f"Image Details:\n"
                                                       f"{'Width:':<15}{width} px\n"
                                                       f"{'Height:':<15}{height} px\n"
                                                       f"{'Channels:':<15}{channels}\n"
                                                       f"{'Type:':<15}{img_type}")
        details_label.pack(padx = 20, pady=10, side=tk.RIGHT)
        
        image_ratio = width / height
        img = cv2.resize(img, (256, int(256/image_ratio)))
        
        # Convert the image to a format tkinter can display
        if channels == 3:  # Convert BGR to RGB for color images
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img)
        img_tk = ImageTk.PhotoImage(img_pil)
        
        # Display the image
        img_label = tk.Label(details_window, image=img_tk)
        img_label.image = img_tk  # Keep a reference to avoid garbage collection
        img_label.pack(padx = 10, pady=10, side=tk.LEFT)