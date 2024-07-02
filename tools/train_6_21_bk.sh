# NOTE: let's assume mask2former is the backbone

# Define the train_model function
train_model() {
    local PRETRAIN=$1
    local FINETUNE=$2
    local TEST_DATASET=$3
    local I2I_MODEL=$4
    local GPU_ID=${5:-0}  # Default GPU ID to 0 if not specified

    # Determine the config file path based on the PRETRAIN option
    if [ "$PRETRAIN" = "depth_anything" ]; then
        config_file="configs/mask2former/depth_anything/${TEST_DATASET}/${I2I_MODEL}.py"
    else
        config_file="configs/mask2former/${TEST_DATASET}/${I2I_MODEL}.py"
    fi

    # Define the output directory
    output_dir="work_dirs/${PRETRAIN}/${FINETUNE}/${TEST_DATASET}/${I2I_MODEL}"
    mkdir -p "${output_dir}"

    echo "Training ${PRETRAIN}/${FINETUNE}/${TEST_DATASET} with ${I2I_MODEL}..."

    # Dictionary of pretrained paths
    declare -A pretrained_paths
    pretrained_paths["Cityscapes"]="pretrained/mask2former_swin-l-in22k-384x384-pre_8xb2-90k_cityscapes-512x1024_20221202_141901-28ad20f1.pth"
    pretrained_paths["Day"]="work_dirs/BDD10K/No/BDD10K/Day/best_mIoU_iter_80000.pth"
    pretrained_paths["depth_anything"]="checkpoints/cityscapes_vitl_mIoU_86.4.pth"

    # Construct the command based on the FINETUNE and PRETRAIN options
    if [ "$FINETUNE" = "No" ]; then
        CMD="python tools/train.py $config_file --work-dir $output_dir"
        echo "Starting training from scratch..."
    else
        pretrained_path=${pretrained_paths[$PRETRAIN]}
        if [ -z "$pretrained_path" ]; then
            echo "Invalid pretrain dataset: $PRETRAIN"
            exit 1
        fi
        CMD="python tools/train.py $config_file --work-dir $output_dir --resume --cfg-options load_from='$pretrained_path'"
        echo "Resuming training with fine-tuning on $PRETRAIN from $pretrained_path..."
    fi

    # Execute the command with the specified GPU and log output
    CUDA_VISIBLE_DEVICES=$GPU_ID \
    nohup \
    $CMD \
    > outs/${PRETRAIN}_${FINETUNE}_${TEST_DATASET}_${I2I_MODEL}.out 2>&1 &

    echo "Training initiated. Check the output file: outs/${PRETRAIN}_${FINETUNE}_${TEST_DATASET}_${I2I_MODEL}.out"
}


# Cityscapes -> BDD10K
# train_model Cityscapes BDD10K BDD10K Day_Night 0
# train_model Cityscapes BDD10K BDD10K Day 1
# train_model Cityscapes BDD10K BDD10K Night 2
# train_model Cityscapes BDD10K BDD10K CUT 0
# train_model Cityscapes BDD10K BDD10K MoNCE 1
# train_model Cityscapes BDD10K BDD10K TPSeNCE 2
# train_model Cityscapes BDD10K BDD10K CycleGAN-turbo 0
# train_model Cityscapes BDD10K BDD10K Instruct-pix2pix 1

# Cityscapes -> NightCity (tuning crop_size)
# train_model Cityscapes NightCity NightCity No_crop_size_256_512 0
# train_model Cityscapes NightCity NightCity No_crop_size_512_512 1
# train_model Cityscapes NightCity NightCity No_crop_size_512_1024 2 => The best crop_size!
# train_model Cityscapes NightCity NightCity No_crop_size_384_768 3

# Cityscapes -> NightCity (tuning iterations) => 110k out of 130k is the best
# train_model Cityscapes NightCity NightCity No_crop_size_512_1024_iter_110k 0
# train_model Cityscapes NightCity NightCity No_crop_size_512_1024_iter_120k 1
# train_model Cityscapes NightCity NightCity No_crop_size_512_1024_iter_130k 2
# train_model Cityscapes NightCity NightCity No_crop_size_512_1024_iter_140k 3

# train_model Cityscapes NightCity NightCity Night 0

# NightCity pretrain -> skip for now


# BDD10K pretrain
# train_model BDD10K No BDD10K Day_Night 0
# train_model BDD10K No BDD10K Day 1
# train_model BDD10K No BDD10K Night 2

# BDD10K pretrain, pick Day weights, finetune on BDD10K
# # train_model Day BDD10K BDD10K CUT 0
# train_model Day BDD10K BDD10K MoNCE 1
# train_model Day BDD10K BDD10K TPSeNCE 2
# train_model Day BDD10K BDD10K CycleGAN-turbo 3
# train_model Day BDD10K BDD10K Instruct-pix2pix 0








# get OOM, wait for author response!!!
# # depth_anything pretrain, finetune on BDD10K (Need to fix this code, once test done)
# export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:32
# train_model depth_anything BDD10K BDD10K Day 0



# NOTE: these are the versions I use (mmengine >0.10.2 cause train stucks after dataloading!!!!!!)
# pip install -U openmim
# mim install mmengine==0.10.2
# mim install mmcv==2.0.0rc4
# pip install "mmdet>=3.0.0rc4"
# pip install -r requirements.txt
# pip install wandb