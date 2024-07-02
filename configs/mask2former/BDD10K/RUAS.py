_base_ = './Day.py'

# Paths to images and labels
model_name = 'RUAS'
img_path = f'/longdata/anurag_storage/2PCNet/LLIE/Results/{model_name}/bdd100k/images/10k/val_night'

# NOTE: add val_dataloader
val_dataloader = dict(
    dataset=dict(
        data_prefix=dict(
            img_path=img_path,
        ),
    )
)
test_dataloader = val_dataloader