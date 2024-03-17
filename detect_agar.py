import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image_path = r"C:\Users\annie\OneDrive - University of Leeds\Final Year\Team project\Image processing\Lab images\RawPlateImages\RawPlateImages\Clindamycin\0\IMG_6972.jpg"
img = cv2.imread(image_path)

# Display the original image
plt.subplot(3, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
plt.subplot(3, 2, 2)
plt.imshow(gray_img, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# Apply Gaussian blur to reduce noise
blur_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

# Display the blurred image
plt.subplot(3, 2, 3)
plt.imshow(blur_img, cmap='gray')
plt.title('Blurred Image')
plt.axis('off')

# Adaptive thresholding to isolate dark regions
thresh_img = cv2.adaptiveThreshold(blur_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# Display the thresholded image
plt.subplot(3, 2, 4)
plt.imshow(thresh_img, cmap='gray')
plt.title('Thresholded Image')
plt.axis('off')

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours based on area (exclude small regions)
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 1000]  # Adjust area threshold as needed

# Draw contours on the thresholded image
contour_img = cv2.drawContours(cv2.cvtColor(thresh_img, cv2.COLOR_GRAY2BGR), filtered_contours, -1, (0, 255, 0), 3)  # Green contours

# Display the thresholded image with contours
plt.subplot(3, 2, 5)
plt.imshow(cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB))
plt.title('Contours Detected')
plt.axis('off')

# Find the most circular contour
most_circular_contour = max(filtered_contours, key=lambda x: cv2.contourArea(x))

# Get the bounding box of the contour
x, y, w, h = cv2.boundingRect(most_circular_contour)

# Crop the original image using the bounding box
cropped_img = img[y:y+h, x:x+w]

# Display the cropped image
plt.subplot(3, 2, 6)
plt.imshow(cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB))
plt.title('Cropped Image')
plt.axis('off')

plt.tight_layout()
plt.show()
