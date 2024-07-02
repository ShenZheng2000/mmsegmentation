_base_ = [
    '../../depth_anything_large_mask2former_16xb1_80k_cityscapes_896x896.py'
]

dataset_type = 'BDD100KDataset'

# TODO: even crop_size is reduced to 128x128, OOM still occurs!!!!!!!!!!!!
# We must find a smaller model.
crop_size = (128, 128)  # New smaller crop size

# Override the data_preprocessor to use the new crop_size
data_preprocessor = dict(
    size=crop_size
)

# Update model to use the new crop_size in its test_cfg
model = dict(
    test_cfg=dict(
        mode='slide',
        crop_size=crop_size,  # New smaller crop size
        stride=(128, 128)  # Adjust stride to maintain overlap, typically half of the crop size
    )
)

# Update train and test pipelines to use the new crop size
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations'),
    # NOTE: Remove RandomChoiceResize to reduce memory
    # dict(
    #     type='RandomChoiceResize',
    #     # scales=[int(x * 0.1 * 128) for x in range(5, 21)],  # Adjust scales to fit new crop size
    #     resize_type='ResizeShortestEdge',
    #     max_size=128 * 4
    #     ),  
    dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),  # New smaller crop size
    dict(type='RandomFlip', prob=0.5),
    # dict(type='PhotoMetricDistortion'), # Remove or simplify PhotoMetricDistortion to reduce memory
    dict(type='PackSegInputs') 
]

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=(128 * 4, 128), keep_ratio=True),  # Adjust resize scale to match new crop size
    dict(type='LoadAnnotations'),
    dict(type='PackSegInputs')
]

# NOTE: specify day images for training
train_img_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train_day'
train_seg_map_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/labels/sem_seg/masks/train'

train_dataloader = dict(
    dataset=dict(
        type=dataset_type,
        data_prefix=dict(
            img_path=train_img_path,
            seg_map_path=train_seg_map_path
        ),
        pipeline=train_pipeline  # Use the updated train pipeline
    )
)

# NOTE: specify night images for validation
val_img_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/val_night'
val_seg_map_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/labels/sem_seg/masks/val'

val_dataloader = dict(
    dataset=dict(
        type=dataset_type,
        data_prefix=dict(
            img_path=val_img_path,
            seg_map_path=val_seg_map_path
        ),
        pipeline=test_pipeline  # Use the updated test pipeline
    )
)

# Ensure test_dataloader is consistent with val_dataloader
test_dataloader = val_dataloader
