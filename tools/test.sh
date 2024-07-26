# NOTE: let's assume mask2former is the backbone

test_model() {
    PRETRAIN=$1
    FINETUNE=$2
    TEST_DATASET=$3
    I2I_MODEL=$4
    ITER=${5:-90000}
    TEST_CONFIG=${6:-""}  # <-- This line is added to accept an optional TEST_CONFIG argument

    if [ "$PRETRAIN" = "depth_anything" ]; then
        config_file="configs/mask2former/depth_anything/${TEST_DATASET}/${I2I_MODEL}.py"
    else
        config_file="configs/mask2former/${TEST_DATASET}/${I2I_MODEL}.py"
    fi

    if [ -n "$TEST_CONFIG" ]; then
        test_config_file="configs/mask2former/${TEST_DATASET}/${TEST_CONFIG}.py"  # <-- This line is added
    else
        test_config_file="$config_file"  # <-- This line is added
    fi

    output_dir="work_dirs/${PRETRAIN}/${FINETUNE}/${TEST_DATASET}/${I2I_MODEL}"

    if [ "$PRETRAIN" = "Cityscapes" ] && [ "$FINETUNE" = "No" ]; then
        checkpoint_path="pretrained/mask2former_swin-l-in22k-384x384-pre_8xb2-90k_cityscapes-512x1024_20221202_141901-28ad20f1.pth"
    elif [ "$PRETRAIN" = "BDD10K" ] && [ "$FINETUNE" = "No" ]; then
        checkpoint_path="work_dirs/BDD10K/No/BDD10K/${I2I_MODEL}/iter_${ITER}.pth"
    elif [ "$PRETRAIN" = "depth_anything" ] && [ "$FINETUNE" = "No" ]; then
        checkpoint_path="checkpoints/cityscapes_vitl_mIoU_86.4.pth"
    else
        checkpoint_path="work_dirs/${PRETRAIN}/${FINETUNE}/${FINETUNE}/${I2I_MODEL}/iter_${ITER}.pth" # NOTE: use double FINETUNE here to get the correct path
    fi

    mkdir -p "${output_dir}"

    echo "Testing ${PRETRAIN}/${FINETUNE}/${TEST_DATASET} with ${I2I_MODEL}..."

    CUDA_VISIBLE_DEVICES=3 python tools/test.py \
        "$test_config_file" \
        "$checkpoint_path" \
        --out "${output_dir}/predictions" \
        --work-dir "${output_dir}"

    echo "Testing completed."
}



# ############### Cityscapes ###############

# Pretrain
# test_model "Cityscapes" "No" "Cityscapes" "No"

# Finetuning
# test_model "Cityscapes" "BDD10K" "Cityscapes" "Day_Night" "95000" 
# test_model "Cityscapes" "BDD10K" "Cityscapes" "Day" "100000"
# test_model "Cityscapes" "BDD10K" "Cityscapes" "Night" "90000"
# test_model "Cityscapes" "NightCity" "Cityscapes" "Night" "110000"
# test_model "Cityscapes" "Cityscapes" "Cityscapes" "CUT"
# test_model "Cityscapes" "Cityscapes" "Cityscapes" "MoNCE"
# test_model "Cityscapes" "Cityscapes" "Cityscapes" "TPSeNCE"
# test_model "Cityscapes" "Cityscapes" "Cityscapes" "CycleGAN-turbo"
# test_model "Cityscapes" "Cityscapes" "Cityscapes" "Instruct-pix2pix"

# # Finetuning in BDD10K Images
# test_model "Cityscapes" "BDD10K" "Cityscapes" "CUT" "100000"
# test_model "Cityscapes" "BDD10K" "Cityscapes" "MoNCE" "95000"
# test_model "Cityscapes" "BDD10K" "Cityscapes" "TPSeNCE" "100000"
# test_model "Cityscapes" "BDD10K" "Cityscapes" "CycleGAN-turbo" "95000"
# test_model "Cityscapes" "BDD10K" "Cityscapes" "Instruct-pix2pix" "100000"


# Preprocessing
# test_model "Cityscapes" "No" "Cityscapes" "RUAS"
# test_model "Cityscapes" "No" "Cityscapes" "SCI"
# test_model "Cityscapes" "No" "Cityscapes" "RetinexFormer"
# test_model "Cityscapes" "No" "Cityscapes" "SKF"
# test_model "Cityscapes" "No" "Cityscapes" "LLFlow"
# test_model "Cityscapes" "No" "Cityscapes" "NeRCo"
# test_model "Cityscapes" "No" "Cityscapes" "ZeroDCE"
# test_model "Cityscapes" "No" "Cityscapes" "CLIP_LIT"
# test_model "Cityscapes" "No" "Cityscapes" "PairLIE"
# test_model "Cityscapes" "No" "Cityscapes" "DiffLL"

