_base_ = [
    '../../depth_anything_large_mask2former_16xb1_80k_cityscapes_896x896.py'
]

# NOTE: change dataset type and root
dataset_type = 'ACDCDataset'
img_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/ACDC/rgb_anon/night/val'
seg_map_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/ACDC/gt/night/val'

# NOTE: add val_dataloader
val_dataloader = dict(
    dataset=dict(
        type=dataset_type,
        data_prefix=dict(
            img_path=img_path,
            seg_map_path=seg_map_path
        ),
    )
)

test_dataloader = val_dataloader