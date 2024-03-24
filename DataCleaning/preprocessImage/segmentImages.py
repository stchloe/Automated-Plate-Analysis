import os
from PIL import Image, ImageDraw

# Function to scale coordinates based on the scaling factor
def scale_coordinates(coordinates, scale_factor):
    scaled_coordinates = []
    for x, y, w, h in coordinates:
        scaled_x = int((x - X_OFFSET) * scale_factor)  # Adjusting the x-coordinate
        scaled_y = int((y - Y_OFFSET) * scale_factor)  # Adjusting the y-coordinate
        scaled_w = int(w * scale_factor)
        scaled_h = int(h * scale_factor)
        scaled_coordinates.append((scaled_x, scaled_y, scaled_w, scaled_h))
    return scaled_coordinates

# Load the original image to get its size
original_image_path = r"C:\TeamProject\Automated-Plate-Analysis\DataCleaning\CleanImages\Clindamycin\Clind0.jpg"
original_image = Image.open(original_image_path)
original_image_size = original_image.size

# Load the image to be segmented to get its size
segmented_image_path = r"C:\TeamProject\Automated-Plate-Analysis\DataCleaning\CleanImages\Clindamycin\Clind64.jpg"
segmented_image = Image.open(segmented_image_path)
segmented_image_size = segmented_image.size

# Calculate scaling factors for both dimensions
scale_factor_x = segmented_image_size[0] / original_image_size[0]
scale_factor_y = segmented_image_size[1] / original_image_size[1]

# Define the coordinates of the rectangles obtained from the original image - in correct order
original_coordinates = [
    (501, 225, 135, 135), (706, 190, 140, 140), (974, 228, 132, 132),
    (1150, 180, 128, 138), (385, 360, 136, 136), (635, 375, 136, 136),
    (869, 401, 126, 126), (1035, 395, 140, 140), (1200, 420, 148, 148),
    (256, 525, 140, 140), (460, 545, 140, 140), (738, 566, 138, 148),
    (965, 561, 124, 134), (1221, 571, 128, 138), (1460, 542, 118, 128),
    (99, 713, 136, 146), (325, 767, 136, 146), (596, 740, 138, 148),
    (844, 746, 118, 128), (1085, 747, 132, 142), (1322, 734, 138, 148),
    (1504, 760, 138, 148), (320, 1150, 138, 148), (560, 1150, 134, 144),
    (870, 1172, 138, 148), (1112, 1178, 126, 136), (1334, 1146, 138, 148)
]

# Define the offset values to move the coordinates
X_OFFSET = 0  # Adjust this value as needed
Y_OFFSET = 0  # Adjust this value as needed

# Scale the coordinates based on the scaling factors
scaled_coordinates = scale_coordinates(original_coordinates, scale_factor_x)

# Create a copy of the segmented image for display with red borders
display_image = segmented_image.copy()
draw = ImageDraw.Draw(display_image)

# Draw rectangles with red borders on the display image
for rect in scaled_coordinates:
    x, y, w, h = rect
    draw.rectangle([x, y, x + w, y + h], outline="red", width=2)

# Display the image with red borders
display_image.show()

# Crop and save each rectangle to the output folder without red borders
output_folder = r"C:\TeamProject\Automated-Plate-Analysis\DataCleaning\CleanImages\Clindamycin\Clind64_Strains"
os.makedirs(output_folder, exist_ok=True)

for i, rect in enumerate(scaled_coordinates):
    x, y, w, h = rect
    cropped_image = segmented_image.crop((x, y, x + w, y + h))
    cropped_image.save(os.path.join(output_folder, f"Strain_{i + 1}.jpg"))
