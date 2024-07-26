_base_ = './Day.py'

# NOTE: test on train to get some visualizations
val_img_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train_day_CycleGAN-turbo'
val_seg_map_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/labels/sem_seg/masks/train'

val_dataloader = dict(
    dataset=dict(
        data_prefix=dict(
            img_path=val_img_path,
            seg_map_path=val_seg_map_path),
    )
)
test_dataloader = val_dataloader
