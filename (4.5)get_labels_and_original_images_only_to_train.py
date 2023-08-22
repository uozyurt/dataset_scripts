import os
import shutil
import glob
import utils.utils as utils

ROOT_PATH = "/home/umut/AKONS/AKONS_FINAL_DATASET/UNIFIED_DATASET_ONLY_TO_TRAIN"

ALL_IMAGES_PATH = "/home/umut/AKONS/AKONS_DATASET_OTHER/ALL_IMAGES_AKONS"
ALL_LABELS_PATH = "/home/umut/AKONS/AKONS_DATASET_OTHER/ALL_LABELS_DRONE_AIRCRAFT_HELICOPTER"

DEST_PATH = "/home/umut/AKONS/AKONS_FINAL_DATASET/DATASET_WITH_LABELS_ONLY_TO_TRAIN"

DEST_PATH_IMAGES = os.path.join(DEST_PATH, "images")
DEST_PATH_LABELS = os.path.join(DEST_PATH, "labels")

os.makedirs(DEST_PATH_IMAGES, exist_ok=True)
os.makedirs(DEST_PATH_LABELS, exist_ok=True)

POSTFIX = "_annotated"
IF_POSTFIX = True


for image_name in os.listdir(ROOT_PATH):

    if IF_POSTFIX:
        image_name_clean = image_name.replace(POSTFIX, "")
    else:
        image_name_clean = image_name


    image_path = os.path.join(ALL_IMAGES_PATH, image_name_clean)
    label_path = os.path.join(ALL_LABELS_PATH, utils.get_label_file_name(image_name_clean))

    shutil.copy(image_path, DEST_PATH_IMAGES)
    shutil.copy(label_path, DEST_PATH_LABELS)
