import tkinter as tk
from tkinter import ttk
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter_components.tkinter_info_buttom import *

class ProcessFrameBase:
    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()
    
    def apply(self, img):
        raise NotImplementedError("apply method must be implemented in subclass.")

class ThresholdingFrame(ProcessFrameBase):
    name = "Thresholding"
    info_text = (
    "📌 Threshold Bilgisi\n\n"
    "• Threshold: 0 ile 255 arasında bir değerdir. Bu eşik değeri, görüntüdeki piksellerin ikili hale getirilmesinde kullanılır.\n\n"
    "• Threshold Type:\n"
    "  - Binary: Piksel değeri eşikten büyükse 255 (beyaz), küçükse 0 (siyah) yapılır.\n"
    "  - Binary Inverse: Piksel değeri eşikten büyükse 0 (siyah), küçükse 255 (beyaz) yapılır.\n\n"
    "🎯 Not: Bu işlem sadece gri tonlamalı (grayscale) görüntüler için geçerlidir.\n\n"
    "———————————————\n\n"
    "📌 Threshold Info\n\n"
    "• Threshold: A value between 0 and 255. It is used to convert pixels into binary form based on this threshold.\n\n"
    "• Threshold Type:\n"
    "  - Binary: If the pixel value is greater than the threshold, it becomes 255 (white); otherwise, it becomes 0 (black).\n"
    "  - Binary Inverse: If the pixel value is greater than the threshold, it becomes 0 (black); otherwise, it becomes 255 (white).\n\n"
    "🎯 Note: This operation only works on grayscale images."
)

    
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
        
        self.info_buttom = ImageButtonApp(self.frame, text= ThresholdingFrame.info_text)
     
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
    name = "Gabor Filter"
    info_text = (
    "📌 Gabor Filtresi Parametreleri\n\n"
    "• Ksize: Çekirdeğin (kernel) boyutu. Tek sayı ve pozitif olmalıdır. Örn: 3, 5, 7...\n"
    "• Sigma: Gauss dağılımının standart sapması. Tipik aralık: 1.0 - 10.0\n"
    "• Theta: Filtrenin yönü (radyan cinsinden). 0 ile pi arasında bir değerdir.\n"
    "• Lambda: Sinüzoidal bileşenin dalga boyu. Pozitif bir değerdir. Örn: 4.0\n"
    "• Gamma: En-boy oranı. Genellikle 0 ile 1 arasında olur. 1: dairesel, <1: eliptik yapı.\n"
    "• Phi: Faz kayması. 0 ile 2*pi arasında değer alabilir.\n\n"
    "🎯 Not: Gri seviyeli görsellerle daha iyi sonuç verir.\n\n"
    "———————————————\n\n"
    "📌 Gabor Filter Parameters\n\n"
    "• Ksize: Kernel size. Must be a positive odd number. E.g., 3, 5, 7...\n"
    "• Sigma: Standard deviation of the Gaussian envelope. Typical range: 1.0 - 10.0\n"
    "• Theta: Orientation of the filter in radians. Should be between 0 and pi.\n"
    "• Lambda: Wavelength of the sinusoidal component. Must be positive. E.g., 4.0\n"
    "• Gamma: Aspect ratio. Usually between 0 and 1. 1: circular, <1: elliptical shape.\n"
    "• Phi: Phase offset. Should be between 0 and 2*pi.\n\n"
    "🎯 Note: Works best with grayscale images."
)

    
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

        self.info_buttom = ImageButtonApp(self.frame, text= GaborFilterFrame.info_text)

    def apply(self, img):
        
        ksize = int(self.ksize_entry.get())
        sigma = int(self.sigma_entry.get())
        theta = int(self.theta_entry.get())
        lamda = float(self.lambda_frame.get())
        gamma = float(self.gamma_entry.get())
        phi = int(self.phi_entry.get())
                
        ht_kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lamda, gamma, phi, ktype=cv2.CV_32F)
        img = cv2.filter2D(img, cv2.CV_8UC3, ht_kernel)
        return img

