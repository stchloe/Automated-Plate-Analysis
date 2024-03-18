import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Read the image
img = cv.imread(r'C:\TeamProject\Automated-Plate-Analysis\DataCleaning\SampleImage001.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"
rsz_img = cv.resize(img, None, fx=0.25, fy=0.25)

# Convert BGR to RGB
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Convert to grayscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Create the sharpening kernel
sobel_kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Sharpen the image
sharpened_image = cv.filter2D(grey, -1, sobel_kernel_x, sobel_kernel_y)

# Detect circles
circles = cv.HoughCircles(sharpened_image, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # draw the outer circle
    cv.circle(sharpened_image, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv.circle(sharpened_image, (i[0], i[1]), 2, (0, 0, 255), 3)

cv.imshow('detected circles', sharpened_image)
cv.waitKey(0)
cv.destroyAllWindows()
