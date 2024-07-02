_base_ = '../Dark_Zurich/Dark.py'

# NOTE: change dataset type and root
dataset_type = 'CityscapesDataset'
img_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/CityScape150/leftImg8bit'
seg_map_path = '/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/CityScape150/gtFine'

# NOTE: add val_dataloader
val_dataloader = dict(
    dataset=dict(
        type=dataset_type,
        data_prefix=dict(
            img_path=img_path,
            seg_map_path=seg_map_path
        ),
    )
)

test_dataloader = val_dataloader