class MorphologicalFrame(ProcessFrameBase):
    name = "Morphological" 
    info_text = (
    "📌 Morfolojik İşlemler Parametreleri\n\n"
    "• Kernel Size: Yapısal elemanın boyutudur. Pozitif ve tek sayı olmalıdır. Örn: 3, 5, 7...\n"
    "• Kernel Shape: Çekirdek şeklidir. Rectangular (dikdörtgen), Ellipse (elips), veya Cross (çapraz) olabilir.\n"
    "• Operations: Uygulanacak morfolojik işlemi seçin:\n"
    "  - Erode: Nesneleri küçültür.\n"
    "  - Dilation: Nesneleri genişletir.\n"
    "  - Opening: Gürültü temizleme (erode ardından dilation).\n"
    "  - Closing: Küçük boşlukları kapatma (dilation ardından erode).\n"
    "  - Gradient: Kenarları çıkarır (dilation - erode).\n"
    "  - Top Hat: Orijinal görüntü - Opening sonucu.\n"
    "  - Black Hat: Closing sonucu - Orijinal görüntü.\n"
    "• Iterations: İşlemin kaç kez uygulanacağını belirtir. Genellikle 1-5 arası kullanılır.\n\n"
    "🎯 Not: Gri seviyeli görüntülerle daha etkili sonuçlar elde edilir.\n\n"
    "———————————————\n\n"
    "📌 Morphological Operations Parameters\n\n"
    "• Kernel Size: Size of the structuring element. Must be a positive odd number. E.g., 3, 5, 7...\n"
    "• Kernel Shape: Shape of the kernel. Can be Rectangular, Ellipse, or Cross.\n"
    "• Operations: Select the desired morphological operation:\n"
    "  - Erode: Shrinks objects.\n"
    "  - Dilation: Expands objects.\n"
    "  - Opening: Removes small noise (erode followed by dilation).\n"
    "  - Closing: Closes small holes (dilation followed by erode).\n"
    "  - Gradient: Extracts edges (dilation - erode).\n"
    "  - Top Hat: Original image - Opening result.\n"
    "  - Black Hat: Closing result - Original image.\n"
    "• Iterations: Number of times the operation is repeated. Usually between 1 and 5.\n\n"
    "🎯 Note: Grayscale images give better results for most morphological operations."
)

    
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

        self.info_buttom = ImageButtonApp(self.frame, text= MorphologicalFrame.info_text)

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
        
            case  "Dilation":
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
    name = "Gamma Transform"
    info_text = (
    "📌 Gamma Dönüşümü Parametreleri\n\n"
    "• Gamma Value: Görüntünün parlaklığını ayarlayan pozitif bir değerdir. Genellikle 0.1 ile 5.0 arasında olur.\n"
    "  - Gamma < 1: Görüntü kararmaya başlar (daha koyu).\n"
    "  - Gamma > 1: Görüntü aydınlanır (daha parlak).\n\n"
    "🎯 Not: Görüntüdeki kontrastı değiştirebilir, ancak aşırı değerler görsel bozulmalara yol açabilir.\n\n"
    "———————————————\n\n"
    "📌 Gamma Correction Parameters\n\n"
    "• Gamma Value: A positive value that adjusts the brightness of the image. It usually ranges between 0.1 and 5.0.\n"
    "  - Gamma < 1: The image becomes darker.\n"
    "  - Gamma > 1: The image becomes brighter.\n\n"
    "🎯 Note: It can change the contrast of the image, but extreme values may cause visual distortions."
)

    
    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()
    
    def create_widgets(self):
        
        tk.Label(self.frame, text="Gamma Value:").grid(row=1, column=0, padx=2, pady=2)
        self.gamma_transform_entry = tk.Entry(self.frame)
        self.gamma_transform_entry.grid(row=1, column=1, padx=2, pady=2)

        self.info_buttom = ImageButtonApp(self.frame, text= GammaTransformFrame.info_text)


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
    name = "Canny Edge Detection"
    info_text = (
    "📌 Canny Kenar Algılama Parametreleri\n\n"
    "• Kernel Size: Canny algılama çekirdeğinin boyutudur. Pozitif ve tek sayı olmalıdır. Örn: 3, 5, 7...\n"
    "• Low Threshold: Canny algoritmasındaki düşük eşik değeridir. 0 ile 255 arasında olmalıdır.\n"
    "• Max Threshold: Canny algoritmasındaki yüksek eşik değeridir. 0 ile 255 arasında olmalıdır.\n"
    "• L2gradient: L2 normunun kullanılıp kullanılmayacağını belirtir. True ya da False olarak seçilebilir.\n\n"
    "🎯 Not: Düşük eşik değeri, kenarları daha hassas bir şekilde tespit eder. Yüksek eşik değeri, sadece belirgin kenarları alır.\n\n"
    "• Giriş Görseli: Gri seviyeli bir görüntü olmalıdır. Renkli görüntülerde de işlem yapılabilir ancak en iyi sonuçlar **gri seviyeli** görüntülerde alınır.\n\n"
    "———————————————\n\n"
    "📌 Canny Edge Detection Parameters\n\n"
    "• Kernel Size: Size of the Canny detection kernel. Must be a positive odd number. E.g., 3, 5, 7...\n"
    "• Low Threshold: The low threshold value for Canny algorithm. It should be between 0 and 255.\n"
    "• Max Threshold: The high threshold value for Canny algorithm. It should be between 0 and 255.\n"
    "• L2gradient: Whether to use the L2 norm. Can be True or False.\n\n"
    "🎯 Note: A lower threshold captures finer edges, while a higher threshold detects more prominent edges.\n\n"
    "• Input Image: The image should be in grayscale. It can also work with color images, but the best results are achieved with **grayscale** images."
)

    
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
    
        self.info_buttom = ImageButtonApp(self.frame, text= CannyEdgeDetectorFrame.info_text)
    
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
    name = "Hough Transform"   
    info_text = (
    "📌 Hough Dönüşümü ile Çevre Algılama Parametreleri\n\n"
    "• Dp: Hough dönüşümünde kullanılan çözünürlük parametresidir. Genellikle 1.0 veya daha büyük bir değer olmalıdır.\n"
    "• Minimum Distance: Tespit edilen daireler arasındaki minimum mesafedir. Pozitif bir tamsayı olmalıdır.\n"
    "• Param1: Canny kenar algılama algoritmasındaki yüksek eşik değeridir. 0 ile 255 arasında olmalıdır.\n"
    "• Param2: Dairelerin merkezinin bulunabilmesi için gereken eşik değeridir. 0 ile 100 arasında olmalıdır.\n"
    "• Minimum Radius: Tespit edilecek dairelerin minimum çapıdır. 0 ile 100 arasında olmalıdır.\n"
    "• Maximum Radius: Tespit edilecek dairelerin maksimum çapıdır. 0 ile 100 arasında olmalıdır.\n"
    "• Mark Color: Tespit edilen dairelerin işaretleneceği renk. Seçenekler: Kırmızı (Red) veya Mavi (Blue).\n\n"
    "• Giriş Görseli: Giriş görseli, gri seviyeli veya renkli olabilir, ancak genellikle gri seviyeli görsellerde daha net sonuçlar alınır.\n"
    "🎯 Not: Dairelerin net bir şekilde tespit edilebilmesi için giriş görselinin yüksek kontrast ve net olması önerilir.\n\n"
    "———————————————\n\n"
    "📌 Hough Transform Circle Detection Parameters\n\n"
    "• Dp: The resolution parameter used in Hough transform. It should be a positive integer, usually 1.0 or higher.\n"
    "• Minimum Distance: The minimum distance between detected circles. It should be a positive integer.\n"
    "• Param1: The high threshold value for the Canny edge detection algorithm. It should be between 0 and 255.\n"
    "• Param2: The threshold for center detection of the circles. It should be between 0 and 100.\n"
    "• Minimum Radius: The minimum radius of circles to be detected. It should be between 0 and 100.\n"
    "• Maximum Radius: The maximum radius of circles to be detected. It should be between 0 and 100.\n"
    "• Mark Color: The color to mark detected circles. Options: Red or Blue.\n\n"
    "• Input Image: The input image can be grayscale or colored, but grayscale images generally produce sharper results.\n"
    "🎯 Note: For better results, the input image should have high contrast and sharp edges."
)
    
        
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
    
        self.info_buttom = ImageButtonApp(self.frame, text= HoughTransformFrame.info_text)
    
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
    name = "Gaussian Blur"    
    info_text = (
    "📌 Hough Dönüşümü ile Çevre Algılama Parametreleri\n\n"
    "• Dp: Hough dönüşümünde kullanılan çözünürlük parametresidir. Genellikle 1.0 veya daha büyük bir değer olmalıdır.\n"
    "• Minimum Distance: Tespit edilen daireler arasındaki minimum mesafedir. Pozitif bir tamsayı olmalıdır.\n"
    "• Param1: Canny kenar algılama algoritmasındaki yüksek eşik değeridir. 0 ile 255 arasında olmalıdır.\n"
    "• Param2: Dairelerin merkezinin bulunabilmesi için gereken eşik değeridir. 0 ile 100 arasında olmalıdır.\n"
    "• Minimum Radius: Tespit edilecek dairelerin minimum çapıdır. 0 ile 100 arasında olmalıdır.\n"
    "• Maximum Radius: Tespit edilecek dairelerin maksimum çapıdır. 0 ile 100 arasında olmalıdır.\n"
    "• Mark Color: Tespit edilen dairelerin işaretleneceği renk. Seçenekler: Kırmızı (Red) veya Mavi (Blue).\n\n"
    "🎯 Not: Dairelerin net bir şekilde tespit edilebilmesi için giriş görselinin yüksek kontrast ve net olması önerilir.\n\n"
    "———————————————\n\n"
    "📌 Hough Transform Circle Detection Parameters\n\n"
    "• Dp: The resolution parameter used in Hough transform. It should be a positive integer, usually 1.0 or higher.\n"
    "• Minimum Distance: The minimum distance between detected circles. It should be a positive integer.\n"
    "• Param1: The high threshold value for the Canny edge detection algorithm. It should be between 0 and 255.\n"
    "• Param2: The threshold for center detection of the circles. It should be between 0 and 100.\n"
    "• Minimum Radius: The minimum radius of circles to be detected. It should be between 0 and 100.\n"
    "• Maximum Radius: The maximum radius of circles to be detected. It should be between 0 and 100.\n"
    "• Mark Color: The color to mark detected circles. Options: Red or Blue.\n\n"
    "🎯 Note: For better results, the input image should have high contrast and sharp edges."
)

    
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
    
        self.info_buttom = ImageButtonApp(self.frame, text= GaussianBlurFrame.info_text)
    
    def apply(self, img):
        
        ksize = int(self.ksize_entry.get())
        sigmax = float(self.sigmax_entry.get())
        sigmay = float(self.sigmay_entry.get())
        
        img = cv2.GaussianBlur(img, (ksize, ksize), sigmax, sigmay)
    
        return img