# Large Pretrain
# test_model "depth_anything" "No" "Cityscapes" "No"

# Tuning freeze stages
# test_model "Cityscapes" "BDD10K" "Cityscapes" "Day_Night_freeze_stage_1_110k" "100000"
# test_model "Cityscapes" "BDD10K" "Cityscapes" "Day_Night_freeze_stage_2_110k" "105000"
# test_model "Cityscapes" "BDD10K" "Cityscapes" "Day_Night_freeze_stage_3_110k" "105000"
# test_model "Cityscapes" "BDD10K" "Cityscapes" "Day_Night_freeze_stage_4_110k" "105000"

# Tuning mixing images
# test_model "Cityscapes" "BDD10K" "Cityscapes" "Day_and_Cityscapes_total_iter_110k" "95000" "Day_Night" # placeholder for TEST_CONFIG argument


# # ############### BDD10K (Night) ##############

# Pretrain
# test_model "Cityscapes" "No" "BDD10K" "No"

# Finetuning
# test_model "Cityscapes" "BDD10K" "BDD10K" "Day_Night" "95000"
# test_model "Cityscapes" "BDD10K" "BDD10K" "Day" "100000"
# test_model "Cityscapes" "BDD10K" "BDD10K" "Night" "90000"
# test_model "Cityscapes" "NightCity" "BDD10K" "Night" "110000"
# test_model "Cityscapes" "Cityscapes" "BDD10K" "CUT"
# test_model "Cityscapes" "Cityscapes" "BDD10K" "MoNCE"
# test_model "Cityscapes" "Cityscapes" "BDD10K" "TPSeNCE"
# test_model "Cityscapes" "Cityscapes" "BDD10K" "CycleGAN-turbo"
# test_model "Cityscapes" "Cityscapes" "BDD10K" "Instruct-pix2pix"

# Finetuning (NOTE: check test_6_21_bk.sh for more details about I2I on BDD10K images)
# test_model "Cityscapes" "BDD10K" "BDD10K" "TPSeNCE_2" "100000"


# Preprocessing
# test_model "Cityscapes" "No" "BDD10K" "RUAS"
# test_model "Cityscapes" "No" "BDD10K" "SCI"
# test_model "Cityscapes" "No" "BDD10K" "RetinexFormer"
# test_model "Cityscapes" "No" "BDD10K" "SKF"
# test_model "Cityscapes" "No" "BDD10K" "LLFlow"
# test_model "Cityscapes" "No" "BDD10K" "NeRCo"
# test_model "Cityscapes" "No" "BDD10K" "ZeroDCE"
# test_model "Cityscapes" "No" "BDD10K" "CLIP_LIT"
# test_model "Cityscapes" "No" "BDD10K" "PairLIE"
# test_model "Cityscapes" "No" "BDD10K" "DiffLL"
# test_model "Cityscapes" "No" "BDD10K" "CycleGAN-turbo_b2a" # reverse way for preprocessing


# Large Pretrain
# test_model "depth_anything" "No" "BDD10K" "No"

# Tuning mixing images
# test_model "Cityscapes" "BDD10K" "BDD10K" "Day_and_Cityscapes_total_iter_110k" "95000" "Day_Night" # placeholder for TEST_CONFIG argument



# # ############### Night_Driving ###############

# Pretrain
# test_model "Cityscapes" "No" "Night_Driving" "No"

# Finetuning
# test_model "Cityscapes" "BDD10K" "Night_Driving" "Day_Night" "95000"
# test_model "Cityscapes" "BDD10K" "Night_Driving" "Day" "100000"
# test_model "Cityscapes" "BDD10K" "Night_Driving" "Night"  "90000"
# test_model "Cityscapes" "Cityscapes" "Night_Driving" "CUT"
# test_model "Cityscapes" "Cityscapes" "Night_Driving" "MoNCE"
# test_model "Cityscapes" "Cityscapes" "Night_Driving" "TPSeNCE"
# test_model "Cityscapes" "Cityscapes" "Night_Driving" "CycleGAN-turbo"
# test_model "Cityscapes" "Cityscapes" "Night_Driving" "Instruct-pix2pix"
# test_model "Cityscapes" "NightCity" "Night_Driving" "Night" "110000"

