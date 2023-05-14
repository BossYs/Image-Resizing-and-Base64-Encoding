<h1>Image Resizing and Base64 Encoding</h1>
This repository contains two Python scripts:

resize.py: Resizes images and reduces their bit depth.
convertImage.py: Converts resized images to base64-encoded data and writes the data to an output file.
Usage
1. Resize and change bit depth of images
Run resize.py to resize images and change their bit depth:

bash
python resize.py
The script processes images in the public folder, resizes them to a maximum size of 500x500 pixels, and reduces their bit depth to 256 colors. 
The resized images are saved in the resized_images folder.

2. Convert resized images to base64
Run convertImage.py to convert the resized images to base64-encoded data:

bash
python convertImage.py
The script processes images in the resized_images folder and writes the base64-encoded data to the output.txt file.

Dependencies
Python 3.x
Pillow (Python Imaging Library)
Install Pillow using pip:

bash
pip install pillow
