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
