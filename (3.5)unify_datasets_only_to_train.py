import os
import shutil
import glob

ROOT_PATH = "/home/umut/Desktop/AKONS_FINAL_DATASET/ONLY_TO_TRAIN_DATASETS"

DEST_PATH = "/home/umut/Desktop/AKONS_FINAL_DATASET/UNIFIED_DATASET_ONLY_TO_TRAIN"

os.makedirs(DEST_PATH, exist_ok=True)

for image_path in glob.glob(os.path.join(ROOT_PATH, "**", "*")):
    shutil.copy(image_path, DEST_PATH)
