import numpy as np
from PIL import Image
import os

# NOTE: NightCity dataset has different IDs for sky. We need to convert them to match Cityscapes IDs!!!

# Define the current grayscale ID to correct grayscale ID mapping
id_to_correct_id = {
    7: 0,  # road
    8: 1,  # sidewalk
    11: 2, # building
    12: 3, # wall
    13: 4, # fence
    17: 5, # pole
    19: 6, # traffic light
    20: 7, # traffic sign
    21: 8, # vegetation
    22: 9, # terrain
    23: 10, # sky
    24: 11, # person
    25: 12, # rider
    26: 13, # car
    27: 14, # truck
    28: 15, # bus
    31: 16, # train
    32: 17, # motorcycle
    33: 18  # bicycle
}

def convert_grayscale_id(image_path, save_path):
    """
    Convert a grayscale ID image to the corrected grayscale ID image using the mapping and save the result.
    
    Parameters:
    - image_path: str, path to the input grayscale ID image.
    - save_path: str, path to save the resulting corrected grayscale ID image.
    """
    # Load the grayscale image
    grayscale_image = Image.open(image_path).convert('L')
    grayscale_array = np.array(grayscale_image)
    
    # Create an empty array for the corrected grayscale ID image
    corrected_id_array = np.zeros_like(grayscale_array, dtype=np.uint8)
    
    # Apply the mapping to convert current IDs to the correct IDs
    for current_id, correct_id in id_to_correct_id.items():
        # Find where the current ID matches and assign the corresponding correct ID
        match = grayscale_array == current_id
        corrected_id_array[match] = correct_id
    
    # Convert the corrected ID array to an image
    corrected_id_image = Image.fromarray(corrected_id_array, mode='L')
    
    # Save the corrected grayscale ID image
    corrected_id_image.save(save_path)
    print(f"Saved corrected grayscale ID image to {save_path}")

def process_folder(input_folder, output_folder):
    """
    Process all grayscale ID images in the input folder, convert them using the ID-to-ID mapping,
    and save them to the output folder with the same filenames.
    
    Parameters:
    - input_folder: str, path to the directory containing input grayscale ID images.
    - output_folder: str, path to the directory to save corrected grayscale ID images.
    """
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Iterate through all files in the input folder
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(('png', 'jpg', 'jpeg')):  # Add other image extensions if needed
                input_image_path = os.path.join(root, file)
                # Create the corresponding output path, maintaining the same filename
                relative_path = os.path.relpath(input_image_path, input_folder)
                output_image_path = os.path.join(output_folder, relative_path)
                
                # Ensure the directory for the output image exists
                os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
                
                # Convert and save the corrected grayscale ID image
                convert_grayscale_id(input_image_path, output_image_path)

# Example usage
input_directory_path = "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/NightCity/NightCity-label/label/val"
output_directory_path = "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/NightCity/NightCity-label/label_correct/val"

# Process the folder
process_folder(input_directory_path, output_directory_path)



# Just for reference...
# # RGB Color -> Correct grayscale ID -> Current grayscale ID
# palette = [
#     [128, 64, 128],  # 0: road (same) -> 7
#     [244, 35, 232],  # 1: sidewalk (same) -> 8
#     [70, 70, 70],    # 2: building (same)  -> 11
#     [102, 102, 156], # 3: wall (same) -> 12
#     [190, 153, 153], # 4: fence (same) -> 13
#     [153, 153, 153], # 5: pole (same) -> 17
#     [250, 170, 30],  # 6: traffic light (same) -> 19
#     [220, 220, 0],   # 7: traffic sign (same) -> 20
#     [107, 142, 35],  # 8: vegetation (same) -> 21
#     [152, 251, 152], # 9: terrain (same) -> 22
#     [0, 130, 180],  # 10: sky (different) -> 23
#     [220, 20, 60],   # 11: person (same) -> 24
#     [255, 0, 0],     # 12: rider (same) -> 25
#     [0, 0, 142],     # 13: car (same) -> 26
#     [0, 0, 70],      # 14: truck (same) -> 27
#     [0, 60, 100],    # 15: bus (same) -> 28
#     [0, 80, 100],    # 16: train (same) -> 31
#     [0, 0, 230],     # 17: motorcycle (same) -> 32
#     [119, 11, 32]    # 18: bicycle (same) -> 33
# ]
