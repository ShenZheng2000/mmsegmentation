# Copyright (c) OpenMMLab. All rights reserved.
from mmseg.registry import DATASETS
from .cityscapes import CityscapesDataset


@DATASETS.register_module()
class NightCityDataset(CityscapesDataset):
    """NightCityDataset dataset."""

    def __init__(self,
                 img_suffix='.png',
                 seg_map_suffix='_labelIds.png',
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)