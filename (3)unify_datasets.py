import os
import shutil
import glob

ROOT_PATH = "/home/umut/Desktop/AKONS_FINAL_DATASET/CLEANED_PARTS_MERGED_WITH_BACKGROUNDS"

DEST_PATH = "/home/umut/Desktop/AKONS_FINAL_DATASET/UNIFIED_DATASET"

os.makedirs(DEST_PATH, exist_ok=True)

for image_path in glob.glob(os.path.join(ROOT_PATH, "**", "*")):
    shutil.copy(image_path, DEST_PATH)