class KitterIllingworthFrame(ProcessFrameBase):
    name = "Kittler-Illingworth"
    info_text = (
    "📌 Kittler-Illingworth Optimum Eşik Değeri Parametreleri\n\n"
    "• Optimum Threshold: Kittler-Illingworth yöntemine dayalı olarak görüntüdeki optimum eşik değeri.\n"
    "• Kittler-Illingworth yöntemi, görüntü histogramındaki iki sınıfı (arka plan ve ön plan) ayıran eşik değerini bulur.\n"
    "• Bu yöntem, sınıfların varyanslarını dikkate alarak en düşük maliyeti veren eşik değerini belirler.\n\n"
    "🎯 Not: Kittler-Illingworth yöntemi, özellikle aydınlık ve karanlık bölgelerin net bir şekilde ayrıldığı görüntülerde daha iyi sonuç verir.\n\n"
    "———————————————\n\n"
    "📌 Kittler-Illingworth Optimum Threshold Parameters\n\n"
    "• Optimum Threshold: The optimum threshold based on the Kittler-Illingworth method for separating background and foreground.\n"
    "• The Kittler-Illingworth method determines the threshold value that minimizes the cost function, considering the variance of both classes (background and foreground).\n\n"
    "🎯 Note: The Kittler-Illingworth method works best for images where the background and foreground are clearly separated."
)

    
    def create_widgets(self):
        
        tk.Label(self.frame, text="Optimum Threshold:").grid(row=1, column=0, padx=2, pady=2)
        self.optimum_threshold_label = tk.Label(self.frame)
        self.optimum_threshold_label.grid(row=1, column=1, padx=2, pady=2)
        
        self.info_buttom = ImageButtonApp(self.frame, text= KitterIllingworthFrame.info_text)
        
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
    name = "Draw Histogram"
    info_text = (
    "📌 Görüntü Histogramı Çizimi Parametreleri\n\n"
    "• Görüntü Histogramı: Görüntüdeki piksellerin renk yoğunluklarını gösteren bir grafiktir.\n"
    "• Histogram, görüntüdeki farklı renk yoğunluklarının dağılımını analiz etmek için kullanılır.\n"
    "• Bu işlem, her pikselin gri ton değeri için frekansları hesaplar ve bir histogram oluşturur.\n\n"
    "🎯 Not: Histogram analizi, kontrast, parlaklık ayarları veya görüntü iyileştirme tekniklerini belirlemek için faydalıdır.\n\n"
    "———————————————\n\n"
    "📌 Image Histogram Drawing Parameters\n\n"
    "• Image Histogram: A graph that shows the frequency of pixel intensities in an image.\n"
    "• The histogram represents the distribution of pixel values across the image, useful for image analysis.\n"
    "• This operation calculates the frequency of each grayscale value and creates a histogram.\n\n"
    "🎯 Note: Histogram analysis is useful for determining contrast, brightness settings, or image enhancement techniques."
)

    
    def create_widgets(self):
        self.info_buttom = ImageButtonApp(self.frame, text= DrawHistogramFrame.info_text)
    
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

class ColorConvertFrame(ProcessFrameBase):
    name = "Color Conversion"
    info_text = (
    "📌 Renk Dönüşümü Parametreleri\n\n"
    "• RGB'den Grayscale'e: Renkli bir görüntüyü gri tonlara dönüştürür. Her pikselin gri ton değeri hesaplanır.\n"
    "• Grayscale'den RGB'ye: Gri tonlu bir görüntüyü renklendirilmiş (RGB) görüntüye dönüştürür. Ancak orijinal renk bilgisi kaybolur.\n"
    "• RGB'den HSV'ye: Renkli bir görüntüyü, renk (Hue), doygunluk (Saturation) ve parlaklık (Value) bileşenlerine ayırır.\n"
    "• HSV'den RGB'ye: HSV formatındaki bir görüntüyü, kırmızı-yeşil-mavi (RGB) formatına dönüştürür.\n\n"
    "🎯 Not: Görüntü işleme ve renk analizi için uygun renk dönüşümünü seçmek önemlidir.\n\n"
    "———————————————\n\n"
    "📌 Color Conversion Parameters\n\n"
    "• RGB to Grayscale: Converts a color image to grayscale. Each pixel is converted to a corresponding grayscale value.\n"
    "• Grayscale to RGB: Converts a grayscale image back to RGB. The original color information is lost.\n"
    "• RGB to HSV: Converts an image from RGB to HSV, separating hue, saturation, and value components.\n"
    "• HSV to RGB: Converts an image from HSV back to RGB.\n\n"
    "🎯 Note: Selecting the appropriate color conversion is crucial for image processing and color analysis."
)


    def create_widgets(self):
        tk.Label(self.frame, text="Select Color Conversion:").grid(row=1, column=0, padx=2, pady=2)
        
        # Combobox for color conversion type
        self.color_convert_combobox = ttk.Combobox(self.frame, values=["RGB to Grayscale", "Grayscale to RGB", "RGB to HSV", "HSV to RGB"])
        self.color_convert_combobox.grid(row=1, column=1, padx=2, pady=2)
        self.color_convert_combobox.set("RGB to Grayscale")

        self.info_buttom = ImageButtonApp(self.frame, text= ColorConvertFrame.info_text)

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
    name = "Resize"
    info_text = (
    "📌 Görüntü Yeniden Boyutlandırma Parametreleri\n\n"
    "• Width (Genişlik): Görüntünün yeni genişliği. Pozitif bir tamsayı değeri olmalıdır.\n"
    "• Height (Yükseklik): Görüntünün yeni yüksekliği. Pozitif bir tamsayı değeri olmalıdır.\n\n"
    "🎯 Not: Görüntü boyutları değiştirilirken orijinal görüntünün en-boy oranı korunmaz, bu da distorsiyona neden olabilir.\n\n"
    "———————————————\n\n"
    "📌 Image Resizing Parameters\n\n"
    "• Width: The new width of the image. It should be a positive integer.\n"
    "• Height: The new height of the image. It should be a positive integer.\n\n"
    "🎯 Note: Resizing the image may cause distortion as the original aspect ratio is not preserved."
)


    def create_widgets(self):
        tk.Label(self.frame, text="Width:").grid(row=1, column=0, padx=2, pady=2)
        self.width_entry = tk.Entry(self.frame)
        self.width_entry.grid(row=1, column=1, padx=2, pady=2)
        
        tk.Label(self.frame, text="Height:").grid(row=2, column=0, padx=2, pady=2)
        self.height_entry = tk.Entry(self.frame)
        self.height_entry.grid(row=2, column=1, padx=2, pady=2)
        
        self.info_buttom = ImageButtonApp(self.frame, text= ResizeFrame.info_text)

    def apply(self, img):
        width = int(self.width_entry.get())
        height = int(self.height_entry.get())

        # Resize the image
        resized_image = cv2.resize(img, (width, height))

        return resized_image

