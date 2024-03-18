import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Read the image
img = cv.imread(r'C:\TeamProject\Automated-Plate-Analysis\DataCleaning\SampleImage001.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

# Convert BGR to RGB
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Convert to grayscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Create the sharpening kernel
sobel_kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Sharpen the image
sharpened_image = cv.filter2D(grey, -1, sobel_kernel_x, sobel_kernel_y)

# Apply Canny edge detection
edges = cv.Canny(sharpened_image, threshold1=150, threshold2=200)

# Find contours
contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
cv.drawContours(img_rgb, contours, -1, (0, 255, 0), 3)

plt.subplot(121), plt.imshow(img_rgb), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(sharpened_image, cmap='gray'), plt.title('Grayscale')
plt.xticks([]), plt.yticks([])
plt.show()
