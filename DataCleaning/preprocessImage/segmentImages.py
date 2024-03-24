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
segmented_image_path = r"C:\TeamProject\Automated-Plate-Analysis\DataCleaning\CleanImages\Metronidazole\Met32.jpg"
segmented_image = Image.open(segmented_image_path)
segmented_image_size = segmented_image.size

# Calculate scaling factors for both dimensions
scale_factor_x = segmented_image_size[0] / original_image_size[0]
scale_factor_y = segmented_image_size[1] / original_image_size[1]

# Define the coordinates of the rectangles obtained from the original image - in correct order
original_coordinates = [
    (520, 210, 135, 135), (785, 200, 140, 140), (980, 190, 132, 132),
    (1180, 190, 138, 138), (360, 370, 136, 136), (605, 350, 136, 136),
    (875, 350, 126, 126), (1095, 385, 140, 140), (1280, 350, 148, 148),
    (220, 525, 140, 140), (480, 570, 140, 140), (720, 540, 148, 148),
    (975, 540, 124, 134), (1195, 550, 128, 138), (1430, 545, 118, 128),
    (95, 730, 146, 146), (350, 740, 136, 146), (570, 750, 138, 148),
    (860, 770, 118, 118), (1090, 740, 142, 142), (1330, 745, 148, 148),
    (1545, 740, 148, 148), (290, 1200, 148, 148), (530, 1210, 144, 144),
    (840, 1140, 138, 148), (1160, 1090, 136, 136), (1410, 1080, 148, 148)
]

# Define the offset values to move the coordinates
X_OFFSET = 20  # Adjust this value as needed
Y_OFFSET = -30  # Adjust this value as needed

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
output_folder = r"C:\TeamProject\Automated-Plate-Analysis\DataCleaning\CleanImages\Metronidazole\Met32_Strains"
os.makedirs(output_folder, exist_ok=True)

for i, rect in enumerate(scaled_coordinates):
    x, y, w, h = rect
    cropped_image = segmented_image.crop((x, y, x + w, y + h))
    cropped_image.save(os.path.join(output_folder, f"Strain_{i + 1}.jpg"))