class RotateFrame(ProcessFrameBase):
    name = "Rotate"
    info_text = (
    "📌 Görüntü Döndürme Parametreleri\n\n"
    "• Rotation Angle (Dönme Açısı): Görüntünün döneceği açı. Seçenekler: 90°, 180°, 270°.\n\n"
    "🎯 Not: Seçilen döndürme açısı, görüntüyü saat yönünde veya saat yönünün tersine döndürür.\n\n"
    "———————————————\n\n"
    "📌 Image Rotation Parameters\n\n"
    "• Rotation Angle: The angle by which the image will be rotated. Options: 90°, 180°, 270°.\n\n"
    "🎯 Note: The selected rotation angle will rotate the image clockwise or counterclockwise."
)


    def create_widgets(self):
        tk.Label(self.frame, text="Select Rotation Angle:").grid(row=1, column=0, padx=2, pady=2)
        
        # Combobox for rotation angles
        self.rotation_combobox = ttk.Combobox(self.frame, values=["90", "180", "270"])
        self.rotation_combobox.grid(row=1, column=1, padx=2, pady=2)
        self.rotation_combobox.set("90")

        self.info_buttom = ImageButtonApp(self.frame, text= RotateFrame.info_text)

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
    name = "Flip"
    info_text = (
    "📌 Görüntü Çevirme Parametreleri\n\n"
    "• Flip Direction (Çevirme Yönü): Görüntünün hangi yönde çevrileceği. Seçenekler: Yatay (Horizontal), Dikey (Vertical), Her İki Yön (Both).\n\n"
    "🎯 Not: Yatay çevirme, görüntüyü soldan sağa ters çevirir; dikey çevirme, görüntüyü yukarıdan aşağıya ters çevirir. Her iki yön seçildiğinde, hem yatay hem de dikey olarak tersine döner.\n\n"
    "———————————————\n\n"
    "📌 Image Flip Parameters\n\n"
    "• Flip Direction: The direction in which the image will be flipped. Options: Horizontal, Vertical, Both.\n\n"
    "🎯 Note: Horizontal flip reverses the image left to right; vertical flip reverses the image top to bottom. Choosing both flips will reverse the image in both directions."
)


    def create_widgets(self):
        tk.Label(self.frame, text="Select Flip Direction:").grid(row=1, column=0, padx=2, pady=2)
        
        # Combobox for flip directions
        self.flip_combobox = ttk.Combobox(self.frame, values=["Horizontal", "Vertical", "Both"])
        self.flip_combobox.grid(row=1, column=1, padx=2, pady=2)
        self.flip_combobox.set("Horizontal")
        
        self.info_buttom = ImageButtonApp(self.frame, text= FlipFrame.info_text)

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
    name = "Median Blur"
    info_text = (
    "📌 Median Blur (Medyan Bulanıklığı) Parametreleri\n\n"
    "• Kernel Size (Çekirdek Boyutu): Median bulanıklık algoritmasında kullanılan çekirdek boyutudur. Genellikle tek sayılar (3, 5, 7 vb.) kullanılır.\n\n"
    "🎯 Not: Çekirdek boyutunu arttırmak, daha fazla bulanıklık sağlar, ancak detayların kaybolmasına da yol açabilir. Görüntüdeki gürültüleri yumuşatmak için uygundur.\n\n"
    "———————————————\n\n"
    "📌 Median Blur Parameters\n\n"
    "• Kernel Size: The size of the kernel used in the median blur algorithm. Typically, odd numbers (3, 5, 7, etc.) are used.\n\n"
    "🎯 Note: Increasing the kernel size results in more blur, but it may also cause the loss of finer details. It's useful for smoothing out noise in an image."
)


    def create_widgets(self):
        tk.Label(self.frame, text="Kernel Size:").grid(row=1, column=0, padx=2, pady=2)
        self.kernel_size_entry = tk.Entry(self.frame)
        self.kernel_size_entry.grid(row=1, column=1, padx=2, pady=2)
        
        self.info_buttom = ImageButtonApp(self.frame, text= MedianBlurFrame.info_text)

    def apply(self, img):
        kernel_size = int(self.kernel_size_entry.get())

        # Apply Median Blur
        blurred_image = cv2.medianBlur(img, kernel_size)

        return blurred_image

#! May be not working
class BilateralFilterFrame(ProcessFrameBase):
    name = "Bilateral Filter"
    info_text = (
    "📌 Bilateral Filter (İki Taraflı Filtre) Parametreleri\n\n"
    "• Diameter: Filtreleme sırasında her pikselin çevresinde kullanılacak piksel komşuluğunun çapı. Pozitif bir tamsayı olmalıdır.\n"
    "• Sigma Color: Renk uzayındaki standart sapmadır. Bu değer arttıkça, benzer renklerdeki pikseller daha fazla etkilenir.\n"
    "• Sigma Space: Uzamsal koordinatlar arasındaki mesafeye göre olan standart sapmadır. Bu değer arttıkça, daha uzak pikseller filtreye dahil edilir.\n\n"
    "🎯 Not: Bilateral filtre, kenarları koruyarak gürültüyü azaltmak için idealdir. Bu nedenle kenar netliğinin korunması istenen görüntülerde tercih edilir.\n\n"
    "———————————————\n\n"
    "📌 Bilateral Filter Parameters\n\n"
    "• Diameter: Diameter of each pixel neighborhood used during filtering. Should be a positive integer.\n"
    "• Sigma Color: Standard deviation in the color space. Higher values mean that farther colors within the neighborhood will be mixed together.\n"
    "• Sigma Space: Standard deviation in the coordinate space. Higher values mean that farther pixels will influence each other.\n\n"
    "🎯 Note: Bilateral filter is ideal for reducing noise while preserving edges. It’s commonly used when edge sharpness must be maintained."
)


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
        
        self.info_buttom = ImageButtonApp(self.frame, text= BilateralFilterFrame.info_text)

    def apply(self, img):
        d = int(self.d_entry.get())
        sigma_color = float(self.sigma_color_entry.get())
        sigma_space = float(self.sigma_space_entry.get())

        # Apply Bilateral Filter
        filtered_image = cv2.bilateralFilter(img, d, sigma_color, sigma_space)

        return filtered_image

