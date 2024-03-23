import cv2
import numpy as np
# Define the function to compress images
def resize_image_to_target_size(img, target_size_kb):
    # Calculate the target size in bytes
    target_size_bytes = target_size_kb * 1024

    # Initialize compression quality
    quality = 90  # Initial guess

    while True:
        # Encode the image to JPEG with the current quality
        _, encoded_img = cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, quality])

        # Check the size of the encoded image
        current_size_bytes = len(encoded_img.tobytes())

        # If the size is within the tolerance, break
        if abs(current_size_bytes - target_size_bytes) < 1000:
            break

        # Adjust the quality based on the difference between current and target size
        quality -= 5 if current_size_bytes > target_size_bytes else -5

    # Decode the compressed image
    compressed_img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)

    return compressed_img
