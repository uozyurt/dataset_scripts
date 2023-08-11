import os
import shutil
import random
import glob

BACKGROUNDS_INCLUDE_PERCENT = 1

ROOT_PATH = "/home/umut/Desktop/AKONS_FINAL_DATASET/CLEANED_PARTS_MERGED"
DEST_PATH = "/home/umut/Desktop/AKONS_FINAL_DATASET/CLEANED_PARTS_MERGED_WITH_BACKGROUNDS"

os.makedirs(DEST_PATH, exist_ok=True)

for dataset_name in os.listdir(ROOT_PATH):
    background_elements = glob.glob(os.path.join(ROOT_PATH, dataset_name, "0_object(background)", "*"))
    wanted_background_elements = random.sample(background_elements, int(len(background_elements) * BACKGROUNDS_INCLUDE_PERCENT))
    normal_elements = glob.glob(os.path.join(ROOT_PATH, dataset_name, "1_or_more_object", "*"))

    save_path = os.path.join(DEST_PATH, dataset_name)
    os.makedirs(save_path, exist_ok=True)

    print(f"In {dataset_name}".ljust(65) + f", found {len(wanted_background_elements)}".ljust(14) + f"background images,{len(normal_elements)}".ljust(32) + "normal images")

    for element in wanted_background_elements:
        shutil.copy(element, save_path)

    for element in normal_elements:
        shutil.copy(element, save_path)












