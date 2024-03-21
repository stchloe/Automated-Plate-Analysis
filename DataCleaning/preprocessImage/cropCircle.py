import cv2
import numpy as np


def crop_image(img):
    # Convert to grayscale
    grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(grey, (5, 5), 0)

    # Apply Hough Circle Transform to detect circles
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                               param1=50, param2=30, minRadius=300, maxRadius=50)

    # Ensure circles were detected
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        # Assume only one circle is detected
        for (x, y, r) in circles:
            # Crop image using circle as a mask
            mask = np.zeros_like(grey)
            cv2.circle(mask, (x, y), r, 255, -1)
            masked_img = cv2.bitwise_and(img, img, mask=mask)

            # Get bounding box of the circle
            x1 = max(0, x - r)
            y1 = max(0, y - r)
            x2 = min(img.shape[1], x + r)
            y2 = min(img.shape[0], y + r)

            # Crop the image using the bounding box
            cropped = masked_img[y1:y2, x1:x2]
            return cropped

    # If no circle is detected, return None
    return None


img = cv2.imread(r"C:\TeamProject\Automated-Plate-Analysis\DataCleaning\RawImages\Clindamycin\Clind0.jpg")
cropped = crop_image(img)
cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
