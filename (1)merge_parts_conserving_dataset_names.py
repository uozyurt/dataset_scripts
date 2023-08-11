import os
import shutil


"""
START THIS PIPELINE FROM HERE, CONTINUE WITH (2), (3) ...

THE FORMAT HAS TO BE LIKE THIS: Part names are not important, but dataset names are important.
Also the "0_object(background)" and "1_or_more_object" folder names are important and can be changed in the code. Although, they should be same in all datasets.




ROOT_PATH:
    PART_1:
        DATASET_1:
            0_object(background):
                background_image_1.jpg
                background_image_2.jpg
                ...
            1_or_more_object:
                normal_image_1.jpg
                normal_image_2.jpg
                ...
        DATASET_2:
            ...
    PART_2:
        ...
    ...



"""




ROOT_PATH = "/home/umut/Desktop/AKONS_FINAL_DATASET/CLEANED_PARTS"

DEST_PATH = "/home/umut/Desktop/AKONS_FINAL_DATASET/CLEANED_PARTS_MERGED"


all_dataset_names = []

BACKGROUND_FOLDER_NAME = "0_object(background)"
NORMAL_IMAGES_FOLDER_NAME = "1_or_more_object"


for part_name in os.listdir(ROOT_PATH):
    for dataset_name in os.listdir(os.path.join(ROOT_PATH, part_name)):
        all_dataset_names.append(dataset_name)

all_dataset_names = list(set(all_dataset_names))

for dataset_name in all_dataset_names:
    dataset_path = os.path.join(DEST_PATH, dataset_name)
    os.makedirs(os.path.join(dataset_path, BACKGROUND_FOLDER_NAME), exist_ok=True)
    os.makedirs(os.path.join(dataset_path, NORMAL_IMAGES_FOLDER_NAME), exist_ok=True)


for part_name in os.listdir(ROOT_PATH):
    part_path = os.path.join(ROOT_PATH, part_name)
    for dataset_name in os.listdir(part_path):
        dest_path = os.path.join(DEST_PATH, dataset_name)
        src_path = os.path.join(part_path, dataset_name)
        for file_name in os.listdir(os.path.join(src_path, BACKGROUND_FOLDER_NAME)):
            file_path = os.path.join(src_path, BACKGROUND_FOLDER_NAME, file_name)
            final_dest_path = os.path.join(dest_path, BACKGROUND_FOLDER_NAME, file_name)
            shutil.copy(file_path, final_dest_path)
        
        for file_name in os.listdir(os.path.join(src_path, NORMAL_IMAGES_FOLDER_NAME)):
            file_path = os.path.join(src_path, NORMAL_IMAGES_FOLDER_NAME, file_name)
            final_dest_path = os.path.join(dest_path, NORMAL_IMAGES_FOLDER_NAME, file_name)
            shutil.copy(file_path, final_dest_path)
        



















