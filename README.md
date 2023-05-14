Image Resizer Script:
This script resizes all images inside a specified folder, maintaining their aspect ratios, and saves the resized images in a new folder. The maximum dimensions (width, height) of the resized images can be set using the max_size variable. This script uses the Pillow library for image processing.

Usage:
Install the Pillow library using pip install Pillow.
Set the public_folder variable to the path of the folder containing the images you want to resize.
Set the output_folder variable to the path of the folder where you want to save the resized images. The script will create this folder if it does not exist.
Set the max_size variable to a tuple containing the maximum width and height of the resized images (e.g., (800, 800)).
Run the script using python resize_images.py (assuming the script is saved as resize_images.py).

Image to Base64 Converter Script:
This script converts images in a specified folder to base64-encoded strings and saves the encoded data to a text file. The script supports common image formats such as PNG, JPG, JPEG, GIF, and BMP.

Usage:
Set the public_folder variable to the path of the folder containing the images you want to convert.
Set the output_file variable to the path of the text file where you want to save the base64-encoded data. The script will create this file if it does not exist.
Run the script using python image_to_base64.py (assuming the script is saved as image_to_base64.py).
