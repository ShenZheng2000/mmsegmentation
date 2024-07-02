# TODO: refer to this for more info: configs/_base_/datasets/bdd100k.py
_base_ = 'Day_crop_size_360_640.py'

dataset_type = 'BDD100KDataset'

# NOTE: specify day images for train
train_img_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train_day'
train_seg_map_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/labels/sem_seg/masks/train'

crop_size = (640, 640) # NOTE: (height, width) TODO: pay around this for better results?
image_size = (1280, 720) # NOTE: BDD100K size is here (width, height)

train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations'),
    dict(
        type='RandomResize',
        scale=image_size,
        ratio_range=(0.5, 2.0),
        keep_ratio=True),
    dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PhotoMetricDistortion'),
    dict(type='PackSegInputs')
]


train_dataloader = dict(
    batch_size=2,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(type='InfiniteSampler', shuffle=True),
    dataset=dict(
        type=dataset_type,
        data_prefix=dict(
            img_path=train_img_path,
            seg_map_path=train_seg_map_path),
        pipeline=train_pipeline))

