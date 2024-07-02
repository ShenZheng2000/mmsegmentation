# pip install pytorch-fid
# python -m pytorch_fid XXX YYY

######################### BDD10K (Day->Night) #########################
SRC="/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train_day"
TGT="/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train_night"

# # Day_Night
# echo "Testing Day_Night"
# python -m pytorch_fid $SRC "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train"
# python -m pytorch_fid $TGT "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train"

# # Day
# echo "Testing Day"
# python -m pytorch_fid $TGT $SRC

# Cityscapes
echo "Testing Cityscapes"
# python -m pytorch_fid $SRC "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Clean_Images/cityscapes/leftImg8bit_train_all_in_one_dir"
python -m pytorch_fid $TGT "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Clean_Images/cityscapes/leftImg8bit_train_all_in_one_dir"

# CUT
# echo "Testing CUT"
# python -m pytorch_fid $SRC "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train_night_CUT"
# python -m pytorch_fid $TGT "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train_night_CUT"

# # MoNCE
# echo "Testing MoNCE"
# python -m pytorch_fid $SRC "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train_night_MoNCE"
# python -m pytorch_fid $TGT "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train_night_MoNCE"


# # TPSeNCE
# echo "Testing TPSeNCE"
# python -m pytorch_fid $SRC "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train_night_TPSeNCE"
# python -m pytorch_fid $TGT "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train_night_TPSeNCE"


# # CycleGAN-turbo
# echo "Testing CycleGAN-turbo"
# python -m pytorch_fid $SRC "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train_night_CycleGAN-turbo"
# python -m pytorch_fid $TGT "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train_night_CycleGAN-turbo"

# # Instruct-pix2pix
# echo "Testing Instruct-pix2pix"
# python -m pytorch_fid $SRC "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train_night_Instruct-pix2pix"
# python -m pytorch_fid $TGT "/longdata/anurag_storage/2PCNet/LLIE/Dataset/Dark_Images/bdd100k/images/10k/train_night_Instruct-pix2pix"
