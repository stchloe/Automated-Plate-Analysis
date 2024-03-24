import os
import cv2
from cropImage import crop_image
from maskImage import mask_circle

# Path to the folder containing the input images
input_folder = r"C:\TeamProject\Automated-Plate-Analysis\DataCleaning\RawImages\Vancomycin"

# Path to the folder where the standardized and compressed images will be saved
output_folder = r"C:\TeamProject\Automated-Plate-Analysis\DataCleaning\CleanImages\Vancomycin"

# Target size in bytes
target_size_bytes = 205 * 1024

# Iterate through all files in the input folder
for filename in os.listdir(input_folder):
    # Read image
    img_path = os.path.join(input_folder, filename)
    img = cv2.imread(img_path)

    # Crop image
    ROI = crop_image(img)

    # Define the center and radius of the circle
    center = (ROI.shape[1] // 2, ROI.shape[0] // 2)  # Center of the image
    radius = min(ROI.shape[0], ROI.shape[1]) // 2  # Radius of the circle

    # Crop the image as a circle
    cropped_circle = mask_circle(ROI, center, radius)

    # Compress image to target size
    quality = 90  # Initial quality
    encoded_img = cv2.imencode('.jpg', cropped_circle, [cv2.IMWRITE_JPEG_QUALITY, quality])[1]
    current_size_bytes = len(encoded_img.tobytes())

    while current_size_bytes > target_size_bytes and quality >= 0:
        quality -= 5
        encoded_img = cv2.imencode('.jpg', cropped_circle, [cv2.IMWRITE_JPEG_QUALITY, quality])[1]
        current_size_bytes = len(encoded_img.tobytes())

    # Decode the compressed image
    compressed_img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)

    # Save the compressed image
    output_path = os.path.join(output_folder, filename)
    cv2.imwrite(output_path, compressed_img)

print("Compression complete. Compressed images saved to", output_folder)
