import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
from matplotlib.colors import TwoSlopeNorm

# Purpose: Compute the per-pixel acc. dif. between two folders of images


def load_images(folder, is_gt=False, is_cs=False):
    if is_gt:
        if is_cs:
            surfix = 'gtFine_color.png'
        else:
            surfix = 'gt_labelColor.png'
    else:
        if is_cs:
            surfix = 'leftImg8bit.png'
        else:
            surfix = 'rgb_anon.png'

    images = []

    # Walk through the directory recursively
    for root, dirs, files in os.walk(folder):
        # Pick the files only if they end with "gt_labelColor.png"
        for file in files:
            # print("root is", root)
            if file.endswith(surfix) and 'train' not in root:
                images.append(
                    os.path.join(root, file)
                    )
                
    return images

def get_average_score(predicted_map_path, gt_map_path, dataset = 'cityscapes', resize_shape=None):

    if dataset == 'cityscapes':
        is_cs = True
    else:
        is_cs = False

    # Load predicted and GT images
    predicted_maps = load_images(predicted_map_path, is_gt=False, is_cs=is_cs)
    gt_maps = load_images(gt_map_path, is_gt=True, is_cs=is_cs)

    predicted_maps = sorted(predicted_maps, key=lambda x: "_".join(x.split('_')[:-2]))
    gt_maps = sorted(gt_maps, key=lambda x: "_".join(x.split('_')[:-2]))

    scores = None

    # This is for grayscale
    for i in range(len(predicted_maps)):
        pred_map = cv2.imread(predicted_maps[i], cv2.IMREAD_GRAYSCALE)
        gt_map = cv2.imread(gt_maps[i], cv2.IMREAD_GRAYSCALE)

        # resize the images if necessary
        if resize_shape is not None:
            pred_map = cv2.resize(pred_map, resize_shape, interpolation=cv2.INTER_NEAREST)
            gt_map = cv2.resize(gt_map, resize_shape, interpolation=cv2.INTER_NEAREST)

        # create a mask for ignore_value (set to sky for now)
        mask = (gt_map != 117)

        # Compute scores
        # scores += np.where(pred_map == gt_map, 1, 0)
        if scores is None:
            scores = np.zeros_like(pred_map, dtype=np.float32)

        scores += np.where((pred_map == gt_map) & mask, 1, 0)

    # Calculate average scores
    average_scores = scores / len(predicted_maps)

    return average_scores

dataset = 'acdc' # ['acdc', 'darkzurich', 'cityscapes']
model = "TPSeNCE" # ['CycleGAN-turbo', 'TPSeNCE']
resize_shape = (256, 256)

if dataset == 'cityscapes':
    pred_map_path_baseline =  "/home/aghosh/Projects/2PCNet/Methods/DAFormer/work_dirs/local-exp80/test_11_11/preds"
    gt_map_path = "/home/aghosh/Projects/2PCNet/Datasets/cityscapes/gtFine/val"
    ours_map_path = "/home/aghosh/Projects/2PCNet/Methods/DAFormer/work_dirs/local-exp88/test_11_11/preds"

# NOTE: only consider night images for now
elif dataset == 'acdc':
    pred_map_path_baseline = '/longdata/anurag_storage/2PCNet/LLIE/mmsegmentation/work_dirs/ACDC/Dark/visualizations'
    gt_map_path = '/home/aghosh/Projects/2PCNet/Datasets/acdc/gt/night/val'
    ours_map_path = f"/longdata/anurag_storage/2PCNet/LLIE/mmsegmentation/work_dirs/ACDC/{model}/visualizations" 

elif dataset == 'darkzurich':
    pred_map_path_baseline = "/longdata/anurag_storage/2PCNet/LLIE/mmsegmentation/work_dirs/Dark_Zurich/Dark/visualizations" 
    gt_map_path = "/home/aghosh/Projects/2PCNet/Datasets/dark_zurich/gt/val/night/GOPR0356"
    ours_map_path = f"/longdata/anurag_storage/2PCNet/LLIE/mmsegmentation/work_dirs/Dark_Zurich/{model}/visualizations" 

average_scores_baseline = get_average_score(pred_map_path_baseline, gt_map_path, dataset=dataset, resize_shape=resize_shape)
average_scores_ours = get_average_score(ours_map_path, gt_map_path, dataset=dataset, resize_shape=resize_shape)

data = average_scores_ours - average_scores_baseline

# Visualization
norm = TwoSlopeNorm(
                    vmin=-max(data.flatten()), 
                    vcenter=0, 
                    vmax=max(data.flatten())
                    ) # Maybe: use smaller scales for better visualization
plt.imshow(data, cmap='bwr', norm=norm)  # 'bwr' is a blue-white-red colormap
plt.colorbar(fraction=0.05)
plt.tight_layout()
plt.xticks([])
plt.yticks([])
# plt.axis('off')
plt.savefig(f'vis_err_map/{dataset}_{model}.png', bbox_inches='tight')
# plt.savefig(f'average_score_visualization_{dataset}.pdf', bbox_inches='tight')