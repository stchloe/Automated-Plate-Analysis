import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read image
img = cv2.imread(r"C:\TeamProject\Automated-Plate-Analysis\DataCleaning\met0_125.jpg",
                 cv2.IMREAD_REDUCED_GRAYSCALE_4)

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

# Apply thresholding to convert to binary
ret, thresh = cv2.threshold(img, 70, 255, 0)

# Apply Canny edge detection
edges = cv2.Canny(thresh, threshold1=150, threshold2=200)

# find the non-zero min-max coords of canny
pts = np.argwhere(edges > 0)
y1, x1 = pts.min(axis=0)
y2, x2 = pts.max(axis=0)

# crop the region
cropped = edges[y1:y2, x1:x2]
cv2.imwrite("cropped.png", cropped)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
cv2.drawContours(img_rgb, contours, -1, (0, 255, 0), 3)

# Draw rectangle around original image
tagged = cv2.rectangle(img_rgb.copy(), (x1, y1), (x2, y2), (255, 0, 0), 3, cv2.LINE_AA)
cv2.imshow("tagged", tagged)
cv2.waitKey()

plt.subplot(121), plt.imshow(tagged ), plt.title('Greyscale Image with Bounding Box and Contours')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cropped, cmap='gray'), plt.title('Binary Cropped Image')
plt.xticks([]), plt.yticks([])
plt.show()
