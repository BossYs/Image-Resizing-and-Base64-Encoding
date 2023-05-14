import os
from PIL import Image

# Function to resize an image and change its bit depth
def resize_image_and_change_bit_depth(image_path, max_size, output_folder, colors=256):
    # Open the image
    img = Image.open(image_path)
    # Resize the image to the specified maximum dimensions
    img.thumbnail(max_size)

    # Convert the image to RGBA mode
    img = img.convert('RGBA')

    # Convert the image to the desired number of colors
    img = img.quantize(colors=colors)

    # Save the resized and color-quantized image to the output folder
    img.save(os.path.join(output_folder, os.path.basename(image_path)))

# Define the input and output folders and the maximum size for resizing
public_folder = "public"
output_folder = "resized_images"
max_size = (500, 500)

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Walk through the input folder and its subfolders
for root, dirs, files in os.walk(public_folder):
    # Loop through the files in the current folder
    for file in files:
        # Check if the file has an image file extension
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Get the full path to the image file
            image_path = os.path.join(root, file)
            # Resize the image and change its bit depth
            resize_image_and_change_bit_depth(image_path, max_size, output_folder)
