# NOTE: let's assume mask2former is the backbone

test_model() {
    PRETRAIN=$1
    FINETUNE=$2
    TEST_DATASET=$3
    I2I_MODEL=$4
    ITER=${5:-90000}
    
    if [ "$PRETRAIN" = "depth_anything" ]; then
        config_file="configs/mask2former/depth_anything/${TEST_DATASET}/${I2I_MODEL}.py"
    else
        config_file="configs/mask2former/${TEST_DATASET}/${I2I_MODEL}.py" # TODO: add Cityscapes to this before?
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
        echo 
    fi
    
    mkdir -p "${output_dir}"

    echo "Testing ${PRETRAIN}/${FINETUNE}/${TEST_DATASET} with ${I2I_MODEL}..."

    CUDA_VISIBLE_DEVICES=3 python tools/test.py \
        "$config_file" \
        "$checkpoint_path" \
        --out "${output_dir}/predictions" \
        --work-dir "${output_dir}"

    echo "Testing completed."
}

# NOTE: skip preprocess, and skip DCS for now

# ############### Cityscapes ###############
# test_model "Cityscapes" "No" "Cityscapes" "No"
# test_model "Cityscapes" "Cityscapes" "Cityscapes" "CUT"
# test_model "Cityscapes" "Cityscapes" "Cityscapes" "MoNCE"
# test_model "Cityscapes" "Cityscapes" "Cityscapes" "TPSeNCE"
# test_model "Cityscapes" "Cityscapes" "Cityscapes" "CycleGAN-turbo"
# test_model "Cityscapes" "Cityscapes" "Cityscapes" "Instruct-pix2pix"

# test_model "Cityscapes" "BDD10K" "Cityscapes" "Night" "90000" # Night just for testing config placeholder
test_model "Cityscapes" "NightCity" "Cityscapes" "Night" "110000" # Night just for testing config placeholder

# test_model "depth_anything" "No" "Cityscapes" "No" 



# # ############### BDD10K ###############
# test_model "Cityscapes" "No" "BDD10K" "No"
# test_model "Cityscapes" "BDD10K" "BDD10K" "Day_Night" "95000"
# test_model "Cityscapes" "BDD10K" "BDD10K" "Day" "100000"
# test_model "Cityscapes" "BDD10K" "BDD10K" "Night" "90000"
# test_model "Cityscapes" "BDD10K" "BDD10K" "CUT" "100000"
# test_model "Cityscapes" "BDD10K" "BDD10K" "MoNCE" "95000"
# test_model "Cityscapes" "BDD10K" "BDD10K" "TPSeNCE" "100000"
# test_model "Cityscapes" "BDD10K" "BDD10K" "CycleGAN-turbo" "95000"
# test_model "Cityscapes" "BDD10K" "BDD10K" "Instruct-pix2pix" "100000"

# test_model "Cityscapes" "NightCity" "BDD10K" "Night" "110000"

# test_model "depth_anything" "No" "BDD10K" "No"



# # ############### Night_Driving ###############
# test_model "Cityscapes" "No" "Night_Driving" "No"
# test_model "Cityscapes" "Cityscapes" "Night_Driving" "CUT"
# test_model "Cityscapes" "Cityscapes" "Night_Driving" "MoNCE"
# test_model "Cityscapes" "Cityscapes" "Night_Driving" "TPSeNCE"
# test_model "Cityscapes" "Cityscapes" "Night_Driving" "CycleGAN-turbo"
# test_model "Cityscapes" "Cityscapes" "Night_Driving" "Instruct-pix2pix"

# test_model "Cityscapes" "BDD10K" "Night_Driving" "Day_Night" "95000"
# test_model "Cityscapes" "BDD10K" "Night_Driving" "Day" "100000"
# test_model "Cityscapes" "BDD10K" "Night_Driving" "Night"  "90000"
# test_model "Cityscapes" "BDD10K" "Night_Driving" "CUT" "100000"
# test_model "Cityscapes" "BDD10K" "Night_Driving" "MoNCE" "95000"
# test_model "Cityscapes" "BDD10K" "Night_Driving" "TPSeNCE" "100000"
# test_model "Cityscapes" "BDD10K" "Night_Driving" "CycleGAN-turbo" "95000"
# test_model "Cityscapes" "BDD10K" "Night_Driving" "Instruct-pix2pix" "100000"

