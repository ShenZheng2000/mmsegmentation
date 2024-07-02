

import os
import numpy as np
from PIL import Image

# Define the colors to check for in the images
colors_to_check = {
    # "wall": (102, 102, 156),
    # "terrain": (152, 251, 152),
    # "rider": (255, 0, 0),
    # "truck": (0, 0, 70),
    # "train": (0, 80, 100),
    # "motorcycle": (0, 0, 230),
    "bicycle": (119, 11, 32)
}

def check_colors_in_image(image_path):
    """
    Check for specified colors in an image and print the filename if any are found.
    
    Parameters:
    - image_path: str, path to the input color map image.
    """
    # Load the image
    color_image = Image.open(image_path).convert('RGB')
    color_array = np.array(color_image)
    
    # Initialize a flag to check if any specified color is found
    found = False
    
    # Check each specified color in the image
    for color_name, color in colors_to_check.items():
        if np.any(np.all(color_array == color, axis=-1)):
            found = True
            print(f"File '{image_path}' contains the color for {color_name} ({color}).")
            break  # Exit after finding the first match

def process_directory(directory_path):
    """
    Process all images in the given directory to check for the specified colors.
    
    Parameters:
    - directory_path: str, path to the directory containing color map images.
    """
    # Traverse all files in the directory
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(('png', 'jpg', 'jpeg')):  # Add other image extensions if needed
                image_path = os.path.join(root, file)
                check_colors_in_image(image_path)

# Example usage
input_directory_path = "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/NightCity/NightCity-label/color/val"  # Replace with your folder path

# Process the directory
process_directory(input_directory_path)