# NOTE: BDD sem seg only for testset, but testset has no day/night labels
# Therefore, I manuually pick night images, and categorize rest as day images


import os
import shutil

train_or_val = 'val'

# Define the paths to the folders
train_folder = f'/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/{train_or_val}'
train_night_folder = f'/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/{train_or_val}_night'
train_day_folder = f'/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/{train_or_val}_day'

# Create the train_day folder if it doesn't exist
os.makedirs(train_day_folder, exist_ok=True)

# Get the list of files in the train and train_night folders
train_files = set(os.listdir(train_folder))
train_night_files = set(os.listdir(train_night_folder))

# Find the files that are in train but not in train_night
train_day_files = train_files - train_night_files

# Copy the files to the train_day folder
for file in train_day_files:
    src_path = os.path.join(train_folder, file)
    dst_path = os.path.join(train_day_folder, file)
    shutil.copy2(src_path, dst_path)

print(f"Copied {len(train_day_files)} files to {train_day_folder}")





# NOTE: I think none of the approach below works. Let's look at ALL images and see if we can find a pattern


# ######################## Approach based on average_brightness (RGB -> GrayScale) ########################

# import os
# import cv2
# import shutil
# import numpy as np

# def calculate_average_brightness_grayscale(image_path):
#     image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#     return image.mean()

# def create_new_folder(original_folder):
#     new_folder = f"{original_folder}_night"
    
#     # Check if the folder exists and delete it if it does
#     if os.path.exists(new_folder):
#         shutil.rmtree(new_folder)
    
#     # Create the new folder
#     os.makedirs(new_folder, exist_ok=True)
#     return new_folder

# def copy_night_images(original_folder, brightness_threshold=70):
#     new_folder = create_new_folder(original_folder)

#     count = 0
    
#     for root, _, files in os.walk(original_folder):
#         for file in files:
#             if file.endswith(('jpg', 'png')):
#                 image_path = os.path.join(root, file)
#                 average_brightness = calculate_average_brightness_grayscale(image_path)
                
#                 if average_brightness < brightness_threshold:
#                     # Construct the destination path
#                     relative_path = os.path.relpath(image_path, original_folder)
#                     destination_path = os.path.join(new_folder, relative_path)
#                     destination_dir = os.path.dirname(destination_path)
                    
#                     # Create the destination directory if it doesn't exist
#                     os.makedirs(destination_dir, exist_ok=True)
                    
#                     # Copy the image
#                     shutil.copy2(image_path, destination_path)
#                     count += 1

#     print(f"Total number of night images: {count}")

# # Example usage
# original_folder = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Clean_Images/bdd100k/images/10k/val'
# copy_night_images(original_folder, brightness_threshold=60)




######################## Approach based on average_brightness (HSV Space) ########################

# import os
# import cv2
# import shutil
# import numpy as np

# def calculate_average_brightness_hsv(image_path):
#     image = cv2.imread(image_path)
#     hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#     v_channel = hsv_image[:, :, 2]
#     return v_channel.mean()

# def create_new_folder(original_folder):
#     new_folder = f"{original_folder}_night"
    
#     # Check if the folder exists and delete it if it does
#     if os.path.exists(new_folder):
#         shutil.rmtree(new_folder)
    
#     # Create the new folder
#     os.makedirs(new_folder, exist_ok=True)
#     return new_folder

# def copy_night_images(original_folder, brightness_threshold):
#     new_folder = create_new_folder(original_folder)

#     count = 0
    
#     for root, _, files in os.walk(original_folder):
#         for file in files:
#             if file.endswith(('jpg', 'png')):
#                 image_path = os.path.join(root, file)
#                 average_brightness = calculate_average_brightness_hsv(image_path)
                
#                 if average_brightness < brightness_threshold:
                    
#                     print("average_brightness = ", average_brightness)

#                     # Construct the destination path
#                     relative_path = os.path.relpath(image_path, original_folder)
#                     destination_path = os.path.join(new_folder, relative_path)
#                     destination_dir = os.path.dirname(destination_path)
                    
#                     # Create the destination directory if it doesn't exist
#                     os.makedirs(destination_dir, exist_ok=True)
                    
#                     # Copy the image
#                     shutil.copy2(image_path, destination_path)
#                     # print(f"Copied {image_path} to {destination_path}")

#                     count += 1

#     print(f"Total number of night images: {count}")

# # Example usage
# original_folder = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Clean_Images/bdd100k/images/10k/val'
# copy_night_images(original_folder, brightness_threshold=70)





######################## Approach based on percentage of dark pixels ########################

# import os
# import cv2
# import shutil
# import numpy as np

# def calculate_dark_pixel_percentage(image_path, dark_threshold=60):
#     image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#     total_pixels = image.size
#     dark_pixels = np.sum(image < dark_threshold)
#     return dark_pixels / total_pixels * 100

# def create_new_folder(original_folder):
#     new_folder = f"{original_folder}_night"
    
#     # Check if the folder exists and DELETE it if it does
#     if os.path.exists(new_folder):
#         shutil.rmtree(new_folder)
    
#     # Create the new folder
#     os.makedirs(new_folder, exist_ok=True)
#     return new_folder

# def copy_night_images(original_folder, dark_pixel_percentage_threshold=50, dark_threshold=60):
#     new_folder = create_new_folder(original_folder)

#     count = 0
    
#     for root, _, files in os.walk(original_folder):
#         for file in files:
#             if file.endswith(('jpg', 'png')):
#                 image_path = os.path.join(root, file)
#                 dark_pixel_percentage = calculate_dark_pixel_percentage(image_path, dark_threshold)
                
#                 if dark_pixel_percentage > dark_pixel_percentage_threshold:
#                     # Construct the destination path
#                     relative_path = os.path.relpath(image_path, original_folder)
#                     destination_path = os.path.join(new_folder, relative_path)
#                     destination_dir = os.path.dirname(destination_path)
                    
#                     # Create the destination directory if it doesn't exist
#                     os.makedirs(destination_dir, exist_ok=True)
                    
#                     # Copy the image
#                     shutil.copy2(image_path, destination_path)
#                     # print(f"Copied {image_path} to {destination_path}")

#                     count += 1

#     print(f"Total number of night images: {count}")

# # Example usage
# original_folder = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Clean_Images/bdd100k/images/10k/val'
# copy_night_images(original_folder, dark_pixel_percentage_threshold=60, dark_threshold=50)




# import cv2

# def is_daytime(image_path, threshold=70): # NOTE: I select 70 as threshold
#     image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#     average_brightness = image.mean()
#     print(f"average_brightness = {average_brightness:.0f}")
#     return average_brightness > threshold

# # Example usage
# image_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Clean_Images/bdd100k/images/10k/val/9c7940d0-70d74ab0.jpg'
# if is_daytime(image_path):
#     print("The image was captured during the day.")
# else:
#     print("The image was captured at night.")
