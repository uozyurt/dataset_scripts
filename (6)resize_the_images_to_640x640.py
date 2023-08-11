import os
import shutil
from PIL import Image


DATASET_SOURCE_PATH = "/home/umut/Desktop/AKONS_FINAL_DATASET/READY_DATASET"

DATA_SET_DEST_PATH = "/home/umut/Desktop/AKONS_FINAL_DATASET/READY_DATASET_640"

os.makedirs(DATA_SET_DEST_PATH, exist_ok=True)

for sub_dir_name in os.listdir(DATASET_SOURCE_PATH):
    sub_dir_images_path = os.path.join(DATASET_SOURCE_PATH, sub_dir_name, "images")
    
    os.makedirs(os.path.join(DATA_SET_DEST_PATH, sub_dir_name, "images"), exist_ok=True)

    for image_name in os.listdir(sub_dir_images_path):
        image_path = os.path.join(sub_dir_images_path, image_name)
        image = Image.open(image_path)

        resized_image = image.resize((640, 640))

        resized_image.save(os.path.join(DATA_SET_DEST_PATH, sub_dir_name, "images", image_name))


for sub_dir_name in os.listdir(DATASET_SOURCE_PATH):
    sub_dir_labels_path = os.path.join(DATASET_SOURCE_PATH, sub_dir_name, "labels")

    if not os.path.exists(sub_dir_labels_path):
        continue
    
    os.makedirs(os.path.join(DATA_SET_DEST_PATH, sub_dir_name, "labels"), exist_ok=True)

    for label_name in os.listdir(sub_dir_labels_path):
        save_path = os.path.join(DATA_SET_DEST_PATH, sub_dir_name, "labels", label_name)
        shutil.copy(os.path.join(sub_dir_labels_path, label_name), save_path)