class Filter2DFrame(ProcessFrameBase):
    name = "Filter2D"
    info_text = (
    "📌 filter2D Konvolüsyon İşlemi Parametreleri\n\n"
    "• 3x3 Kernel: Görüntü üzerine uygulanacak çekirdek (kernel) değerlerini ifade eder.\n"
    "  Bu değerler, konvolüsyon işleminde her pikselin komşularıyla nasıl birleştirileceğini belirler.\n"
    "  Örneğin, kenar algılama, bulanıklaştırma veya keskinleştirme işlemleri için farklı çekirdekler kullanılabilir.\n\n"
    "🎯 Not: Girdi görüntüsü net ve kontrastlı olursa konvolüsyon etkisi daha belirgin olur.\n"
    "      Kernel değerlerinin toplamı yüksekse görüntü aydınlanabilir; negatif değerler keskinleştirme sağlar.\n\n"
    "———————————————\n\n"
    "📌 filter2D Convolution Parameters\n\n"
    "• 3x3 Kernel: Represents the kernel values to be applied over the image.\n"
    "  These values define how each pixel is combined with its neighbors during the convolution operation.\n"
    "  Different kernels are used for edge detection, blurring, or sharpening.\n\n"
    "🎯 Note: A sharp and high-contrast input image will yield more visible convolution effects.\n"
    "      If the kernel values sum up to a high value, the output image may become brighter; negative values enhance edges."
)


    def create_widgets(self):
        tk.Label(self.frame, text="3x3 Kernel Values (row-wise):").grid(row=1, column=0, columnspan=2, padx=2, pady=2)

        self.info_buttom = ImageButtonApp(self.frame, text= Filter2DFrame.info_text)

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
    name = "Sobel Edge Detection"
    info_text = (
    "📌 Sobel Kenar Algılama Parametreleri\n\n"
    "• dx: x ekseni yönünde türev alınıp alınmayacağını belirtir. 1 ise x yönlü kenarları algılar.\n"
    "• dy: y ekseni yönünde türev alınıp alınmayacağını belirtir. 1 ise y yönlü kenarları algılar.\n"
    "• Kernel Size: Sobel filtresinde kullanılacak çekirdek boyutudur. Pozitif tek sayı (örneğin: 1, 3, 5) olmalıdır.\n\n"
    "🎯 Not: dx ve dy birlikte 1 olarak seçilirse hem yatay hem dikey kenarlar algılanır.\n\n"
    "———————————————\n\n"
    "📌 Sobel Edge Detection Parameters\n\n"
    "• dx: Specifies whether to take the derivative in the x-direction. 1 detects horizontal edges.\n"
    "• dy: Specifies whether to take the derivative in the y-direction. 1 detects vertical edges.\n"
    "• Kernel Size: The size of the kernel to be used in the Sobel filter. It must be an odd positive integer (e.g., 1, 3, 5).\n\n"
    "🎯 Note: If both dx and dy are set to 1, both horizontal and vertical edges are detected."
)


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

        self.info_buttom = ImageButtonApp(self.frame, text= SobelFrame.info_text)

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
    name = "Scharr Edge Detection"
    info_text = (
    "📌 Scharr Kenar Algılama Parametreleri\n\n"
    "• dx: x ekseni yönünde türev alınıp alınmayacağını belirtir. 1 seçilirse yatay kenarları algılar.\n"
    "• dy: y ekseni yönünde türev alınıp alınmayacağını belirtir. 1 seçilirse dikey kenarları algılar.\n\n"
    "🎯 Not: Scharr filtresi, özellikle küçük çekirdek boyutlarında (örneğin 3x3) Sobel filtresine göre daha hassas sonuçlar verir.\n\n"
    "———————————————\n\n"
    "📌 Scharr Edge Detection Parameters\n\n"
    "• dx: Indicates whether to compute the derivative in the x-direction. 1 detects horizontal edges.\n"
    "• dy: Indicates whether to compute the derivative in the y-direction. 1 detects vertical edges.\n\n"
    "🎯 Note: The Scharr filter provides more accurate results than the Sobel filter, especially for small kernel sizes like 3x3."
)


    def create_widgets(self):
        # dx selecting
        tk.Label(self.frame, text="dx:").grid(row=1, column=0, padx=2, pady=2)
        self.dx_combobox = ttk.Combobox(self.frame, values=[0, 1])
        self.dx_combobox.grid(row=1, column=1, padx=2, pady=2)

        # dy selecting
        tk.Label(self.frame, text="dy:").grid(row=2, column=0, padx=2, pady=2)
        self.dy_combobox = ttk.Combobox(self.frame, values=[0, 1])
        self.dy_combobox.grid(row=2, column=1, padx=2, pady=2)

        self.info_buttom = ImageButtonApp(self.frame, text= ScharrFrame.info_text)

    def apply(self, img):
        dx = int(self.dx_combobox.get())
        dy = int(self.dy_combobox.get())

        # Apply
        scharr_image = cv2.Scharr(img, cv2.CV_64F, dx, dy)

        # Normalize image and convert to uint8
        scharr_image = cv2.convertScaleAbs(scharr_image)

        return scharr_image

class LaplacianFrame(ProcessFrameBase):
    name = "Laplacian Edge Detection"
    info_text = (
    "📌 Laplace Kenar Algılama Parametresi\n\n"
    "• Kernel Size: Türevi alırken kullanılan çekirdek (kernel) boyutu. Tek sayı ve pozitif olmalıdır (örn. 1, 3, 5).\n"
    "Daha büyük değerler daha fazla kenar detayı çıkarabilir fakat aynı zamanda görüntüde bulanıklığa da yol açabilir.\n\n"
    "🎯 Not: Laplace operatörü, görüntüdeki ikinci türev bilgisini kullanarak kenarları simetrik olarak algılar.\n\n"
    "———————————————\n\n"
    "📌 Laplacian Edge Detection Parameter\n\n"
    "• Kernel Size: The size of the filter kernel used for computing the derivative. Must be a positive odd number (e.g., 1, 3, 5).\n"
    "Larger values may enhance edge details but also introduce blurring.\n\n"
    "🎯 Note: The Laplacian operator uses the second derivative of the image to detect edges symmetrically."
)


    def create_widgets(self):
        # Entry for kernel size (must be odd and positive)
        tk.Label(self.frame, text="Kernel Size (e.g., 1, 3, 5):").grid(row=1, column=0, padx=2, pady=2)
        self.ksize_entry = tk.Entry(self.frame)
        self.ksize_entry.grid(row=1, column=1, padx=2, pady=2)
        
        self.info_buttom = ImageButtonApp(self.frame, text= LaplacianFrame.info_text)

    def apply(self, img):
        ksize = int(self.ksize_entry.get())

        # Apply Laplacian operator using 64-bit float depth
        laplacian_image = cv2.Laplacian(img, cv2.CV_64F, ksize=ksize)

        # Convert the result to 8-bit absolute values for display
        laplacian_image = cv2.convertScaleAbs(laplacian_image)

        return laplacian_image

