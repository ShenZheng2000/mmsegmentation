_base_ = './Dark.py'

# Paths to images and labels
img_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Clean_Images/CityScape150' # NOTE: clean (gt) images

# NOTE: add val_dataloader
val_dataloader = dict(
    dataset=dict(
        data_prefix=dict(
            img_path=img_path,
        ),
    )
)
test_dataloader = val_dataloader