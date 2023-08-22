import os
import shutil
import random

DATASET_SOURCE_PATH = "/home/umut/AKONS/AKONS_FINAL_DATASET/DATASET_WITH_LABELS"
DATASET_ONLY_TO_TRAIN_SOURCE_PATH = "/home/umut/AKONS/AKONS_FINAL_DATASET/DATASET_WITH_LABELS_ONLY_TO_TRAIN"

DATA_SET_DEST_PATH = "/home/umut/AKONS/AKONS_FINAL_DATASET/READY_DATASET"


DATA_SET_DEST_PATH_TRAIN = os.path.join(DATA_SET_DEST_PATH, "train")
DATA_SET_DEST_PATH_VAL = os.path.join(DATA_SET_DEST_PATH, "val")
DATA_SET_DEST_PATH_TEST = os.path.join(DATA_SET_DEST_PATH, "test")


DATA_SET_DEST_PATH_TRAIN_IMAGES = os.path.join(DATA_SET_DEST_PATH_TRAIN, "images")
DATA_SET_DEST_PATH_TRAIN_LABELS = os.path.join(DATA_SET_DEST_PATH_TRAIN, "labels")

DATA_SET_DEST_PATH_VAL_IMAGES = os.path.join(DATA_SET_DEST_PATH_VAL, "images")
DATA_SET_DEST_PATH_VAL_LABELS = os.path.join(DATA_SET_DEST_PATH_VAL, "labels")

DATA_SET_DEST_PATH_TEST_IMAGES = os.path.join(DATA_SET_DEST_PATH_TEST, "images")
DATA_SET_DEST_PATH_TEST_LABELS = os.path.join(DATA_SET_DEST_PATH_TEST, "labels")

os.makedirs(DATA_SET_DEST_PATH_TRAIN_IMAGES, exist_ok=True)
os.makedirs(DATA_SET_DEST_PATH_TRAIN_LABELS, exist_ok=True)

os.makedirs(DATA_SET_DEST_PATH_VAL_IMAGES, exist_ok=True)
os.makedirs(DATA_SET_DEST_PATH_VAL_LABELS, exist_ok=True)

os.makedirs(DATA_SET_DEST_PATH_TEST_IMAGES, exist_ok=True)
os.makedirs(DATA_SET_DEST_PATH_TEST_LABELS, exist_ok=True)


dataset_path_images = os.path.join(DATASET_SOURCE_PATH, "images")
dataset_path_labels = os.path.join(DATASET_SOURCE_PATH, "labels")

dataset_only_to_train_path_images = os.path.join(DATASET_ONLY_TO_TRAIN_SOURCE_PATH, "images")
dataset_only_to_train_path_labels = os.path.join(DATASET_ONLY_TO_TRAIN_SOURCE_PATH, "labels")

os.makedirs(dataset_path_images, exist_ok=True)
os.makedirs(dataset_path_labels, exist_ok=True)

os.makedirs(dataset_only_to_train_path_images, exist_ok=True)
os.makedirs(dataset_only_to_train_path_labels, exist_ok=True)

ultimate_train_ratio = 0.75
ultimate_val_ratio = 0.18
ultimate_test_ratio = 0.07

if((ultimate_train_ratio + ultimate_val_ratio + ultimate_test_ratio - 1.0) > 0.0001):
    print("ERROR")
    exit()

all_names_images = sorted(os.listdir(dataset_path_images))
all_names_labels = sorted(os.listdir(dataset_path_labels))

all_names_images_only_to_train = sorted(os.listdir(dataset_only_to_train_path_images))
all_names_labels_only_to_train = sorted(os.listdir(dataset_only_to_train_path_labels))

size_of_normal_dataset = len(all_names_images)
size_of_only_to_train_dataset = len(all_names_images_only_to_train)

total_size = size_of_normal_dataset + size_of_only_to_train_dataset


ultimate_train_images_number = int(ultimate_train_ratio * total_size)
ultimate_val_images_number = int(ultimate_val_ratio * total_size)
ultimate_test_images_number = int(ultimate_test_ratio * total_size)

train_images_num_from_normal_dataset = ultimate_train_images_number - size_of_only_to_train_dataset
val_images_num_from_normal_dataset = ultimate_val_images_number
test_images_num_from_normal_dataset = ultimate_test_images_number

train_ratio_of_normal = train_images_num_from_normal_dataset / size_of_normal_dataset
val_ratio_of_normal = val_images_num_from_normal_dataset / size_of_normal_dataset
test_ratio_of_normal = test_images_num_from_normal_dataset / size_of_normal_dataset


for name, labels in zip(all_names_images, all_names_labels):
    if(name.split(".jpg")[0] != labels.split(".txt")[0]):
        print("ERROR")
        break

dataset_size = len(all_names_images)

random_index_list = list(range(dataset_size))

last_index = dataset_size - 1

random.shuffle(random_index_list)

train_index_list = random_index_list[0 : int(train_ratio_of_normal * dataset_size)]
val_index_list = random_index_list[int(train_ratio_of_normal * dataset_size) : int((train_ratio_of_normal + val_ratio_of_normal) * dataset_size)]
test_index_list = random_index_list[int((train_ratio_of_normal + val_ratio_of_normal) * dataset_size) : ]


for index in train_index_list:
    shutil.copy(os.path.join(dataset_path_images, all_names_images[index]), DATA_SET_DEST_PATH_TRAIN_IMAGES)
    shutil.copy(os.path.join(dataset_path_labels, all_names_labels[index]), DATA_SET_DEST_PATH_TRAIN_LABELS)

for index in val_index_list:
    shutil.copy(os.path.join(dataset_path_images, all_names_images[index]), DATA_SET_DEST_PATH_VAL_IMAGES)
    shutil.copy(os.path.join(dataset_path_labels, all_names_labels[index]), DATA_SET_DEST_PATH_VAL_LABELS)

for index in test_index_list:
    shutil.copy(os.path.join(dataset_path_images, all_names_images[index]), DATA_SET_DEST_PATH_TEST_IMAGES)
    shutil.copy(os.path.join(dataset_path_labels, all_names_labels[index]), DATA_SET_DEST_PATH_TEST_LABELS)



for only_to_train_image_name, only_to_train_label_name in zip(all_names_images_only_to_train, all_names_labels_only_to_train):
    shutil.copy(os.path.join(dataset_only_to_train_path_images, only_to_train_image_name), DATA_SET_DEST_PATH_TRAIN_IMAGES)
    shutil.copy(os.path.join(dataset_only_to_train_path_labels, only_to_train_label_name), DATA_SET_DEST_PATH_TRAIN_LABELS)