# test_model "Cityscapes" "NightCity" "Night_Driving" "Night" "110000"

# test_model "BDD10K" "No" "Night_Driving" "Day_Night" "30000"
# test_model "BDD10K" "No" "Night_Driving" "Day" "80000"
# test_model "BDD10K" "No" "Night_Driving" "Night" "10000"
# test_model "Day" "BDD10K" "Night_Driving" "CUT" "90000"
# test_model "Day" "BDD10K" "Night_Driving" "MoNCE" "95000"
# test_model "Day" "BDD10K" "Night_Driving" "TPSeNCE" "100000"
# test_model "Day" "BDD10K" "Night_Driving" "CycleGAN-turbo" "95000"
# test_model "Day" "BDD10K" "Night_Driving" "Instruct-pix2pix" "90000"

# test_model "depth_anything" "No" "Night_Driving" "No"




# ############### Dark_Zurich ###############
# test_model "Cityscapes" "No" "Dark_Zurich" "No"
# test_model "Cityscapes" "Cityscapes" "Dark_Zurich" "CUT"
# test_model "Cityscapes" "Cityscapes" "Dark_Zurich" "MoNCE"
# test_model "Cityscapes" "Cityscapes" "Dark_Zurich" "TPSeNCE"
# test_model "Cityscapes" "Cityscapes" "Dark_Zurich" "CycleGAN-turbo"
# test_model "Cityscapes" "Cityscapes" "Dark_Zurich" "Instruct-pix2pix"

# test_model "Cityscapes" "BDD10K" "Dark_Zurich" "Day_Night" "95000"
# test_model "Cityscapes" "BDD10K" "Dark_Zurich" "Day" "100000"
# test_model "Cityscapes" "BDD10K" "Dark_Zurich" "Night"  "90000"
# test_model "Cityscapes" "BDD10K" "Dark_Zurich" "CUT" "100000"
# test_model "Cityscapes" "BDD10K" "Dark_Zurich" "MoNCE" "95000"
# test_model "Cityscapes" "BDD10K" "Dark_Zurich" "TPSeNCE" "100000"
# test_model "Cityscapes" "BDD10K" "Dark_Zurich" "CycleGAN-turbo" "95000"
# test_model "Cityscapes" "BDD10K" "Dark_Zurich" "Instruct-pix2pix" "100000"

# test_model "Cityscapes" "NightCity" "Dark_Zurich" "Night" "110000"

# test_model "BDD10K" "No" "Dark_Zurich" "Day_Night" "30000"
# test_model "BDD10K" "No" "Dark_Zurich" "Day" "80000"
# test_model "BDD10K" "No" "Dark_Zurich" "Night" "10000"
# test_model "Day" "BDD10K" "Dark_Zurich" "CUT" "90000"
# test_model "Day" "BDD10K" "Dark_Zurich" "MoNCE" "95000"
# test_model "Day" "BDD10K" "Dark_Zurich" "TPSeNCE" "100000"
# test_model "Day" "BDD10K" "Dark_Zurich" "CycleGAN-turbo" "95000"
# test_model "Day" "BDD10K" "Dark_Zurich" "Instruct-pix2pix" "90000"

# test_model "depth_anything" "No" "Dark_Zurich" "No"




# ############### ACDC ###############
# test_model "Cityscapes" "No" "ACDC" "No"
# test_model "Cityscapes" "Cityscapes" "ACDC" "CUT"
# test_model "Cityscapes" "Cityscapes" "ACDC" "MoNCE"
# test_model "Cityscapes" "Cityscapes" "ACDC" "TPSeNCE"
# test_model "Cityscapes" "Cityscapes" "ACDC" "CycleGAN-turbo"
# test_model "Cityscapes" "Cityscapes" "ACDC" "Instruct-pix2pix"

# test_model "Cityscapes" "BDD10K" "ACDC" "Day_Night"  "95000"
# test_model "Cityscapes" "BDD10K" "ACDC" "Day" "100000"
# test_model "Cityscapes" "BDD10K" "ACDC" "Night"  "90000"
# test_model "Cityscapes" "BDD10K" "ACDC" "CUT" "100000"
# test_model "Cityscapes" "BDD10K" "ACDC" "MoNCE" "95000"
# test_model "Cityscapes" "BDD10K" "ACDC" "TPSeNCE" "100000"
# test_model "Cityscapes" "BDD10K" "ACDC" "CycleGAN-turbo" "95000"
# test_model "Cityscapes" "BDD10K" "ACDC" "Instruct-pix2pix" "100000"

