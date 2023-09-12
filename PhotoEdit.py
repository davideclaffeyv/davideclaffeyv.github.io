# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 14:50:25 2023

@author: david
"""

import os
import PIL
from PIL import Image


# Function to find the dimensions of the smallest image in a folder
def find_smallest_image_dimensions(folder_path):
    smallest_width = float('inf')
    smallest_height = float('inf')

    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image = Image.open(os.path.join(folder_path, filename))
            width, height = image.size
            smallest_width = min(smallest_width, width)
            smallest_height = min(smallest_height, height)

    return smallest_width, smallest_height

# Function to convert and resize images in the folder
def convert_and_crop_images(folder_path, output_folder):
    smallest_width, smallest_height = find_smallest_image_dimensions(folder_path)

    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image = Image.open(os.path.join(folder_path, filename))
            image = image.convert('RGBA')  # Convert to RGBA (PNG with alpha channel)

            # Calculate the cropping box to match the smallest dimensions
            width, height = image.size
            left = (width - smallest_width) // 2
            top = (height - smallest_height) // 2
            right = (width + smallest_width) // 2
            bottom = (height + smallest_height) // 2

            # Crop the image
            image = image.crop((left, top, right, bottom))

            new_filename = os.path.splitext(filename)[0] + '.png'
            image.save(os.path.join(output_folder, new_filename), 'PNG')

if __name__ == "__main__":
    input_folder = r"C:\Users\david\Dropbox (Personal)\PC\Desktop\CNC"
    output_folder = r"C:\Users\david\Dropbox (Personal)\PC\Desktop\CNC"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    convert_and_crop_images(input_folder, output_folder)
    print("Conversion and cropping completed.")
    
#%%
import os
import PIL
from PIL import Image
from pillow_heif import register_heif_opener

# Function to crop images to a specified aspect ratio
def crop_images_to_aspect_ratio(folder_path, output_folder, target_aspect_ratio):
    
    register_heif_opener()
    
    directory = r"C:\Users\david\Dropbox (Personal)\PC\Documents\git_page\davideclaffeyv\davideclaffeyv.github.io\CNC\CNC Photo processing"
    files = [f for f in os.listdir(directory) if f.endswith('.HEIC') or f.endswith('.heif')]
    
    # Convert each file to JPEG
    for filename in files:
        image = Image.open(os.path.join(directory, filename))
        image.convert('RGB').save(os.path.join(directory, os.path.splitext(filename)[0] + '.jpg'))
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image = Image.open(os.path.join(folder_path, filename))

            # Calculate cropping dimensions to match the target aspect ratio
            width, height = image.size
            if width / height > target_aspect_ratio:
                new_width = int(height * target_aspect_ratio)
                left = (width - new_width) // 2
                right = left + new_width
                top = 0
                bottom = height
            else:
                new_height = int(width / target_aspect_ratio)
                top = (height - new_height) // 2
                bottom = top + new_height
                left = 0
                right = width

            # Crop the image
            image = image.crop((left, top, right, bottom))

            new_filename = os.path.splitext(filename)[0] + '.png'
            image.save(os.path.join(output_folder, new_filename), 'PNG')

if __name__ == "__main__":
    input_folder = r"C:\Users\david\Dropbox (Personal)\PC\Documents\git_page\davideclaffeyv\davideclaffeyv.github.io\CNC\CNC Photo processing"
    output_folder = r"C:\Users\david\Dropbox (Personal)\PC\Documents\git_page\davideclaffeyv\davideclaffeyv.github.io\CNC\CNC Photo processed"
    target_aspect_ratio = 4.0/3.0  # Specify your desired aspect ratio here

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    crop_images_to_aspect_ratio(input_folder, output_folder, target_aspect_ratio)
    print(f"Cropping to a {target_aspect_ratio}:1 aspect ratio completed.")
#%%
import os
import PIL
from PIL import Image

# Function to generate a YAML file with entries for all PNG images in the folder
def generate_combined_yaml_file(folder_path, output_file, url_prefix):
    with open(output_file, 'w') as yaml_file:
        yaml_file.write('---\n')  # Start of the YAML document
        for filename in os.listdir(folder_path):
            if filename.lower().endswith('.png'):
                image_path = os.path.join(folder_path, filename)
                title = os.path.splitext(filename)[0]
                url = os.path.join(url_prefix, filename)  # Construct the URL
                yaml_content = f"""\
- url: {url}
  image_path: {url}
  title: "{title}"
"""
                yaml_file.write(yaml_content)
        yaml_file.write('---\n')  # End of the YAML document

if __name__ == "__main__":
    input_folder = r"C:\Users\david\Dropbox (Personal)\PC\Documents\git_page\davideclaffeyv\davideclaffeyv.github.io\CNC\CNC Photo processed"
    output_file = r"C:\Users\david\Dropbox (Personal)\PC\Desktop\CNC\photo.yaml"
    url_prefix = "/assets/images/CNC/"

    print(f"Generating YAML file for PNG images in: {input_folder}")

    # Create an empty YAML file
    open(output_file, 'w').close()

    generate_combined_yaml_file(input_folder, output_file, url_prefix)
    print(f"Combined YAML file generation completed at: {output_file}.")
