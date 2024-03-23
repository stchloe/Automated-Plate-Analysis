import cv2
import numpy as np

# Read the image
image_path = r"C:\TeamProject\Automated-Plate-Analysis\DataCleaning\CleanImages\Clindamycin\Clind0.jpg"
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Define the kernel size for Gaussian blur (should be odd)
kernel_size = (25, 25)  # Adjust kernel size as needed

# Apply Gaussian blur - needed to crop to exact petri dish size
blurred_image = cv2.GaussianBlur(img, kernel_size, 0)

# Apply adaptive histogram equalization
clahe = cv2.createCLAHE(clipLimit=1.75, tileGridSize=(10, 10))
adaptive_img = clahe.apply(blurred_image)

# Apply Hough Circle Transform to detect circles - GOLDEN PARAMS !! DETECTS ALL STRAINS !!
circles = cv2.HoughCircles(adaptive_img, cv2.HOUGH_GRADIENT, dp=1, minDist=166,
                           param1=20, param2=16, minRadius=43, maxRadius=55)

# Ensure circles were detected
if circles is not None:
    circles = np.uint16(np.around(circles))

    # List to store the coordinates of the rectangles
    rectangles = []

    # Draw slightly bigger red boxes around the circles
    for circle in circles[0, :]:
        center = (circle[0], circle[1])
        radius = circle[2]

        # Calculate coordinates for the rectangle (add/subtract 5 pixels to each side)
        x, y, w, h = center[0] - radius - 20, center[1] - radius - 20, 2 * radius + 30, 2 * radius + 40

        # Append rectangle coordinates to the list
        rectangles.append((x, y, w, h))

    # Sort the rectangles based on x-coordinate first and then by y-coordinate
    rectangles.sort(key=lambda rect: (rect[1], rect[0]))

    # Save each rectangle as a separate image
    for i, rect in enumerate(rectangles):
        x, y, w, h = rect
        roi = img[y:y+h, x:x+w]
        cv2.imwrite(f"Rectangle_{i+1}.jpg", roi)

else:
    print("No circles detected.")