# Preprocessing
# test_model "Cityscapes" "No" "Night_Driving" "RUAS"
# test_model "Cityscapes" "No" "Night_Driving" "SCI"
# test_model "Cityscapes" "No" "Night_Driving" "RetinexFormer"
# test_model "Cityscapes" "No" "Night_Driving" "SKF"
# test_model "Cityscapes" "No" "Night_Driving" "LLFlow"
# test_model "Cityscapes" "No" "Night_Driving" "NeRCo"
# test_model "Cityscapes" "No" "Night_Driving" "ZeroDCE"
# test_model "Cityscapes" "No" "Night_Driving" "CLIP_LIT"
# test_model "Cityscapes" "No" "Night_Driving" "PairLIE"
# test_model "Cityscapes" "No" "Night_Driving" "DiffLL"
# test_model "Cityscapes" "No" "Night_Driving" "CycleGAN-turbo_b2a" # reverse way for preprocessing

# Large Pretrain
# test_model "depth_anything" "No" "Night_Driving" "No"

# test_model "Cityscapes" "BDD10K" "Night_Driving" "Day_Night_freeze_stage_1_110k" "100000"
# test_model "Cityscapes" "BDD10K" "Night_Driving" "Day_Night_freeze_stage_2_110k" "105000"
# test_model "Cityscapes" "BDD10K" "Night_Driving" "Day_Night_freeze_stage_3_110k" "105000"
# test_model "Cityscapes" "BDD10K" "Night_Driving" "Day_Night_freeze_stage_4_110k" "105000"


# Tuning mixing images
# test_model "Cityscapes" "BDD10K" "Night_Driving" "Day_and_Cityscapes_total_iter_110k" "95000" "Day_Night" # placeholder for TEST_CONFIG argument


# ############### Dark_Zurich ###############

# Pretrain
# test_model "Cityscapes" "No" "Dark_Zurich" "No"

# Finetuning
# test_model "Cityscapes" "BDD10K" "Dark_Zurich" "Day_Night" "95000"
# test_model "Cityscapes" "BDD10K" "Dark_Zurich" "Day" "100000"
# test_model "Cityscapes" "BDD10K" "Dark_Zurich" "Night"  "90000"
# test_model "Cityscapes" "Cityscapes" "Dark_Zurich" "CUT"
# test_model "Cityscapes" "Cityscapes" "Dark_Zurich" "MoNCE"
# test_model "Cityscapes" "Cityscapes" "Dark_Zurich" "TPSeNCE"
# test_model "Cityscapes" "Cityscapes" "Dark_Zurich" "CycleGAN-turbo"
# test_model "Cityscapes" "Cityscapes" "Dark_Zurich" "Instruct-pix2pix"
# test_model "Cityscapes" "NightCity" "Dark_Zurich" "Night" "110000"

# Preprocessing
# test_model "Cityscapes" "No" "Dark_Zurich" "RUAS"
# test_model "Cityscapes" "No" "Dark_Zurich" "SCI"
# test_model "Cityscapes" "No" "Dark_Zurich" "RetinexFormer"
# test_model "Cityscapes" "No" "Dark_Zurich" "SKF"
# test_model "Cityscapes" "No" "Dark_Zurich" "LLFlow"
# test_model "Cityscapes" "No" "Dark_Zurich" "NeRCo"
# test_model "Cityscapes" "No" "Dark_Zurich" "ZeroDCE"
# test_model "Cityscapes" "No" "Dark_Zurich" "CLIP_LIT"
# test_model "Cityscapes" "No" "Dark_Zurich" "PairLIE"
# test_model "Cityscapes" "No" "Dark_Zurich" "DiffLL"
# test_model "Cityscapes" "No" "Dark_Zurich" "CycleGAN-turbo_b2a" # reverse way for preprocessing

# Large Pretrain
# test_model "depth_anything" "No" "Dark_Zurich" "No"

# test_model "Cityscapes" "BDD10K" "Dark_Zurich" "Day_Night_freeze_stage_1_110k" "100000"
# test_model "Cityscapes" "BDD10K" "Dark_Zurich" "Day_Night_freeze_stage_2_110k" "105000"
# test_model "Cityscapes" "BDD10K" "Dark_Zurich" "Day_Night_freeze_stage_3_110k" "105000"
# test_model "Cityscapes" "BDD10K" "Dark_Zurich" "Day_Night_freeze_stage_4_110k" "105000"


# Tuning mixing images
# test_model "Cityscapes" "BDD10K" "Dark_Zurich" "Day_and_Cityscapes_total_iter_110k" "95000" "Day_Night" # placeholder for TEST_CONFIG argument


# ############### ACDC (Night) ###############

# Pretrain
# test_model "Cityscapes" "No" "ACDC" "No"

