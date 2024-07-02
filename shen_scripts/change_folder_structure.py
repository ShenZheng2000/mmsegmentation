# import os
# import shutil

# # Purpose: change from format of ${I2I_MODEL}/${TEST_DATASET} to ${TEST_DATASET}/${I2I_MODEL}?

# # Define the base directory (i.e., FINETUNE level!!!!!!!!!!!!!!)
# base_dir = "/longdata/anurag_storage/2PCNet/LLIE/mmsegmentation/work_dirs/Cityscapes/Cityscapes"

# # Traverse the current folder structure from the FINETUNE level
# for i2i_model in os.listdir(base_dir):
#     i2i_model_path = os.path.join(base_dir, i2i_model)
#     if os.path.isdir(i2i_model_path):
#         for test_dataset in os.listdir(i2i_model_path):
#             test_dataset_path = os.path.join(i2i_model_path, test_dataset)
#             if os.path.isdir(test_dataset_path):
#                 # Create new directory structure
#                 new_dir = os.path.join(base_dir, test_dataset, i2i_model)
#                 os.makedirs(new_dir, exist_ok=True)

#                 # Move files to new structure
#                 for file_name in os.listdir(test_dataset_path):
#                     src_file = os.path.join(test_dataset_path, file_name)
#                     dest_file = os.path.join(new_dir, file_name)
#                     shutil.move(src_file, dest_file)

#                 # Remove old empty directories
#                 os.rmdir(test_dataset_path)

#         # Remove the old I2I_MODEL directory if empty
#         if not os.listdir(i2i_model_path):
#             os.rmdir(i2i_model_path)

# # Remove old TEST_DATASET directories if empty
# for test_dataset in os.listdir(base_dir):
#     test_dataset_path = os.path.join(base_dir, test_dataset)
#     if os.path.isdir(test_dataset_path):
#         for i2i_model in os.listdir(test_dataset_path):
#             i2i_model_path = os.path.join(test_dataset_path, i2i_model)
#             if os.path.isdir(i2i_model_path) and not os.listdir(i2i_model_path):
#                 os.rmdir(i2i_model_path)