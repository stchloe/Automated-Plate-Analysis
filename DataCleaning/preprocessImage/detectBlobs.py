import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\TeamProject\Automated-Plate-Analysis\DataCleaning\CleanImages\Clindamycin\Clind0.jpg",
                 cv2.IMREAD_GRAYSCALE)

# Apply thresholding to convert to binary
ret, thresh = cv2.threshold(img, 55, 255, 0)

# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(thresh,
                                    cv2.HOUGH_GRADIENT, 1, 100, param1=40,
                                    param2=12, minRadius=35, maxRadius=55)

# Draw circles that are detected.
if detected_circles is not None:

    # Convert the circle parameters a, b and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        # Draw the circumference of the circle.
        cv2.circle(img, (a, b), r, (0, 0, 255), 2)

        # Draw a small circle (of radius 1) to show the center.
        # cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
        # cv2.imshow("Detected Circle", img)
        # cv2.waitKey(0)

cv2.imwrite("BlobDetection.jpg", img)
