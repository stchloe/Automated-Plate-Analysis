import os
import cv2
import numpy as np
from cropImage import crop_image

# Path to the folder containing the input images
input_folder = r"C:\TeamProject\Automated-Plate-Analysis\DataCleaning\RawImages\Clindamycin"

# Path to the folder where the standardized images will be saved
output_folder = r"C:\TeamProject\Automated-Plate-Analysis\DataCleaning\CleanImages\Clindamycin"

# Iterate through all files in the input folder
for filename in os.listdir(input_folder):
    # Read image
    img_path = os.path.join(input_folder, filename)
    img = cv2.imread(img_path)

    ROI = crop_image(img)

    # Save the standardised image to the output folder
    output_path = os.path.join(output_folder, filename)
    cv2.imwrite(output_path, ROI)  # Adjust 'cropped' if needed

print("Standardization complete. Standardized images saved to", output_folder)