class CornerHarrisFrame(ProcessFrameBase):
    name = "Harris Corner Detection"
    info_text = (
    "📌 Harris Köşe Algılama Parametreleri\n\n"
    "• Block Size: Her piksel için köşe algılamada kullanılan komşuluk boyutu.\n"
    "• Sobel Kernel Size: Türevlerin hesaplandığı Sobel filtresinin boyutu.\n"
    "• k Değeri: Harris denkleminde kullanılan serbest parametre (genellikle 0.04 - 0.06 arası).\n\n"
    "🟥 Yüksek cevap veren alanlar kırmızı ile işaretlenir, bu alanlar köşe içeriyor olabilir.\n\n"
    "———————————————\n\n"
    "📌 Harris Corner Detection Parameters\n\n"
    "• Block Size: Neighborhood size considered for corner detection around each pixel.\n"
    "• Sobel Kernel Size: Aperture size for the Sobel derivative.\n"
    "• k Value: Harris detector free parameter, typically between 0.04 and 0.06.\n\n"
    "🟥 Areas with high corner response are marked in red, indicating potential corners."
)


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

        self.info_buttom = ImageButtonApp(self.frame, text= CornerHarrisFrame.info_text)

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
    name = "Shi-Tomasi Corner Detection"
    info_text = (
    "📌 Köşe Algılama: goodFeaturesToTrack\n\n"
    "• Max Corners: Algılanacak maksimum köşe sayısı.\n"
    "• Quality Level: Algılanan köşelerin minimum kalite eşiği (0 ile 1 arasında).\n"
    "• Min Distance: Algılanan köşeler arasındaki minimum mesafe (piksel cinsinden).\n\n"
    "🟢 Algılanan köşeler yeşil dairelerle gösterilir.\n\n"
    "———————————————\n\n"
    "📌 Corner Detection: goodFeaturesToTrack\n\n"
    "• Max Corners: Maximum number of corners to detect.\n"
    "• Quality Level: Minimum quality threshold for corners (between 0 and 1).\n"
    "• Min Distance: Minimum Euclidean distance between detected corners.\n\n"
    "🟢 Detected corners are drawn as green circles."
)


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

        self.info_buttom = ImageButtonApp(self.frame, text= GoodFeaturesToTrackFrame.info_text)

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
    name = "Adaptive Thresholding"
    info_text = (
    "📌 Adaptif Eşikleme: adaptiveThreshold\n\n"
    "• Max Value: Eşik üstündeki piksellere verilecek maksimum değer.\n"
    "• Adaptive Method: Yerel ortalama (Mean) veya Gauss ağırlıklı ortalama (Gaussian).\n"
    "• Threshold Type: Binary (beyaz-siyah) ya da Binary Inverted (siyah-beyaz).\n"
    "• Block Size: Yerel eşikleme için pencere boyutu (tek sayı ve >1 olmalı).\n"
    "• C: Ortalama değerden çıkarılacak sabit.\n\n"
    "📄 Bu işlem yalnızca gri seviye görüntülerde çalışır.\n\n"
    "———————————————\n\n"
    "📌 Adaptive Thresholding: adaptiveThreshold\n\n"
    "• Max Value: Maximum value to assign to thresholded pixels.\n"
    "• Adaptive Method: Local Mean or Gaussian-weighted mean.\n"
    "• Threshold Type: Binary or Binary Inverted.\n"
    "• Block Size: Size of the local window (odd number > 1).\n"
    "• C: Constant subtracted from the mean.\n\n"
    "📄 Works only on grayscale images."
)


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

        self.info_buttom = ImageButtonApp(self.frame, text= AdaptiveThresholdFrame.info_text)

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
    name = "Otsu Thresholding"
    info_text = (
    "📌 Otsu Eşikleme: cv2.threshold + THRESH_OTSU\n\n"
    "• Max Value: Eşik üstü piksellere atanacak maksimum değer.\n"
    "• Threshold Type: Binary (beyaz-siyah) ya da Binary Inverted (siyah-beyaz).\n\n"
    "📄 Otsu yöntemi, ideal eşiği otomatik olarak belirler.\n"
    "📄 Sadece gri seviye görüntülerle çalışır.\n\n"
    "———————————————\n\n"
    "📌 Otsu Thresholding: cv2.threshold + THRESH_OTSU\n\n"
    "• Max Value: Maximum value to assign to thresholded pixels.\n"
    "• Threshold Type: Binary or Binary Inverted.\n\n"
    "📄 Otsu's method automatically computes the optimal threshold.\n"
    "📄 Works only on grayscale images."
)


    def create_widgets(self):
        
        tk.Label(self.frame, text="OTSU Threshold:").grid(row=1, column=0, padx=2, pady=2)
        self.otsu_threshold_label = tk.Label(self.frame)
        self.otsu_threshold_label.grid(row=1, column=1, padx=2, pady=2)
        
        self.info_buttom = ImageButtonApp(self.frame, text= OtsuThresholdFrame.info_text)
        
    def apply(self, img):
        # Griye çevir (gerekiyorsa)
        if len(img.shape) == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img.copy()

        # Otsu'nun yöntemini uygula, yalnızca eşik değeri döndürülür
        otsu_thresh_value, _ = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        return int(otsu_thresh_value)
    
    def update_result(self, img):
        threshold = self.apply(img)
        self.otsu_threshold_label.config(text=str(threshold))
    
#! Needed update for contours    
class FindContoursFrame(ProcessFrameBase):
    name = "Find Contours"
    info_text = (
    "📌 Kenar Bulma (FindContours): cv2.findContours\n\n"
    "• Retrieval Mode:\n"
    "   - RETR_EXTERNAL: Sadece dış konturları bulur.\n"
    "   - RETR_LIST: Tüm konturları düz bir liste olarak verir.\n"
    "   - RETR_TREE: Konturların hiyerarşisini verir.\n\n"
    "• Approximation Method:\n"
    "   - CHAIN_APPROX_SIMPLE: Gereksiz noktaları atar (daha hafif).\n"
    "   - CHAIN_APPROX_NONE: Tüm noktaları döndürür.\n\n"
    "📄 Giriş görseli griye çevrilir ve ardından ikili eşikleme uygulanır.\n\n"
    "———————————————\n\n"
    "📌 Contour Detection (FindContours): cv2.findContours\n\n"
    "• Retrieval Mode:\n"
    "   - RETR_EXTERNAL: Retrieves only external contours.\n"
    "   - RETR_LIST: Retrieves all contours without hierarchy.\n"
    "   - RETR_TREE: Retrieves all contours and reconstructs hierarchy.\n\n"
    "• Approximation Method:\n"
    "   - CHAIN_APPROX_SIMPLE: Compresses segments to save memory.\n"
    "   - CHAIN_APPROX_NONE: Stores all contour points.\n\n"
    "📄 Input image is converted to grayscale and thresholded to binary."
)

    def create_widgets(self):
        # Combobox for contour retrieval mode (e.g., external or all)
        tk.Label(self.frame, text="Retrieval Mode:").grid(row=1, column=0, padx=2, pady=2)
        self.retrieval_mode_combobox = ttk.Combobox(self.frame, values=['RETR_EXTERNAL', 'RETR_LIST', 'RETR_TREE'])
        self.retrieval_mode_combobox.grid(row=1, column=1, padx=2, pady=2)

        # Combobox for contour approximation method (e.g., simple or accurate)
        tk.Label(self.frame, text="Approximation Method:").grid(row=2, column=0, padx=2, pady=2)
        self.approximation_method_combobox = ttk.Combobox(self.frame, values=['CHAIN_APPROX_SIMPLE', 'CHAIN_APPROX_NONE'])
        self.approximation_method_combobox.grid(row=2, column=1, padx=2, pady=2)

        tk.Label(self.frame, text="Color:").grid(row=3, column=0, padx=2, pady=2)
        self.color_combobox = ttk.Combobox(self.frame, values=["Red", "Green", "Blue"])
        self.color_combobox.grid(row=3, column=1, padx=2, pady=2)

        self.info_buttom = ImageButtonApp(self.frame, text= FindContoursFrame.info_text)

    def apply(self, img):
        # Get user selections for retrieval mode and approximation method
        retrieval_mode = self.retrieval_mode_combobox.get()
        approximation_method = self.approximation_method_combobox.get()
        color = self.color_combobox.get()
        
        colors = {
            "Blue": (255, 0, 0),
            "Green": (0, 255, 0),
            "Red": (0, 0, 255)
            }
        
        # Convert to grayscale if needed
        if len(img.shape) == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img.copy()

        # Apply binary thresholding to create a binary image for contour detection
        # _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        # Convert user input into OpenCV constants
        retrieval_mode_cv = getattr(cv2, retrieval_mode)
        approximation_method_cv = getattr(cv2, approximation_method)

        # Find contours in the binary image
        contours, hierarchy = cv2.findContours(gray, retrieval_mode_cv, approximation_method_cv)

        # Draw the contours on the original image
        result_img = img.copy()
        cv2.drawContours(result_img, contours, -1, colors[color], 2)

        return result_img    

