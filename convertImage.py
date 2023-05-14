#befor running this make sure you are in the correct directory

import base64
import os

# Function to convert an image file to base64
def image_to_base64(image_path):
    # Open the image file in binary mode
    with open(image_path, "rb") as image_file:
        # Encode the image file as base64
        encoded_image = base64.b64encode(image_file.read())
    # Return the base64-encoded data as a string
    return encoded_image.decode("utf-8")

# Set the path to the public folder
public_folder = "resized_images"

# Open the output file
with open("output.txt", "w") as output_file:
    # Walk through the public folder and its subfolders
    for root, dirs, files in os.walk(public_folder):
        # Loop through the files in the current folder
        for file in files:
            # Check if the file has an image file extension
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                # Get the full path to the image file
                image_path = os.path.join(root, file)
                # Convert the image file to base64
                base64_data = image_to_base64(image_path)
                # Write the base64-encoded data for the image file to the output file
                output_file.write(f"Base64 encoded data for {file}:\n")
                output_file.write(base64_data)
                output_file.write("\n\n")
