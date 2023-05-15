<h1>Image Resizing and Base64 Encoding</h1>
<h2>This repository contains two Python scripts:</h2>

<p>resize.py: Resizes images and reduces their bit depth.</p>
<p>convertImage.py: Converts resized images to base64-encoded data and writes the data to an output file.</p>

<h3>Usage</h3>
<h4>1. Resize and change bit depth of images</h4>
<p>Run resize.py to resize images and change their bit depth:</p>

```
python resize.py
```

<p>The script processes images in the public folder, resizes them to a maximum size of 500x500 pixels, and reduces their bit depth to 256 colors. The resized images are saved in the resized_images folder.</p>

<h4>2. Convert resized images to base64</h4>
<p>Run convertImage.py to convert the resized images to base64-encoded data:</p>

```
python convertImage.py
```
  
<p>The script processes images in the resized_images folder and writes the base64-encoded data to the output.txt file.</p>

<h3>Dependencies</h3>
<p>Python 3.x</p>
<p>Pillow (Python Imaging Library)</p>
<h4>Install Pillow using pip:</h4>

```
pip install pillow
```
