# TODO: refer to this for more info: configs/_base_/datasets/bdd100k.py
_base_ = 'Day_crop_size_360_640.py'

train_cfg = dict(type='IterBasedTrainLoop', max_iters=110000, val_interval=5000)