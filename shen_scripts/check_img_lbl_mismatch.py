# Purpose: 
# (1) Check for mismatch between image and label files in a dataset
# (2) Remove images that do not have corresponding labels

import os
import shutil

def check_img_lbl_mismatch(img_folder, lbl_folder, output_folder):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # List all files in image and label folders
    img_files = os.listdir(img_folder)
    lbl_files = os.listdir(lbl_folder)

    # Remove file extensions to compare base names
    img_files_base = [os.path.splitext(f)[0] for f in img_files]
    lbl_files_base = [os.path.splitext(f)[0] for f in lbl_files]

    # Find mismatched files (files in img_folder but not in lbl_folder)
    mismatched_files = [f for f in img_files_base if f not in lbl_files_base]
    
    # Copy mismatched files to output folder
    for file in mismatched_files:
        original_file_path = os.path.join(img_folder, file + '.jpg')  # Assuming images are in .jpg format
        if os.path.exists(original_file_path):
            shutil.copy(original_file_path, output_folder)

    return mismatched_files

def remove_unlabeled_files(root_dir, unlabeled_files, exclude_folder):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if exclude_folder in dirpath:
            continue
        for file in filenames:
            file_base = os.path.splitext(file)[0]
            if file_base in unlabeled_files:
                file_path = os.path.join(dirpath, file)
                os.remove(file_path)
                print(f"Removed: {file_path}")

img_folder = "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train"
lbl_folder = "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/labels/sem_seg/masks/train"
output_folder = "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/train_no_label"
root_dir = "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k"

mismatched_files = check_img_lbl_mismatch(img_folder, lbl_folder, output_folder)

print(f"Number of mismatched files: {len(mismatched_files)}")
print(mismatched_files)

remove_unlabeled_files(root_dir, mismatched_files, output_folder)