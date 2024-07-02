_base_ = './Clean.py'

train_dataloader = dict(
    dataset=dict(
        data_prefix=dict(
            img_path='leftImg8bit_Instruct-pix2pix/train'
            ),
    )
)

# Maybe: evaluation = dict(interval=16000, metric='mIoU', save_best='mIoU')