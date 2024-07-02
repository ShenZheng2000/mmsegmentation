import os
from PIL import Image

def check_image_sizes(directory, expected_width=1024, expected_height=512):
    """
    Check all images in a directory and print the names of those that do not match the specified size.

    Parameters:
    - directory: str, path to the directory containing images or labels.
    - expected_width: int, expected width of the images.
    - expected_height: int, expected height of the images.
    """
    # Traverse all files in the directory
    mis_cnt = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('png', 'jpg', 'jpeg')):  # Add other image extensions if needed
                image_path = os.path.join(root, file)
                try:
                    with Image.open(image_path) as img:
                        width, height = img.size
                        if width != expected_width or height != expected_height:
                            print(f"File '{image_path}' has size {width}x{height}, expected {expected_width}x{expected_height}.")
                            mis_cnt += 1
                except Exception as e:
                    print(f"Error processing file '{image_path}': {e}")

    print(f"Finished checking {len(files)} files. Found {mis_cnt} mismatched.")

# Example usage
directory_path = "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/NightCity/NightCity-label/label/val"

# Check the sizes of all images or labels in the directory
check_image_sizes(directory_path, expected_width=1024, expected_height=512)
