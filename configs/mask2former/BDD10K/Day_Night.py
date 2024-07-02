_base_ = './Day.py'

train_img_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train_day'

train_dataloader = dict(
    dataset=dict(
        data_prefix=dict(
            img_path=train_img_path
        )
    )
)