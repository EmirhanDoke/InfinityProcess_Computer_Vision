import numpy as np
import cv2
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import Tk
from scipy.signal import argrelextrema
import os
import inspect

def calculate_histogram(image):
    """Calculate normalized histogram of a grayscale image"""
    hist, bins = np.histogram(image.flatten(), bins=256, range=(0, 256))
    total_pixels = image.size
    normalized_hist = hist / total_pixels
    return normalized_hist, bins

def total_correlation(hist, s):
    """Calculate total correlation function for threshold s"""
    P_A = np.sum(hist[:s])
    P_B = np.sum(hist[s:])
    
    if P_A == 0 or P_B == 0:
        return -np.inf
    
    term1 = -np.sum((hist[:s] / P_A) ** 2)
    term2 = -np.sum((hist[s:] / P_B) ** 2)
    
    return term1 + term2

def find_peaks(TC, L=6):
    """Find peaks in the total correlation function using Rule-1"""
    peaks = []
    for n in range(L, len(TC)-L):
        is_peak = True
        for i in range(1, L+1):
            if TC[n] <= TC[n-i] or TC[n] <= TC[n+i]:
                is_peak = False
                break
        if is_peak:
            peaks.append(n)
    return peaks

def plot_all_results(image, hist, bins, TC_values, segmented, peaks):
    
    """Display all results in a single figure"""
    plt.figure(figsize=(20, 10))
    
    # Original Image
    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    
    # Image Histogram
    plt.subplot(2, 2, 2)
    plt.bar(bins[:-1], hist, width=1)
    plt.title('Image Histogram')
    plt.xlabel('Gray Level')
    plt.ylabel('Frequency')
    plt.grid(True)
    
    # TC Function (First Dichotomization)
    plt.subplot(2, 2, 3)
    plt.plot(TC_values, 'b-', label='TC Function')
    for peak in peaks:
        plt.plot(peak, TC_values[peak], 'ro')
        plt.text(peak, TC_values[peak], f' t={peak}', verticalalignment='bottom')
    plt.title('Total Correlation Function (First Dichotomization)')
    plt.xlabel('Gray Level')
    plt.ylabel('Total Correlation')
    plt.grid(True)
    plt.legend()
    
    # Segmented Image
    plt.subplot(2, 2, 4)
    plt.imshow(segmented, cmap='gray')
    plt.title('Segmented Image')
    plt.axis('off')
    
    plt.tight_layout()
    # plt.show()

def calculate_class_variance(hist, t):
    """Calculate variances of two classes created by threshold t"""
    # Class 1: 0 to t-1
    indices1 = np.arange(t)
    omega1 = np.sum(hist[:t])
    if omega1 == 0:
        var1 = 0
    else:
        P1 = hist[:t] / omega1
        mu1 = np.sum(indices1 * P1)
        var1 = np.sum((indices1 - mu1)**2 * P1)
    
    # Class 2: t to 255
    indices2 = np.arange(t, 256)
    omega2 = np.sum(hist[t:])
    if omega2 == 0:
        var2 = 0
    else:
        P2 = hist[t:] / omega2
        mu2 = np.sum(indices2 * P2)
        var2 = np.sum((indices2 - mu2)**2 * P2)
    
    return var1, var2

def calculate_discrepancy(hist, thresholds):
    """Calculate discrepancy measure for current thresholds"""
    k = len(thresholds) + 1
    thresholds = [0] + sorted(thresholds) + [256]
    total_dis = 0
    
    for i in range(k):
        start = thresholds[i]
        end = thresholds[i+1]
        class_hist = hist[start:end]
        omega = np.sum(class_hist)
        
        if omega == 0:
            continue
            
        P = class_hist / omega
        indices = np.arange(start, end)
        mu = np.sum(indices * P)
        var = np.sum((indices - mu)**2 * P)
        total_dis += omega * var
    
    return total_dis

def cost_function(discrepancy, k):
    """Calculate cost function value"""
    return 0.8 * np.sqrt(discrepancy) + (np.log2(k))**2

def find_best_threshold(hist, start, end, peaks=None):
    """Find the best threshold in a given histogram region"""
    # Calculate TC function for the selected region
    region_hist = hist[start:end+1]
    TC = np.zeros(end - start + 1)
    for s in range(1, len(region_hist)):
        TC[s] = total_correlation(region_hist, s)
    
    # Find peaks in TC function
    if peaks is None:
        peaks = find_peaks(TC)
    peaks = [p + start for p in peaks if p + start < end]
    
    if not peaks:
        return None
    
    # Find best threshold among peaks (Method-5 from the paper)
    min_variance = np.inf
    best_threshold = None
    
    for peak in peaks:
        var1, var2 = calculate_class_variance(hist, peak)
        current_min_var = min(var1, var2)
        if current_min_var < min_variance:
            min_variance = current_min_var
            best_threshold = peak
    
    return best_threshold

