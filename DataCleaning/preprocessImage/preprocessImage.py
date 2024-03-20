import os
import cv2
import numpy as np

# Path to the folder containing the input images
input_folder = r"C:\TeamProject\Automated-Plate-Analysis\DataCleaning\RawImages\Clindamycin"

# Path to the folder where the standardized images will be saved
output_folder = r"C:\TeamProject\Automated-Plate-Analysis\DataCleaning\CleanImages\Clindamycin"

# Iterate through all files in the input folder
for filename in os.listdir(input_folder):
    # Read image
    img_path = os.path.join(input_folder, filename)
    img = cv2.imread(img_path, cv2.IMREAD_REDUCED_GRAYSCALE_8)

    # Apply thresholding to convert to binary
    ret, thresh = cv2.threshold(img, 55, 255, 0)

    # Apply Canny edge detection
    edges = cv2.Canny(thresh, threshold1=150, threshold2=200)

    # find the non-zero min-max coordinates of canny
    pts = np.argwhere(edges > 0)
    y1, x1 = pts.min(axis=0)
    y2, x2 = pts.max(axis=0)

    # crop the region
    cropped = edges[y1:y2, x1:x2]

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Save the standardized image to the output folder
    output_path = os.path.join(output_folder, filename)
    cv2.imwrite(output_path, cropped)  # Adjust 'cropped' if needed

print("Standardization complete. Standardized images saved to", output_folder)
