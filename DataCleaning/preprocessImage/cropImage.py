import cv2
import numpy as np

def crop_image(img):
    # Convert to grayscale
    grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Define the kernel size for Gaussian blur (should be odd)
    kernel_size = (101, 101)  # Adjust kernel size as needed

    # Apply Gaussian blur - needed to crop to exact petri dish size
    blurred_image = cv2.GaussianBlur(grey, kernel_size, 0)

    # Apply thresholding to convert to binary
    ret, thresh = cv2.threshold(blurred_image, 55, 255, 0)

    # Apply Canny edge detection
    edges = cv2.Canny(thresh, threshold1=200, threshold2=210)

    # Find the non-zero min-max coordinates of canny
    pts = np.argwhere(edges > 0)
    y1, x1 = pts.min(axis=0)
    y2, x2 = pts.max(axis=0)

    # Ensure the width and height of the cropped region are equal
    width = max(x2 - x1, y2 - y1)
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    x1 = center_x - width // 2
    x2 = center_x + width // 2
    y1 = center_y - width // 2
    y2 = center_y + width // 2

    # Crop ROI for original image - not blurred
    cropped = grey[y1:y2, x1:x2]

    return cropped