class DrawContoursFrame(ProcessFrameBase):
    name = "Draw Contours"
    info_text = (
    "📌 Konturları Çizme (DrawContours): cv2.drawContours\n\n"
    "• Kontur Kalınlığı:\n"
    "   - Kontur çizgilerinin kalınlığını belirtir.\n\n"
    "• Kontur Rengi:\n"
    "   - Seçilen renge göre konturlar çizilir (Yeşil, Kırmızı, Mavi).\n\n"
    "📄 Görsel önce gri tonlamaya dönüştürülür, ardından ikili eşikleme uygulanarak konturlar bulunur.\n\n"
    "———————————————\n\n"
    "📌 Drawing Contours (DrawContours): cv2.drawContours\n\n"
    "• Contour Thickness:\n"
    "   - Specifies the thickness of contour lines.\n\n"
    "• Contour Color:\n"
    "   - Contours are drawn in the selected color (Green, Red, Blue).\n\n"
    "📄 The image is first converted to grayscale, followed by binary thresholding to detect contours."
)


    def create_widgets(self):
        # Entry for contour thickness (thickness of contour lines)
        tk.Label(self.frame, text="Contour Thickness:").grid(row=1, column=0, padx=2, pady=2)
        self.thickness_entry = tk.Entry(self.frame)
        self.thickness_entry.grid(row=1, column=1, padx=2, pady=2)

        tk.Label(self.frame, text="Color:").grid(row=3, column=0, padx=2, pady=2)
        self.color_combobox = ttk.Combobox(self.frame, values=["Red", "Green", "Blue"])
        self.color_combobox.grid(row=3, column=1, padx=2, pady=2)
        
        self.info_buttom = ImageButtonApp(self.frame, text= DrawContoursFrame.info_text)

    def apply(self, img):
        # Get user input for thickness and color
        thickness = int(self.thickness_entry.get())
        color = self.color_combobox.get()

        colors = {
            "Blue": (255, 0, 0),
            "Green": (0, 255, 0),
            "Red": (0, 0, 255)
            }

        # Convert to grayscale if needed
        if len(img.shape) == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img.copy()

        # Find contours
        contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw the contours on the original image
        result_img = img.copy()
        cv2.drawContours(result_img, contours, -1, colors[color], thickness)

        return result_img 
#? Del canny side of houghlines    
class HoughLinesFrame(ProcessFrameBase):
    name = "Hough Line Transform"
    info_text = (
    "📌 Hough Doğrusu Dönüşümü (HoughLines): cv2.HoughLines\n\n"
    "• Rho (Mesafe Çözünürlüğü):\n"
    "   - Çizgilerin depolandığı çözünürlük, genellikle piksel cinsindendir.\n\n"
    "• Theta (Açı Çözünürlüğü):\n"
    "   - Açı çözünürlüğü, genellikle radian cinsindendir.\n\n"
    "• Threshold (Eşik Değeri):\n"
    "   - Algılanan çizgilerin geçmesi gereken minimum puan sayısını belirtir.\n\n"
    "📄 Giriş görüntüsü mutlaka gri seviyeli olmalı ve canny edge detector görüntüsü olmalı.\n\n"
    "———————————————\n\n"
    "📌 Hough Line Transform (HoughLines): cv2.HoughLines\n\n"
    "• Rho (Distance Resolution):\n"
    "   - Specifies the resolution of the accumulator, typically in pixels.\n\n"
    "• Theta (Angle Resolution):\n"
    "   - Specifies the angle resolution, usually in radians.\n\n"
    "• Threshold:\n"
    "   - Defines the minimum number of points required to detect a line.\n\n"
    "📄 The input image must be grayscale and must be a canny edge detector image."
)


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

        self.info_buttom = ImageButtonApp(self.frame, text= HoughLinesFrame.info_text)

    def apply(self, img):
        # Get user input for rho, theta, and threshold
        rho = float(self.rho_entry.get())
        theta = float(self.theta_entry.get())
        threshold = int(self.threshold_entry.get())

        # Convert to grayscale if needed
        # if len(img.shape) == 3:
        #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # else:
        #     gray = img.copy()

        # Apply Canny edge detection to get edges for line detection
        # edges = cv2.Canny(gray, 50, 150, apertureSize=3)

        # Use HoughLines to detect lines
        lines = cv2.HoughLines(img, rho, theta, threshold)

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
    name = "Discrete Fourier Transform (DFT)"
    info_text = (
    "📌 Discrete Fourier Transform (DFT): cv2.dft\n\n"
    "• DFT Boyutu:\n"
    "   - DFT sonucu için görüntü boyutunu belirler. Görüntü gerekirse sıfırlarla doldurulur.\n\n"
    "• Sıfır Frekansını Ortaya Taşı (Evet/Hayır):\n"
    "   - Eğer seçilirse, DFT sonucu sıfır frekans bileşeni spektrumun ortasına kaydırılır.\n\n"
    "📄 Görsel önce gri tonlamaya dönüştürülür, ardından DFT uygulanır ve sıfır frekans bileşeni belirtilen şekilde kaydırılır. Sonuç, genlik değerlerine dönüştürülüp normalleştirilir ve görüntülenir.\n\n"
    "———————————————\n\n"
    "📌 Discrete Fourier Transform (DFT): cv2.dft\n\n"
    "• DFT Size:\n"
    "   - Specifies the size of the DFT result. The image is padded with zeros if necessary.\n\n"
    "• Shift Zero Frequency (Yes/No):\n"
    "   - If selected, shifts the zero frequency component to the center of the spectrum.\n\n"
    "📄 The image is first converted to grayscale, followed by DFT. The zero frequency component is shifted if required, and the result is converted to magnitude and normalized for display."
)


    def create_widgets(self):
        # Entry for the size of the image (size of the DFT result)
        tk.Label(self.frame, text="DFT Size:").grid(row=1, column=0, padx=2, pady=2)
        self.size_entry = tk.Entry(self.frame)
        self.size_entry.grid(row=1, column=1, padx=2, pady=2)

        # Combobox for selecting whether to shift the zero frequency component
        tk.Label(self.frame, text="Shift Zero Frequency (Yes/No):").grid(row=2, column=0, padx=2, pady=2)
        self.shift_combobox = ttk.Combobox(self.frame, values=['Yes', 'No'])
        self.shift_combobox.grid(row=2, column=1, padx=2, pady=2)

        self.info_buttom = ImageButtonApp(self.frame, text= DFTFrame.info_text)

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
    name = "Inverse Discrete Fourier Transform (IDFT)"
    info_text = (
        "📌 Inverse Discrete Fourier Transform (IDFT): cv2.idft\n\n"
        "• IDFT Boyutu:\n"
        "   - IDFT sonucu için görüntü boyutunu belirler. Görüntü gerekirse sıfırlarla doldurulur.\n\n"
        "• Sıfır Frekansını Ortaya Taşı (Evet/Hayır):\n"
        "   - Eğer seçilirse, IDFT sonucu sıfır frekans bileşeni spektrumun ortasına kaydırılır.\n\n"
        "📄 Görsel önce gri seviyeli olmalı ve Canny kenar algılama görüntüsü gereklidir. \n\n"
        " Sonrasında DFT işlemi yapılır ve IDFT uygulanarak görsel geri dönüştürülür. Sıfır frekans bileşeni belirtilen şekilde kaydırılır. Sonuç, genlik değerlerine dönüştürülüp normalleştirilir ve görüntülenir.\n\n"
        "———————————————\n\n"
        "📌 Inverse Discrete Fourier Transform (IDFT): cv2.idft\n\n"
        "• IDFT Size:\n"
        "   - Specifies the size of the IDFT result. The image is padded with zeros if necessary.\n\n"
        "• Shift Zero Frequency (Yes/No):\n"
        "   - If selected, shifts the zero frequency component to the center of the spectrum.\n\n"
        "📄 The image must first be grayscale and Canny edge detection image is required.\n\n" 
        "Then DFT operation is performed and IDFT is applied to transform the image back. Zero frequency component is shifted as specified. The result is converted to amplitude values, normalized and displayed."
        )

    def create_widgets(self):
        
        # Entry for the size of the image (size of the IDFT result)
        tk.Label(self.frame, text="IDFT Size:").grid(row=1, column=0, padx=2, pady=2)
        self.size_entry = tk.Entry(self.frame)
        self.size_entry.grid(row=1, column=1, padx=2, pady=2)

        # Combobox for selecting whether to shift the zero frequency component
        tk.Label(self.frame, text="Shift Zero Frequency (Yes/No):").grid(row=2, column=0, padx=2, pady=2)
        self.shift_combobox = ttk.Combobox(self.frame, values=['Yes', 'No'])
        self.shift_combobox.grid(row=2, column=1, padx=2, pady=2)
        
        self.info_buttom = ImageButtonApp(self.frame, text= IDFTFrame.info_text)

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
        # edges = cv2.Canny(gray, 50, 150, apertureSize=3)

        # Perform DFT
        dft = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)

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
    name = "Numpy FFT (Fast Fourier Transform)"
    info_text = (
    "📌 Fourier Dönüşümü (FFT) ve Ters Fourier Dönüşümü (IFFT): np.fft.fft2, np.fft.ifft2\n\n"
    "• Dönüşüm Tipi:\n"
    "   - Görüntüye uygulanacak dönüşüm tipi seçilir: FFT (Fourier Dönüşümü) veya IFFT (Ters Fourier Dönüşümü).\n\n"
    "📄 Görsel önce gri tonlamaya dönüştürülür ve float32 formatına çevrilir. Seçilen dönüşüm türüne göre işlem yapılır:\n"
    "   - FFT: Görüntü Fourier Dönüşümüne uygulanır ve sıfır frekansı merkeze kaydırılır. Sonuç, genlik spektrumu olarak normalleştirilip görüntülenir.\n"
    "   - IFFT: Görüntü önce Fourier Dönüşümüne sonra ise Ters Fourier Dönüşümüne tabi tutulur, bu işlemle görsel geri dönüştürülür ve normalleştirilir.\n\n"
    "———————————————\n\n"
    "📌 Fourier Transform (FFT) and Inverse Fourier Transform (IFFT): np.fft.fft2, np.fft.ifft2\n\n"
    "• Transform Type:\n"
    "   - Select the transformation type to apply on the image: FFT (Fourier Transform) or IFFT (Inverse Fourier Transform).\n\n"
    "📄 The image is first converted to grayscale and then to float32 format. Based on the selected transform type:\n"
    "   - FFT: The image is transformed using the Fourier Transform, and the zero frequency is shifted to the center. The result is the magnitude spectrum, normalized for display.\n"
    "   - IFFT: The image is first transformed by FFT and then by Inverse FFT to reconstruct the original image, normalized for display."
)


    def create_widgets(self):
        # Combobox for selecting FFT or IFFT
        tk.Label(self.frame, text="Transform Type:").grid(row=1, column=0, padx=2, pady=2)
        self.transform_combobox = ttk.Combobox(self.frame, values=["FFT", "IFFT"])
        self.transform_combobox.grid(row=1, column=1, padx=2, pady=2)

        self.info_buttom = ImageButtonApp(self.frame, text= NumpyFFTFrame.info_text)

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

