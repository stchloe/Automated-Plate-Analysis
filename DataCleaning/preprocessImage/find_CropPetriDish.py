import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\TeamProject\Automated-Plate-Analysis\DataCleaning\RawImages\Clindamycin\Clind0.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Gaussian Blur to reduce noise
blurred = cv2.GaussianBlur(img, (7, 7), 0)

# Apply adaptive histogram equalization
clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(10, 10))
adaptive_img = clahe.apply(blurred)

# Apply thresholding to convert to binary
ret, thresh = cv2.threshold(adaptive_img, 70, 255, 0)

# Set up the blob detector parameters
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 0

# Filter by Area.
params.filterByArea = True
params.minArea = 300

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.5

# # Filter by Convexity
# params.filterByConvexity = True
# params.minConvexity = 0.2
#
# # Filter by Inertia
# params.filterByInertia = True
# params.minInertiaRatio = 0.01

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs
keypoints = detector.detect(thresh)

# Draw detected blobs as red circles
img_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255),
                                       cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Display the original and equalized images
# cv2.imshow('Original Image', img)
# cv2.imshow('Equalized Image', adaptive_img)
# cv2.waitKey(0)
cv2.imwrite('AdaptiveHist_Binary_BlobDetection_Test.jpg', img_with_keypoints)
# cv2.destroyAllWindows()
