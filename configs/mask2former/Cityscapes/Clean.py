_base_ = '../mask2former_swin-l-in22k-384x384-pre_8xb2-90k_cityscapes-512x1024.py'

data_root = "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Clean_Images/cityscapes"

train_dataloader = dict(
    dataset=dict(
        data_root=data_root)
        )
val_dataloader = dict(
    dataset=dict(
        data_root=data_root))
test_dataloader = val_dataloader

# Maybe: evaluation = dict(interval=16000, metric='mIoU', save_best='mIoU')