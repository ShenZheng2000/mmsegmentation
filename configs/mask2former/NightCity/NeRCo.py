_base_ = './No.py'

# Paths to images and labels
model_name = 'NeRCo'
img_path = f'/longdata/anurag_storage/2PCNet/LLIE/Results/{model_name}/NightCity/NightCity-images/images/val'

# NOTE: add val_dataloader
val_dataloader = dict(
    dataset=dict(
        data_prefix=dict(
            img_path=img_path,
        ),
    )
)
test_dataloader = val_dataloader