_base_ = './No_crop_size_512_1024.py'

# TODO: increase max_iters if needed
train_cfg = dict(type='IterBasedTrainLoop', max_iters=130000, val_interval=5000) 