class EqualizeHistFrame(ProcessFrameBase):
    name = "Histogram Equalization"
    info_text = (
    "📌 Histogram Eşitleme (EqualizeHist): cv2.equalizeHist\n\n"
    "• Görüntü Gri Tonlamaya Dönüştürülür:\n"
    "   - Eğer giriş görseli renkli ise, önce gri tonlamaya dönüştürülür.\n\n"
    "• Histogram Eşitleme:\n"
    "   - Görüntüdeki parlaklık değerlerinin dağılımını eşitlemek için histogram eşitleme uygulanır.\n"
    "   - Bu işlem, görselin kontrastını artırarak daha iyi görsel detaylar elde edilmesini sağlar.\n\n"
    "📄 Histogram eşitleme, genellikle daha iyi görsel kontrastı elde etmek ve parlaklık seviyelerini dengelemek için kullanılır.\n\n"
    "———————————————\n\n"
    "📌 Histogram Equalization (EqualizeHist): cv2.equalizeHist\n\n"
    "• Grayscale Conversion:\n"
    "   - If the input image is colored, it is first converted to grayscale.\n\n"
    "• Histogram Equalization:\n"
    "   - Histogram equalization is applied to equalize the distribution of pixel intensities.\n"
    "   - This enhances the contrast and improves visual details in the image.\n\n"
    "📄 Histogram equalization is commonly used to improve image contrast and balance brightness levels."
)

    
    def create_widgets(self):
        self.info_buttom = ImageButtonApp(self.frame, text= EqualizeHistFrame.info_text)
    
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
#! may be malfunctioning
class CLAHEFrame(ProcessFrameBase):
    name = "CLAHE (Contrast Limited Adaptive Histogram Equalization)"
    info_text = (
    "📌 CLAHE (Contrast Limited Adaptive Histogram Equalization): cv2.createCLAHE\n\n"
    "• Clip Limit:\n"
    "   - Kontrast sınırlamasının derecesini belirtir. Yüksek değerler daha keskin kontrastlar sağlar.\n\n"
    "• Tile Grid Size:\n"
    "   - Eşitleme işlemi için kullanılan bölgesel ızgaranın boyutunu belirtir. Küçük ızgaralar daha ayrıntılı sonuçlar verir.\n\n"
    "📄 CLAHE, özellikle aydınlatma koşullarının düzensiz olduğu görüntülerde kontrastı artırmak için kullanılır.\n\n"
    "———————————————\n\n"
    "📌 CLAHE (Contrast Limited Adaptive Histogram Equalization): cv2.createCLAHE\n\n"
    "• Clip Limit:\n"
    "   - Specifies the contrast limiting factor. Higher values produce sharper contrasts.\n\n"
    "• Tile Grid Size:\n"
    "   - Defines the size of the grid for local histogram equalization. Smaller grid sizes result in more detailed equalization.\n\n"
    "📄 CLAHE is commonly used to improve contrast in images with uneven lighting conditions."
)

    
    def create_widgets(self):
        self.clip_limit = tk.DoubleVar(value=2.0)
        self.tile_grid_size = tk.IntVar(value=8)
        
        self.info_buttom = ImageButtonApp(self.frame, text= CLAHEFrame.info_text)
        
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