import cv2
import numpy as np

# converts image to greyscale, converts to binary, applies edge detection and finds coordinates to crop image
# NB manual cropping most likely required for a couple of images


def crop_image(img):
    # Convert to grayscale
    grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Define the kernel size for Gaussian blur (should be odd)
    kernel_size = (25, 25)  # Adjust kernel size as needed

    # Apply Gaussian blur - needed to crop to exact petri dish size
    blurred_image = cv2.GaussianBlur(grey, kernel_size, 0)

    # Apply thresholding to convert to binary
    ret, thresh = cv2.threshold(blurred_image, 55, 255, 0)

    # Apply Canny edge detection
    edges = cv2.Canny(thresh, threshold1=150, threshold2=200)

    # Find the non-zero min-max coordinates of canny
    pts = np.argwhere(edges > 0)
    y1, x1 = pts.min(axis=0)
    y2, x2 = pts.max(axis=0)

    # Crop ROI for original image
    cropped = blurred_image[y1:y2, x1:x2]

    return cropped
