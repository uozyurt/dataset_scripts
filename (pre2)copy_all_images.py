import glob
import shutil
import os

DATASET_ROOT_PATH = "/home/umut/Desktop/AKONS_DATASET_OTHER/AKONS_TRAINING_DATASET"


DEST_PATH = "/home/umut/Desktop/AKONS_DATASET_OTHER/ALL_IMAGES_AKONS"

os.makedirs(DEST_PATH, exist_ok=True)


for label_path in (glob.glob(os.path.join(DATASET_ROOT_PATH, "**/**/images/*"), recursive=True)):
    shutil.copy(label_path, DEST_PATH)