# test_model "Cityscapes" "NightCity" "ACDC" "Night" "110000"

# test_model "BDD10K" "No" "ACDC" "Day_Night" "30000"
# test_model "BDD10K" "No" "ACDC" "Day" "80000"
# test_model "BDD10K" "No" "ACDC" "Night" "10000"
# test_model "Day" "BDD10K" "ACDC" "CUT" "90000"
# test_model "Day" "BDD10K" "ACDC" "MoNCE" "95000"
# test_model "Day" "BDD10K" "ACDC" "TPSeNCE" "100000"
# test_model "Day" "BDD10K" "ACDC" "CycleGAN-turbo" "95000"
# test_model "Day" "BDD10K" "ACDC" "Instruct-pix2pix" "90000"

# test_model "depth_anything" "No" "ACDC" "No"



############### NightCity ###############
# test_model "Cityscapes" "No" "NightCity" "No"

# test_model "Cityscapes" "Cityscapes" "NightCity" "CUT"
# test_model "Cityscapes" "Cityscapes" "NightCity" "MoNCE"
# test_model "Cityscapes" "Cityscapes" "NightCity" "TPSeNCE"
# test_model "Cityscapes" "Cityscapes" "NightCity" "CycleGAN-turbo"
# test_model "Cityscapes" "Cityscapes" "NightCity" "Instruct-pix2pix"


# test_model "Cityscapes" "BDD10K" "NightCity" "Day_Night" "95000"
# test_model "Cityscapes" "BDD10K" "NightCity" "Day" "100000"
# test_model "Cityscapes" "BDD10K" "NightCity" "Night" "90000"
# test_model "Cityscapes" "BDD10K" "NightCity" "CUT" "100000"
# test_model "Cityscapes" "BDD10K" "NightCity" "MoNCE" "95000"
# test_model "Cityscapes" "BDD10K" "NightCity" "TPSeNCE" "100000"
# test_model "Cityscapes" "BDD10K" "NightCity" "CycleGAN-turbo" "95000"
# test_model "Cityscapes" "BDD10K" "NightCity" "Instruct-pix2pix" "100000"

# test_model "Cityscapes" "NightCity" "NightCity" "No" "110000"


# test_model "BDD10K" "No" "NightCity" "Day_Night" "30000"
# test_model "BDD10K" "No" "NightCity" "Day" "80000"
# test_model "BDD10K" "No" "NightCity" "Night" "10000"
# test_model "Day" "BDD10K" "NightCity" "CUT" "90000"
# test_model "Day" "BDD10K" "NightCity" "MoNCE" "95000"
# test_model "Day" "BDD10K" "NightCity" "TPSeNCE" "100000"
# test_model "Day" "BDD10K" "NightCity" "CycleGAN-turbo" "95000"
# test_model "Day" "BDD10K" "NightCity" "Instruct-pix2pix" "90000"

# test_model "depth_anything" "No" "NightCity" "No"








############### DCS ###############
# seg_test "DCS" "Clean"
# seg_test "DCS" "Dark"
# seg_test "DCS" "LLFlow"
# seg_test "DCS" "RUAS"
# seg_test "DCS" "SCI"
# seg_test "DCS" "SGZ" => Skip due to size mismatch
# seg_test "DCS" "ZeroDCE"
# seg_test "DCS" "CLIP_LIT"
# seg_test "DCS" "NeRCo"
# seg_test "DCS" "RetinexFormer"
# seg_test "DCS" "DiffLL"
# seg_test "DCS" "SKF"
# seg_test "DCS" "PairLIE"
# seg_test "DCS" "CUT" "work_dirs/Cityscapes/CUT/iter_90000.pth"
# seg_test "DCS" "MoNCE" "work_dirs/Cityscapes/MoNCE/iter_90000.pth"
# seg_test "DCS" "TPSeNCE" "work_dirs/Cityscapes/TPSeNCE/iter_90000.pth"
# seg_test "DCS" "CycleGAN-turbo" "work_dirs/Cityscapes/CycleGAN-turbo/iter_90000.pth"
# seg_test "DCS" "Instruct-pix2pix" "work_dirs/Cityscapes/Instruct-pix2pix/iter_90000.pth"