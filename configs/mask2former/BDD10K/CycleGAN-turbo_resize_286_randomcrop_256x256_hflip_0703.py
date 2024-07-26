_base_ = './Day.py'

train_img_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train_day_CycleGAN-turbo_resize_286_randomcrop_256x256_hflip_0703'

train_dataloader = dict(
    dataset=dict(
        data_prefix=dict(
            img_path=train_img_path
        )
    )
)