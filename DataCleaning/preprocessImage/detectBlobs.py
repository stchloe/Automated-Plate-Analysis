import cv2
import numpy as np


def detect_and_draw_circles(image_path):
    # Read the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply adaptive histogram equalization
    clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(9, 9))
    adaptive_img = clahe.apply(img)

    # Apply Hough Circle Transform to detect circles - GOLDEN PARAMS !! DETECTS ALL STRAINS !!
    circles = cv2.HoughCircles(adaptive_img, cv2.HOUGH_GRADIENT, dp=1, minDist=168,
                               param1=20, param2=15, minRadius=45, maxRadius=55)

    # Ensure circles were detected
    if circles is not None:
        circles = np.uint16(np.around(circles))

        # Draw circles on the original image
        for circle in circles[0, :]:
            center = (circle[0], circle[1])
            radius = circle[2]
            cv2.circle(img, center, radius, (255, 0, 0), 3)

    else:
        print("No circles detected.")

    # Save the image with circles drawn
    output_path = image_path.replace('.jpg', '_circles.jpg')
    cv2.imwrite(output_path, img)

    return img