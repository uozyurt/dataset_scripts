import glob
import shutil
import os

DATASET_ROOT_PATH = "/home/umut/Desktop/AKONS_DATASET_OTHER/AKONS_TRAINING_DATASET"


DEST_PATH = "/home/umut/Desktop/AKONS_DATASET_OTHER/ALL_LABELS_DRONE_AIRCRAFT_HELICOPTER"

os.makedirs(DEST_PATH, exist_ok=True)


datasets_dict = {
    "attemp6.v1i.yolov5pytorch" : {"0":"0"},
    "Drone Detection.v4i.yolov5pytorch": {"2":"0", "0":"1"},
    "drone_detection_final roboflow universe.v1i.yolov5pytorch": {"0":"0"},
    "Drony.v8i.yolov5pytorch": {"0":"0"},
    "Heli Drone Missile.v4i.yolov5pytorch": {"0":"0", "1":"2"},
    "KILINC3.v3i.yolov5pytorch": {"1":"0"},
    "x2.v1i.yolov8": {"0":"0"},
    "egitim.v3i.yolov5pytorch": {"0":"1", "1":"1"},
    "part4.v1-part4.yolov5pytorch": {"0":"0"},
    "Helicopters-of-DC.v2-copterfinder1.2.yolov5pytorch": {"0":"2", "1":"2", "2":"2", "3":"2", "4":"2", "5":"2", "6":"2", "7":"2", "8":"2", "9":"2", "10":"2", "11":"2", "12":"2", "13":"2", "14":"2", "15":"2", "16":"2", "17":"2", "18":"2", "19":"2", "20":"2"}
}



for label_path in (glob.glob(os.path.join(DATASET_ROOT_PATH, "**/**/labels/*.txt"), recursive=True)):
    dataset_name = label_path.split("/")[-4]
    current_dataset_dict = datasets_dict[dataset_name]
    wanted_indexes = list(current_dataset_dict.keys())

    dest_txt_path = os.path.join(DEST_PATH, label_path.split("/")[-1])

    with open(label_path, 'r') as in_file:
        lines = in_file.readlines()

    filtered_lines = []
    for line in lines:
        lines_split = line.split(" ")
        if lines_split[0] in wanted_indexes:
            filtered_lines.append(current_dataset_dict[lines_split[0]] + " " + " ".join(lines_split[1:]))

    with open(dest_txt_path, 'w') as out_file:
        out_file.writelines(filtered_lines)
        

