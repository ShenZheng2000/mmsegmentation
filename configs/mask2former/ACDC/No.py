_base_ = '../mask2former_swin-l-in22k-384x384-pre_8xb2-90k_cityscapes-512x1024.py'

# NOTE: change dataset type and root
dataset_type = 'ACDCDataset'
img_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/ACDC/rgb_anon/night/val'
seg_map_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/ACDC/gt/night/val'

# NOTE: must use complete pipeline
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=(1920, 1080), keep_ratio=True),
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