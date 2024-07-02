_base_ = './No.py'

# Paths to images and labels
model_name = 'SKF'
img_path = f'/longdata/anurag_storage/2PCNet/LLIE/Results/{model_name}/cityscapes/leftImg8bit_val_all_in_one_dir'
seg_map_path = "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Clean_Images/cityscapes/leftImg8bit_val_all_in_one_dir_gtFine"

# NOTE: add val_dataloader
val_dataloader = dict(
    dataset=dict(
        data_prefix=dict(
            img_path=img_path,
            seg_map_path=seg_map_path,
        ),
    )
)
test_dataloader = val_dataloader