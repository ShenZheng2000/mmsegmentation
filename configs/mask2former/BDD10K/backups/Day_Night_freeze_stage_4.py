_base_ = './Day_Night.py'

# NOTE: freeze backbone weights here
model = dict(
    backbone=dict(
        frozen_stages=4,
    ),
)