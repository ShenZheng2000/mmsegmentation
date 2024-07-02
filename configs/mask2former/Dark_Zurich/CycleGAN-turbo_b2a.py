_base_ = './No.py'

# Paths to images and labels
model_name = 'CycleGAN-turbo_b2a'
img_path = f'/longdata/anurag_storage/2PCNet/LLIE/Results/{model_name}/Dark_Zurich/rgb_anon/val/night'

# NOTE: add val_dataloader
val_dataloader = dict(
    dataset=dict(
        data_prefix=dict(
            img_path=img_path,
        ),
    )
)
test_dataloader = val_dataloader