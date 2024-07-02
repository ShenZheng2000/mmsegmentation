_base_ = './Day_Night.py'

# NOTE: freeze backbone weights here
model = dict(
    backbone=dict(
        frozen_stages=2,
    ),
)

train_cfg = dict(type='IterBasedTrainLoop', max_iters=110000, val_interval=5000)