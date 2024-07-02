_base_ = [
    'Day_and_Cityscapes.py'
]

train_cfg = dict(type='IterBasedTrainLoop', max_iters=110000, val_interval=5000)