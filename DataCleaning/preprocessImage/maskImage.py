import cv2
import numpy as np


def mask_circle(image, center, radius):
    # Create a mask with zeros of same shape as image
    mask = np.zeros_like(image)

    # Create a circular white filled mask with the given center and radius
    cv2.circle(mask, center, radius, (255, 255, 255), -1)

    # Bitwise AND operation to mask the original image
    cropped_image = cv2.bitwise_and(image, mask)

    return cropped_image

