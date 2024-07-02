_base_ = './Day_Night.py'

# NOTE: freeze backbone weights here
model = dict(
    backbone=dict(
        frozen_stages=4,
    ),
)

train_cfg = dict(type='IterBasedTrainLoop', max_iters=120000, val_interval=5000)