def select_image_file():
    """Open file dialog to select an image"""
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("Image files", ".jpg;.jpeg;.png;.bmp;*.tif")]
    )
    root.destroy()
    return file_path

def multilevel_thresholding(image):
    """Main function to perform multilevel thresholding"""
    # Select image file
    # image_path = select_image_file()
    # if not image_path:
    #     print("No image selected. Exiting...")
    #     return
    
    # Read input image
    # image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # if image is None:
    #     print("Error: Could not read image")
    #     return
    
    # Calculate normalized histogram
    hist, bins = calculate_histogram(image)
    
    # Calculate TC function for first split
    TC_values = np.zeros(256)
    for s in range(1, 256):
        TC_values[s] = total_correlation(hist, s)
    
    # Find peaks in TC function
    peaks = find_peaks(TC_values)
    
    # Initialize variables
    thresholds = []
    current_regions = [(0, 255)]  # Start with full histogram range
    optimal_k = 1
    min_cost = np.inf
    optimal_thresholds = []
    cost_values = []
    step = 0
    
    # Iterate until cost function reaches minimum
    while True:
        step += 1
        print(f"\nProcessing step {step}...")
        
        # Find region with maximum variance
        max_var = -1
        selected_region = None
        selected_index = -1
        
        for i, (start, end) in enumerate(current_regions):
            if end - start < 2:  # Need at least 2 levels to split
                continue
                
            region_hist = hist[start:end+1]
            omega = np.sum(region_hist)
            if omega == 0:
                continue
                
            P = region_hist / omega
            indices = np.arange(start, end+1)
            mu = np.sum(indices * P)
            var = np.sum((indices - mu)**2 * P)
            
            if var > max_var:
                max_var = var
                selected_region = (start, end)
                selected_index = i
        
        if selected_region is None:
            print("No suitable region found for splitting.")
            break
            
        start, end = selected_region
        
        # For first step, use the peaks we already found
        if step == 1:
            # Filter peaks that are in the current region
            region_peaks = [p for p in peaks if start <= p < end]
            new_threshold = find_best_threshold(hist, start, end, region_peaks)
        else:
            new_threshold = find_best_threshold(hist, start, end)
            
        if new_threshold is None:
            print("No valid threshold found in selected region.")
            break
        
        print(f"Selected threshold at gray level: {new_threshold}")
        
        # Add new threshold and update regions
        thresholds.append(new_threshold)
        thresholds.sort()
        
        # Update current regions
        current_regions.pop(selected_index)
        current_regions.append((start, new_threshold))
        current_regions.append((new_threshold, end))
        current_regions.sort()
        
        # Calculate cost function
        k = len(thresholds) + 1
        discrepancy = calculate_discrepancy(hist, thresholds)
        current_cost = cost_function(discrepancy, k)
        cost_values.append(current_cost)
        
        # Check if we've found a better solution
        if current_cost < min_cost:
            min_cost = current_cost
            optimal_thresholds = thresholds.copy()
            optimal_k = k
            print(f"New optimal cost: {min_cost} with {optimal_k} classes")
        else:
            # Cost increased, we've passed the optimal point
            print("Cost increased - stopping iteration")
            break
    
    print("\nFinal Results:")
    print(f"Optimal number of thresholds: {len(optimal_thresholds)}")
    print(f"Optimal thresholds: {optimal_thresholds}")
    
    # Segment the image using the optimal thresholds
    segmented = np.zeros_like(image)
    thresholds = [0] + optimal_thresholds + [256]
    
    for i in range(len(thresholds) - 1):
        start = thresholds[i]
        end = thresholds[i+1]
        mask = (image >= start) & (image < end)
        
        # Calculate class mean
        class_pixels = image[mask]
        if len(class_pixels) > 0:
            class_mean = np.mean(class_pixels)
        else:
            class_mean = (start + end) / 2
        
        segmented[mask] = class_mean
    
      # Check caller function name
    stack = inspect.stack()
    caller_function_name = stack[1].function
    
    # print(f"Caller function: {caller_function_name}")
    
    if caller_function_name != ["batch_apply_processes","batch_apply_processes_alt"]:
        
        # Display all results in one figure
        plot_all_results(image, hist, bins, TC_values, segmented, peaks)

    return segmented

if __name__ == "__main__":
    multilevel_thresholding()