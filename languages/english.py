# Copyright 2025 Said Emirhan Döke
# Licensed under the Apache License, Version 2.0
translations = {
    "ThresholdingFrame": "📌 Threshold Information\n\n"
        "Input Image: Must be a grayscale image. It can also work on colored images, but the best results are obtained with **grayscale** images.\n"
        "Output Image: Returns as a binary image\n\n"
        "• Threshold: A value between 0 and 255. This threshold value is used to binarize the pixels in the image.\n\n"
        "• Threshold Type:\n"
        "  - Binary: Pixel value is set to 255 (white) if greater than the threshold, otherwise 0 (black).\n"
        "  - Binary Inverse: Pixel value is set to 0 (black) if greater than the threshold, otherwise 255 (white).\n\n",
        
    "GaborFilterFrame": "📌 Gabor Filter Parameters\n\n"
        "Input Image: Must be a grayscale image. It can also work on colored images, but the best results are obtained with **grayscale** images.\n"
        "Output Image: Returns a grayscale image with the Gabor filter applied.\n\n"
        "• Ksize: Kernel size. Must be a positive odd number. E.g., 3, 5, 7...\n"
        "• Sigma: Standard deviation of the Gaussian distribution. Typical range: 1.0 - 10.0\n"
        "• Theta: Orientation of the filter (in radians). A value between 0 and pi.\n"
        "• Lambda: Wavelength of the sinusoidal component. Must be positive. E.g., 4.0\n"
        "• Gamma: Aspect ratio. Typically between 0 and 1. 1: circular, <1: elliptical.\n"
        "• Phi: Phase offset. Can take values between 0 and 2*pi.\n\n"
        "🎯 Note: Works better with grayscale images.",
        
    "MorphologicalFrame": "📌 Morphological Operations Parameters\n\n"
        "Input Image: Must be a grayscale image. It can also work on colored images, but the best results are obtained with **grayscale** images.\n"
        "Output Image: Returns a grayscale or colored image with morphological operations applied.\n\n"
        "• Kernel Size: Size of the structural element. Must be a positive odd number. E.g., 3, 5, 7...\n"
        "• Kernel Shape: Shape of the kernel. Can be Rectangular, Ellipse, or Cross.\n"
        "• Operations: Select the morphological operation to apply:\n"
        "  - Erode: Shrinks objects.\n"
        "  - Dilation: Expands objects.\n"
        "  - Opening: Noise removal (erode followed by dilation).\n"
        "  - Closing: Closes small gaps (dilation followed by erode).\n"
        "  - Gradient: Extracts edges (dilation - erode).\n"
        "  - Top Hat: Original image - Opening result.\n"
        "  - Black Hat: Closing result - Original image.\n"
        "• Iterations: Specifies how many times the operation will be applied. Typically 1-5.\n\n"
        "🎯 Note: More effective results are obtained with grayscale images.",
        
    "GammaTransformFrame": "📌 Gamma Transformation Parameters\n\n"
        "Input Image: Works on both grayscale and colored images.\n"
        "Output Image: Returns a grayscale or colored image with gamma transformation applied.\n\n"
        "• Gamma Value: A positive value that adjusts the brightness of the image. Typically between 0.1 and 5.0.\n"
        "  - Gamma < 1: The image darkens (darker).\n"
        "  - Gamma > 1: The image brightens (lighter).\n\n"
        "🎯 Note: Can change the contrast of the image, but extreme values may cause visual distortions.",
        
    "CannyEdgeDetectorFrame": "📌 Canny Edge Detection Parameters\n\n"
        "Input Image: Must be a grayscale image.\n"
        "Output Image: Returns a grayscale image with Canny edge detection applied.\n\n"
        "• Kernel Size: Size of the Canny detection kernel. Must be a positive odd number. E.g., 3, 5, 7...\n"
        "• Low Threshold: The lower threshold value in the Canny algorithm. Must be between 0 and 255.\n"
        "• Max Threshold: The upper threshold value in the Canny algorithm. Must be between 0 and 255.\n"
        "• L2gradient: A Boolean parameter for more precision in edge gradient calculation. Specifies whether to use the L2 norm.\n\n"
        "🎯 Note: A lower threshold value detects edges more sensitively. A higher threshold value captures only prominent edges.\n\n",
        
    "HoughTransformFrame": "📌 Circle Detection with Hough Transform Parameters\n\n"
        "Input Image: Must be a grayscale image.\n"
        "Output Image: Returns a **colored** image with circle detection applied using Hough Transform.\n\n"
        "• Dp: Resolution parameter used in the Hough transform. Typically 1.0 or greater.\n"
        "• Minimum Distance: Minimum distance between detected circles. Must be a positive integer.\n"
        "• Param1: High threshold value in the Canny edge detection algorithm. Must be between 0 and 255.\n"
        "• Param2: Threshold value required to detect circle centers. Must be between 0 and 100.\n"
        "• Minimum Radius: Minimum radius of the circles to be detected.\n"
        "• Maximum Radius: Maximum radius of the circles to be detected.\n"
        "• Mark Color: Color used to mark the detected circles.\n"
        "🎯 Note: For clear circle detection, the input image should have high contrast and clarity.",
        
    "GaussianBlurFrame": "📌 Gaussian Blur Parameters\n\n"
        "Input Image: Can be either colored or grayscale.\n"
        "Output Image: Returns a grayscale or colored image with Gaussian blur applied.\n\n"
        "• Kernel Size: Kernel size of the Gaussian blur filter. Must be a positive odd number. E.g., 3, 5, 7...\n"
        "• Sigma_X: Standard deviation along the X-axis. Must be a positive number.\n"
        "• Sigma_Y: Standard deviation along the Y-axis. Must be a positive number.\n\n"
        "🎯 Note: Gaussian blur is used to reduce noise and smooth the image.",
        
    "KitterIllingworthFrame": "📌 Kittler-Illingworth Optimal Threshold Parameters\n\n"
        "Input Image: Must be a grayscale image.\n"
        "Output Image: Returns the optimal threshold value calculated using the Kittler-Illingworth method. The previous operation's image is returned but not displayed.\n\n"
        "• Optimum Threshold: The optimal threshold value based on the Kittler-Illingworth method.\n"
        "• The Kittler-Illingworth method finds the threshold value that separates the two classes (background and foreground) in the image histogram.\n"
        "• This method determines the threshold value that minimizes the cost considering the variances of the classes.\n\n"
        "🎯 Note: The Kittler-Illingworth method works better on images where bright and dark regions are clearly separated.",
        
    "DrawHistogramFrame": "📌 Image Histogram Drawing Parameters\n\n"
        "Input Image: Can be either colored or grayscale.\n"
        "Output Image: Returns the histogram graph. The previous operation's image is returned but not displayed.\n\n"
        "• Image Histogram: A graph showing the color intensity distribution of pixels in the image.\n"
        "• The histogram is used to analyze the distribution of different color intensities in the image.\n"
        "• This process calculates the frequencies for each pixel's grayscale value and creates a histogram.\n\n"
        "🎯 Note: Histogram analysis is useful for determining contrast, brightness adjustments, or image enhancement techniques.",
        
    "ColorConvertFrame": "📌 Color Conversion Parameters\n\n"
        "• RGB to Grayscale: Converts a colored image to grayscale. Each pixel's grayscale value is calculated.\n"
        "• Grayscale to RGB: Converts a grayscale image to a colored (RGB) image. However, the original color information is lost.\n"
        "• RGB to HSV: Converts a colored image into its Hue, Saturation, and Value components.\n"
        "• HSV to RGB: Converts an HSV image back to Red-Green-Blue (RGB) format.\n\n"
        "🎯 Note: Choose the appropriate color conversion for image processing and color analysis.",
        
    "ResizeFrame": "📌 Image Resizing Parameters\n\n"
        "Input Image: Can be either colored or grayscale.\n"
        "Output Image: Returns a resized grayscale or colored image.\n\n"
        "• Width: The new width of the image. Must be a positive integer.\n"
        "• Height: The new height of the image. Must be a positive integer.\n\n"
        "🎯 Note: Resizing the image may distort the aspect ratio unless explicitly maintained.",
        
    "RotateFrame": "📌 Image Rotation Parameters\n\n"
        "Input Image: Can be either colored or grayscale.\n"
        "Output Image: Returns a rotated grayscale or colored image.\n\n"
        "• Rotation Angle: The angle by which the image will be rotated. Options: 90°, 180°, 270°.\n\n"
        "🎯 Note: The selected rotation angle rotates the image clockwise.",
        
    "FlipFrame": "📌 Image Flipping Parameters\n\n"
        "Input Image: Can be either colored or grayscale.\n"
        "Output Image: Returns a flipped grayscale or colored image.\n\n"
        "• Flip Direction: Specifies the direction to flip the image. Options: Horizontal, Vertical, Both.\n\n"
        "🎯 Note: Horizontal flip reverses the image left-to-right; vertical flip reverses it top-to-bottom. Both flips apply both transformations.",
        
    "MedianBlurFrame": "📌 Median Blur Parameters\n\n"
        "Input Image: Can be either colored or grayscale.\n"
        "Output Image: Returns a grayscale or colored image with median blur applied.\n\n"
        "• Kernel Size: The kernel size used in the median blur algorithm. Typically odd numbers (e.g., 3, 5, 7).\n\n"
        "🎯 Note: Increasing the kernel size results in more blurring but may also reduce details. Useful for smoothing noise in images.",
        
    "BilateralFilterFrame": "📌 Bilateral Filter Parameters\n\n"
        "Input Image: Can be either colored or grayscale.\n"
        "Output Image: Returns a grayscale or colored image with bilateral filtering applied.\n\n"
        "• Diameter: Diameter of the pixel neighborhood used during filtering. Must be a positive integer.\n"
        "• Sigma Color: Standard deviation in the color space. Higher values mean more influence from similar colors.\n"
        "• Sigma Space: Standard deviation in the coordinate space. Higher values mean more influence from distant pixels.\n\n"
        "🎯 Note: Bilateral filtering is ideal for reducing noise while preserving edges.",
        
    "Filter2DFrame": "📌 filter2D Convolution Parameters\n\n"
        "Input Image: Can be either colored or grayscale.\n"
        "Output Image: Returns a grayscale or colored image with convolution applied.\n\n"
        "• 3x3 Kernel: Specifies the kernel values to apply on the image.\n"
        "  These values determine how neighboring pixels are combined during convolution.\n"
        "  Examples include edge detection, blurring, or sharpening kernels.\n\n"
        "🎯 Note: Clear and high-contrast input images yield more noticeable convolution effects.",
        
    "SobelFrame": "📌 Sobel Edge Detection Parameters\n\n"
        "Input Image: Works on colored images as well, but the best results are obtained with **grayscale** images.\n"
        "Output Image: Returns a grayscale or colored image with Sobel edge detection applied.\n\n"
        "• dx: Specifies whether to compute the derivative in the x-direction. 1 detects horizontal edges.\n"
        "• dy: Specifies whether to compute the derivative in the y-direction. 1 detects vertical edges.\n"
        "• Kernel Size: The kernel size used in the Sobel filter. Must be a positive odd number (e.g., 1, 3, 5).\n\n"
        "🎯 Note: If both dx and dy are set to 1, both horizontal and vertical edges are detected.",
        
    "ScharrFrame": "📌 Scharr Edge Detection Parameters\n\n"
        "Input Image: Must be a grayscale image. Works on colored images as well, but the best results are obtained with **grayscale** images.\n"
        "Output Image: Returns a grayscale or colored image with Scharr edge detection applied.\n\n"
        "• dx: Specifies whether to compute the derivative in the x-direction. 1 detects horizontal edges.\n"
        "• dy: Specifies whether to compute the derivative in the y-direction. 1 detects vertical edges.\n\n"
        "🎯 Note: The Scharr filter provides more accurate results than the Sobel filter, especially for small kernel sizes (e.g., 3x3).",
        
    "LaplacianFrame": "📌 Laplacian Edge Detection Parameters\n\n"
        "Input Image: Must be a grayscale image. Works on colored images as well, but the best results are obtained with **grayscale** images.\n"
        "Output Image: Returns a grayscale or colored image with Laplacian edge detection applied.\n\n"
        "• Kernel Size: The kernel size used for computing the derivative. Must be a positive odd number (e.g., 1, 3, 5).\n\n"
        "🎯 Note: The Laplacian operator detects edges symmetrically by using the second derivative of the image.",
        
    "CornerHarrisFrame": "📌 Harris Corner Detection Parameters\n\n"
        "Input Image: Must be a grayscale image. Works on colored images as well, but the best results are obtained with **grayscale** images.\n"
        "Output Image: Returns a colored image with Harris corner detection applied.\n\n"
        "• Block Size: The size of the neighborhood considered for corner detection.\n"
        "• Sobel Kernel Size: The size of the Sobel filter used for derivative computation.\n"
        "• k Value: Free parameter in the Harris equation (typically between 0.04 and 0.06).\n\n"
        "🟥 High response areas are marked in red, indicating potential corners.",
        
    "GoodFeaturesToTrackFrame": "📌 Corner Detection: goodFeaturesToTrack\n\n"
        "Input Image: Must be a grayscale image.\n"
        "Output Image: Returns a colored image with corner detection applied.\n\n"
        "• Max Corners: The maximum number of corners to detect.\n"
        "• Quality Level: The minimum quality threshold for detected corners (between 0 and 1).\n"
        "• Min Distance: The minimum distance between detected corners (in pixels).\n\n"
        "🟢 Detected corners are marked with green circles.",
        
    "AdaptiveThresholdFrame": "📌 Adaptive Thresholding: adaptiveThreshold\n\n"
        "Input Image: Must be a grayscale image.\n"
        "Output Image: Returns a grayscale image with adaptive thresholding applied.\n\n"
        "• Max Value: The maximum value assigned to pixels above the threshold.\n"
        "• Adaptive Method: Local mean (Mean) or Gaussian-weighted mean (Gaussian).\n"
        "• Threshold Type: Binary (black and white) or Binary Inverted (white and black).\n"
        "• Block Size: The size of the neighborhood used for thresholding (must be an odd number >1).\n"
        "• C: A constant subtracted from the mean or weighted mean.\n\n"
        "📄 This operation works only on grayscale images.",
        
    "OtsuThresholdFrame": "📌 Otsu Thresholding: cv2.threshold + THRESH_OTSU\n\n"
        "Input Image: Must be a grayscale image.\n"
        "Output Image: Returns the optimal Otsu threshold. The previous operation's image is returned but not displayed.\n\n"
        "• Max Value: The maximum value assigned to pixels above the threshold.\n"
        "• Threshold Type: Binary (black and white) or Binary Inverted (white and black).\n\n"
        "📄 The Otsu method automatically determines the ideal threshold.\n"
        "📄 Works only on grayscale images.",
        
    "FindContoursFrame": "📌 Contour Detection (FindContours): cv2.findContours\n\n"
        "Input Image: Must be a grayscale image with prior edge detection (Canny Edge Detection is recommended).\n"
        "Output Image: Returns a colored image with detected contours.\n\n"
        "• Retrieval Mode:\n"
        "   - RETR_EXTERNAL: Retrieves only the external contours.\n"
        "   - RETR_LIST: Retrieves all contours as a flat list.\n"
        "   - RETR_TREE: Retrieves contours with hierarchy.\n\n"
        "• Approximation Method:\n"
        "   - CHAIN_APPROX_SIMPLE: Compresses horizontal, vertical, and diagonal segments.\n"
        "   - CHAIN_APPROX_NONE: Stores all contour points.\n\n",
        
    "DrawContoursFrame": "📌 Drawing Contours (DrawContours): cv2.drawContours\n\n"
        "Input Image: Must be a grayscale image with prior edge detection (Canny Edge Detection is recommended).\n"
        "Output Image: Returns a colored image with drawn contours.\n\n"
        "• Contour Thickness:\n"
        "   - Specifies the thickness of the contour lines.\n\n"
        "• Contour Color:\n"
        "   - Specifies the color used to draw the contours.\n\n",
        
    "HoughLinesFrame": "📌 Hough Line Transform (HoughLines): cv2.HoughLines\n\n"
        "Input Image: Must be a grayscale image with prior edge detection (Canny Edge Detection is recommended).\n"
        "Output Image: Returns a colored image with Hough line transform applied.\n\n"
        "• Rho (Distance Resolution):\n"
        "   - The resolution of the accumulator in pixels.\n\n"
        "• Theta (Angle Resolution):\n"
        "   - The resolution of the accumulator in radians.\n\n"
        "• Threshold:\n"
        "   - The minimum number of intersections required to detect a line.\n\n",
        
    "DFTFrame": "📌 Discrete Fourier Transform (DFT) Parameters\n\n"
        "The image is first converted to grayscale, then DFT is applied. The result is normalized and displayed as a magnitude spectrum.",
        
    "NumpyFFTFrame": "📌 Fourier Transform (FFT) and Inverse Fourier Transform (IFFT) Parameters\n\n"
        "Input Image: Must be a grayscale image.\n\n"
        "Output Image: Returns a grayscale image with FFT or IFFT applied.\n"
        "• Transformation Type: Select the type of transformation to apply: FFT (Fourier Transform) or IFFT (Inverse Fourier Transform).\n\n"
        "🎯 Note: The image is converted to float32 format. Depending on the selected transformation:\n"
        "  - FFT: The image undergoes Fourier Transform, and the zero frequency is shifted to the center. The result is displayed as a magnitude spectrum.\n"
        "  - IFFT: The image undergoes Fourier Transform followed by Inverse Fourier Transform to reconstruct the image.",
        
    "EqualizeHistFrame": "📌 Histogram Equalization (EqualizeHist) Parameters\n\n"
        "Input Image: Must be a grayscale image.\n"
        "Output Image: Returns a histogram-equalized grayscale image.\n\n"
        "• Histogram Equalization: Enhances the contrast of the image by redistributing pixel intensity values.\n\n"
        "🎯 Note: Histogram equalization is commonly used to improve visual contrast and balance brightness levels.",
        
    "CLAHEFrame": "📌 CLAHE (Contrast Limited Adaptive Histogram Equalization) Parameters\n\n"
        "Input Image: Can be either colored or grayscale.\n"
        "Output Image: Returns a grayscale or colored image with CLAHE applied.\n\n"
        "• Clip Limit: Specifies the degree of contrast limiting. Higher values result in sharper contrasts.\n"
        "• Tile Grid Size: Specifies the size of the grid for local histogram equalization. Smaller grids yield more detailed results.\n\n"
        "🎯 Note: CLAHE is particularly useful for enhancing contrast in images with uneven lighting conditions.",
    
    "DatasetProcessInfo": "📌 Dataset Processing Steps\n\n"
        "1- Create Process and fill the parameters.\n"
        "2- Select the source folder.\n"
        "3- Select the destination folder.\n"
        "4- Click the **Prepare Dataset** button.",
    
    "Msezgin_MultiThresholdingFrame": "📌 Multi-Thresholding Parameters\n\n"
        "Input Image: Must be a grayscale image.\n"
        "Output Image: Returns input image.",
    
    "Settings_Title": "Settings",
    
    "User_Settings": "User Settings",
    
    "Warning_Label": "If you make changes to the settings, press the 'save' button.",
    
    "Show_Load_Image_Details_Settings": "Show Load Image Details",
    
    "Language_Select_Settings": "Language Select",
    
    "Theme_Select_Settings": "Theme Select",
    
    "Process_Position_Settings": "Process Position",
    
    "Height_Settings": "Height",
    
    "Infinity_One_Lines_Settings": "Infinity One Lines",
    
    "Save_Button_Settings": "Save",
    
    "Dataset_Process_Settings_Title": "Dataset Process Settings",
    
    "Dataset_Process_Settings": "Dataset Process Settings",
    
    "Dataset_Process_Settings_Warning_Label": "If you make changes to the settings, press the 'save' button\n"
        "then click the 'Process Dataset' button.",
        
    "Select_Folder_Layout_Settings": "Select Folder Layout",
    
    "Select_Folder_Layout_Settings_Warning_Label": "Image or subfolder names are not important",
    
    "Process_Dataset_Button": "Process Dataset",
    
    "Save_Button_MessageBox_Title": "Settings Saved",
    
    "Save_Button_MessageBox_Text": "Saved successfully. Please restart the application to apply some changes.",
    
    "Folder_Type_MessageBox_Title": "Warning",
    
    "Folder_Type_MessageBox_Text": "Please select a folder type.",
    
    "Check_Image_Settings": "Check Image Setting",
    
}
