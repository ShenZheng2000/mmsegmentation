_base_ = '../mask2former_swin-l-in22k-384x384-pre_8xb2-90k_cityscapes-512x1024.py'

# NOTE: change dataset type and root
dataset_type = 'NightCityDataset'

train_img_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/NightCity/NightCity-images/images/train'
train_seg_map_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/NightCity/NightCity-label/label_correct/train'

img_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/NightCity/NightCity-images/images/val'
seg_map_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/NightCity/NightCity-label/label_correct/val'

crop_size = (512, 1024) # NOTE: (height, width)
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

# NOTE: choose 130k iteration for now
train_cfg = dict(type='IterBasedTrainLoop', max_iters=130000, val_interval=5000) 

# NOTE: must use complete pipeline
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=image_size, keep_ratio=True), 
    # add loading annotation after ``Resize`` because ground truth
    # does not need to do resize data transform
    dict(type='LoadAnnotations'),
    dict(type='PackSegInputs')
]

# NOTE: add val_dataloader
val_dataloader = dict(
    dataset=dict(
        type=dataset_type,
        data_prefix=dict(
            img_path=img_path, 
            seg_map_path=seg_map_path
        ),
        pipeline=test_pipeline,
    )
)

test_dataloader = val_dataloader