# Finetuning
# test_model "Cityscapes" "BDD10K" "ACDC" "Day_Night"  "95000"
# test_model "Cityscapes" "BDD10K" "ACDC" "Day" "100000"
# test_model "Cityscapes" "BDD10K" "ACDC" "Night"  "90000"
# test_model "Cityscapes" "Cityscapes" "ACDC" "CUT"
# test_model "Cityscapes" "Cityscapes" "ACDC" "MoNCE"
# test_model "Cityscapes" "Cityscapes" "ACDC" "TPSeNCE"
# test_model "Cityscapes" "Cityscapes" "ACDC" "CycleGAN-turbo"
# test_model "Cityscapes" "Cityscapes" "ACDC" "Instruct-pix2pix"
# test_model "Cityscapes" "NightCity" "ACDC" "Night" "110000"

# Preprocessing
test_model "Cityscapes" "No" "ACDC" "RUAS"
test_model "Cityscapes" "No" "ACDC" "SCI"
test_model "Cityscapes" "No" "ACDC" "RetinexFormer"
test_model "Cityscapes" "No" "ACDC" "SKF"
test_model "Cityscapes" "No" "ACDC" "LLFlow"
test_model "Cityscapes" "No" "ACDC" "NeRCo"
test_model "Cityscapes" "No" "ACDC" "ZeroDCE"
test_model "Cityscapes" "No" "ACDC" "CLIP_LIT"
test_model "Cityscapes" "No" "ACDC" "PairLIE"
test_model "Cityscapes" "No" "ACDC" "DiffLL"
# test_model "Cityscapes" "No" "ACDC" "CycleGAN-turbo_b2a" # reverse way for preprocessing

# Large Pretrain
# test_model "depth_anything" "No" "ACDC" "No"

# test_model "Cityscapes" "BDD10K" "ACDC" "Day_Night_freeze_stage_1_110k" "100000"
# test_model "Cityscapes" "BDD10K" "ACDC" "Day_Night_freeze_stage_2_110k" "105000"
# test_model "Cityscapes" "BDD10K" "ACDC" "Day_Night_freeze_stage_3_110k" "105000"
# test_model "Cityscapes" "BDD10K" "ACDC" "Day_Night_freeze_stage_4_110k" "105000"

# Tuning mixing images
# test_model "Cityscapes" "BDD10K" "ACDC" "Day_and_Cityscapes_total_iter_110k" "95000" "Day_Night" # placeholder for TEST_CONFIG argument


############### NightCity ###############

# Pretrain
# test_model "Cityscapes" "No" "NightCity" "No"

# Finetuning
# test_model "Cityscapes" "BDD10K" "NightCity" "Day_Night" "95000"
# test_model "Cityscapes" "BDD10K" "NightCity" "Day" "100000"
# test_model "Cityscapes" "BDD10K" "NightCity" "Night" "90000"
# test_model "Cityscapes" "Cityscapes" "NightCity" "CUT"
# test_model "Cityscapes" "Cityscapes" "NightCity" "MoNCE"
# test_model "Cityscapes" "Cityscapes" "NightCity" "TPSeNCE"
# test_model "Cityscapes" "Cityscapes" "NightCity" "CycleGAN-turbo"
# test_model "Cityscapes" "Cityscapes" "NightCity" "Instruct-pix2pix"
# test_model "Cityscapes" "NightCity" "NightCity" "No" "110000"

# Preprocessing
# test_model "Cityscapes" "No" "NightCity" "RUAS"
# test_model "Cityscapes" "No" "NightCity" "SCI"
# test_model "Cityscapes" "No" "NightCity" "RetinexFormer"
# test_model "Cityscapes" "No" "NightCity" "SKF"
# test_model "Cityscapes" "No" "NightCity" "LLFlow"
# test_model "Cityscapes" "No" "NightCity" "NeRCo"
# test_model "Cityscapes" "No" "NightCity" "ZeroDCE"
# test_model "Cityscapes" "No" "NightCity" "CLIP_LIT"
# test_model "Cityscapes" "No" "NightCity" "PairLIE"
# test_model "Cityscapes" "No" "NightCity" "DiffLL"
# test_model "Cityscapes" "No" "NightCity" "CycleGAN-turbo_b2a" # reverse way for preprocessing

# Large Pretrain
# test_model "depth_anything" "No" "NightCity" "No"

# test_model "Cityscapes" "BDD10K" "NightCity" "Day_Night_freeze_stage_1_110k" "100000"
# test_model "Cityscapes" "BDD10K" "NightCity" "Day_Night_freeze_stage_2_110k" "105000"
# test_model "Cityscapes" "BDD10K" "NightCity" "Day_Night_freeze_stage_3_110k" "105000"
# test_model "Cityscapes" "BDD10K" "NightCity" "Day_Night_freeze_stage_4_110k" "105000"

# Tuning mixing images
# test_model "Cityscapes" "BDD10K" "NightCity" "Day_and_Cityscapes_total_iter_110k" "95000" "Day_Night" # placeholder for TEST_CONFIG argument