

def get_rid_of_postfix(string, postfix):
    string_parts = string.split(postfix)
    return string_parts[0] + string_parts[1]


def get_label_file_name(image_file_name):
    image_name_parts = image_file_name.split(".")
    return ".".join(image_name_parts[:-1]) + ".txt"