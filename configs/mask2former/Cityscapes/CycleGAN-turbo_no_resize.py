_base_ = './Clean.py'

train_dataloader = dict(
    dataset=dict(
        data_prefix=dict(
            img_path='leftImg8bit_CycleGAN-turbo_no_resize/train'
            ),
    )
)

# Maybe: evaluation = dict(interval=16000, metric='mIoU', save_best='mIoU')

# # NOTE: let's try this to see performance are better with more epochs
# train_cfg = dict(type='IterBasedTrainLoop', max_iters=100000, val_interval=5000)