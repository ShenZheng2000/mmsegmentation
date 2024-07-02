# _base_/datasets/mixed_bdd_cityscapes.py

# Define BDD100K dataset settings
dataset_type_bdd = 'BDD100KDataset'
train_img_path_bdd = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train_day'
train_seg_map_path_bdd = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/labels/sem_seg/masks/train'
val_img_path_bdd = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/val_night'
val_seg_map_path_bdd = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/labels/sem_seg/masks/val'
crop_size_bdd = (360, 640)
image_size_bdd = (1280, 720)

# Define Cityscapes dataset settings
dataset_type_cityscapes = 'CityscapesDataset'
train_img_path_cityscapes = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Clean_Images/cityscapes/leftImg8bit/train'
train_seg_map_path_cityscapes = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Clean_Images/cityscapes/gtFine/train'
val_img_path_cityscapes = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Clean_Images/cityscapes/leftImg8bit/val'
val_seg_map_path_cityscapes = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Clean_Images/cityscapes/gtFine/val'
crop_size_cityscapes = (512, 1024)
image_size_cityscapes = (2048, 1024)

train_pipeline_bdd = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations'),
    dict(type='RandomResize', scale=image_size_bdd, ratio_range=(0.5, 2.0), keep_ratio=True),
    dict(type='RandomCrop', crop_size=crop_size_bdd, cat_max_ratio=0.75),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PhotoMetricDistortion'),
    dict(type='PackSegInputs')
]
test_pipeline_bdd = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=image_size_bdd, keep_ratio=True),
    dict(type='LoadAnnotations'),
    dict(type='PackSegInputs')
]

dataset_bdd_train = dict(
    type=dataset_type_bdd,
    data_prefix=dict(
        img_path=train_img_path_bdd,
        seg_map_path=train_seg_map_path_bdd
    ),
    pipeline=train_pipeline_bdd
)

dataset_bdd_val = dict(
    type=dataset_type_bdd,
    data_prefix=dict(
        img_path=val_img_path_bdd,
        seg_map_path=val_seg_map_path_bdd
    ),
    pipeline=test_pipeline_bdd
)


train_pipeline_cityscapes = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations'),
    dict(type='RandomResize', scale=image_size_cityscapes, ratio_range=(0.5, 2.0), keep_ratio=True),
    dict(type='RandomCrop', crop_size=crop_size_cityscapes, cat_max_ratio=0.75),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PhotoMetricDistortion'),
    dict(type='PackSegInputs')
]
test_pipeline_cityscapes = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=image_size_cityscapes, keep_ratio=True),
    dict(type='LoadAnnotations'),
    dict(type='PackSegInputs')
]

dataset_cityscapes_train = dict(
    type=dataset_type_cityscapes,
    data_prefix=dict(
        img_path=train_img_path_cityscapes,
        seg_map_path=train_seg_map_path_cityscapes
    ),
    pipeline=train_pipeline_cityscapes
)

dataset_cityscapes_val = dict(
    type=dataset_type_cityscapes,
    data_prefix=dict(
        img_path=val_img_path_cityscapes,
        seg_map_path=val_seg_map_path_cityscapes
    ),
    pipeline=test_pipeline_cityscapes
)

# Combine datasets for training and validation
concat_data_train = dict(
    type='ConcatDataset',
    datasets=[dataset_cityscapes_train, dataset_bdd_train]
)

concat_data_val = dict(
    type='ConcatDataset',
    datasets=[dataset_cityscapes_val, dataset_bdd_val]
)

train_dataloader = dict(
    batch_size=2, # NOTE: reduce from 4 to 2 to fit in memory
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='InfiniteSampler', shuffle=True),
    dataset=concat_data_train
)

val_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=concat_data_val
)

test_dataloader = val_dataloader

val_evaluator = dict(type='IoUMetric', iou_metrics=['mIoU'])
test_evaluator = val_evaluator
