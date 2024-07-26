# Fine-tuning Semantic Segmentation Model with Generated Night Images

This project involves training generative models to convert day images to night images and then fine-tuning a semantic segmentation model on these generated night images. The goal is to improve semantic segmentation performance under nighttime conditions.

## Overview

1. **Generative Model Training**: Use CUT, MoNCE, TPSeNCE models to generate night images from the BDD100K day images (Skip for now)
2. **Semantic Segmentation Fine-tuning**: Fine-tune the mask2former model on the generated BDD100K night images.
3. **Model Evaluation**: Assess the performance of the fine-tuned model on multiple datasets including Cityscapes, DarkZurich, and ACDC (further datasets like BDD100K may be considered).

## Environment Setup

Activate the Conda environment with all the necessary dependencies:

```
conda activate openmmlab
```

NOTE: Ensure that mmengine is this version or lower to avoid conflicts.

```
mim install mmengine==0.10.2
```

# Dataset Preparation

Datasets required:

* BDD100K
* Cityscapes
* DarkZurich
* ACDC


# Sem. Seg. Model Finetuning

Run in terminal

```
bash tools/train.sh $MODEL
```

Replace `$MODEL` with your chosen model (options: CUT, MONCE, TPSeNCE).


# Sem. Seg. Model Testing

Run in terminal 

```
bash tools/test.sh
```

This script contains detailed instructions for testing on different datasets and with various models.


# Sem. Seg. Colorization

Run in terminal
```
python shen_scripts/gray2color.py $FOLDER
```

This will generate color semantic maps in `${FOLDER}/${MODEL}/visualizations`, suppose that the predictions are at `${FOLDER}/${MODEL}/predictions`


# Important Configs

Dataset configuration files:

* Cityscapes:  `configs/mask2former/Cityscapes`
* Dark Zurich: `configs/mask2former/Dark_Zurich`
* ACDC: `configs/mask2former/ACDC`