_base_ = './No.py'

# NOTE: change dataset type and root
dataset_type = 'NightCityDataset'
train_img_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/NightCity/NightCity-images/images/train'
train_seg_map_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/NightCity/NightCity-label/label_correct/train'

# TODO: adjust crop_size if needed
crop_size = (512, 512) # NOTE: (height, width)
image_size = (1024, 512) # NOTE: NightCity size is here (width, height)

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


# TODO: increase max_iters if needed
train_cfg = dict(type='IterBasedTrainLoop', max_iters=100000, val_interval=5000) 