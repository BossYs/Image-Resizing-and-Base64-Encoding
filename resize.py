import os
from PIL import Image

def resize_image(image_path, max_size, output_folder):
    img = Image.open(image_path)
    img.thumbnail(max_size)
    img.save(os.path.join(output_folder, os.path.basename(image_path)))

public_folder = "public"
output_folder = "resized_images"
max_size = (500, 500)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for root, dirs, files in os.walk(public_folder):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_path = os.path.join(root, file)
            resize_image(image_path, max_size, output_folder)

