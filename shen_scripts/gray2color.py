from PIL import Image
import numpy as np
import os
import sys
from tqdm import tqdm

def colorize_segmentation_map(image_path, cityscapes_palette, output_folder):
    seg_map = Image.open(image_path)
    seg_array = np.array(seg_map)

    colored_seg_map = Image.new("RGB", seg_map.size)
    colored_seg_array = np.array(colored_seg_map)

    for label, color in enumerate(cityscapes_palette):
        colored_seg_array[seg_array == label] = color

    colored_seg_map = Image.fromarray(colored_seg_array)
    output_path = os.path.join(output_folder, os.path.basename(image_path))
    colored_seg_map.save(output_path)

def process_folder(input_folder, output_folder):
    # NOTE: nightcity has different pallette for sky. For vis against gt, we need to change it, Otherwise, it is fine.  
    cityscapes_palette = [
        [128, 64, 128], [244, 35, 232], [70, 70, 70], [102, 102, 156],
        [190, 153, 153], [153, 153, 153], [250, 170, 30], [220, 220, 0],
        [107, 142, 35], [152, 251, 152], [70, 130, 180], [220, 20, 60],
        [255, 0, 0], [0, 0, 142], [0, 0, 70], [0, 60, 100], [0, 80, 100],
        [0, 0, 230], [119, 11, 32]
    ]

    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder with progress bar
    for file in tqdm(os.listdir(input_folder), desc="Processing images"):
        if file.endswith(".png"):  # Assuming the images are PNGs
            image_path = os.path.join(input_folder, file)
            colorize_segmentation_map(image_path, cityscapes_palette, output_folder)


def process_all_methods(base_folder, specific_method=None):

    method_folders = [specific_method] if specific_method else os.listdir(base_folder)

    for method_folder in tqdm(method_folders, desc="Processing methods"):
        method_path = os.path.join(base_folder, method_folder)
        if os.path.isdir(method_path):
            input_folder = os.path.join(method_path, 'predictions')
            output_folder = os.path.join(method_path, 'visualizations')
            if os.path.exists(input_folder):
                process_folder(input_folder, output_folder)

# Example usage
base_folder = sys.argv[1] # e.g., '/longdata/anurag_storage/2PCNet/LLIE/mmsegmentation/work_dirs/DCS'
specific_method = sys.argv[2] if len(sys.argv) > 2 else None # e.g., 'CycleGAN-turbo'
process_all_methods(base_folder, specific_method)