from imageio import imread
from pathlib import Path
from PIL import Image
import numpy as np
import os

# max_edge_coordinates = {'left_x': 1350, 'right_x': 2036, 'top_y': 0, 'bottom_y': 994}
max_edge_coordinates = None


# Find max edge coordinates through all animations and crop all files with the same coordinates
def save_cropped_objs():
    from main import init_objs
    global max_edge_coordinates
    animation_amount = len(os.listdir(init_objs))
    current_animation = 0
    for animation_name in os.listdir(init_objs):
        path_to_angle = init_objs + animation_name + '/'
        current_animation += 1
        angles_amount = len(os.listdir(path_to_angle))
        current_angle = 0
        for angle in os.listdir(path_to_angle):
            current_angle += 1
            all_objs = dict()
            img_path = path_to_angle + angle
            current_frame = 0
            obj_len = None
            for img_name in os.listdir(img_path):
                if obj_len is None:
                    obj_len = len(os.listdir(img_path))
                current_frame += 1
                all_objs[img_name] = get_pos_to_crop(img_path + '/' + img_name)
                if max_edge_coordinates is None:
                    max_edge_coordinates = all_objs[img_name]
                check_max_edge_coordinates(all_objs[img_name])
                print('Animation: ' + str(current_animation) + '/' + str(animation_amount) + ' Current angle: ' + str(
                    current_angle) + '/' + str(angles_amount) + ' Current frame: ' + str(current_frame) + '/' + str(
                    obj_len) + ' Max edge coordinates: ' + str(max_edge_coordinates))
    save_cropped_images()


def check_max_edge_coordinates(obj_edge_coordinates):
    if obj_edge_coordinates['left_x'] < max_edge_coordinates['left_x']:
        max_edge_coordinates['left_x'] = obj_edge_coordinates['left_x']
    if obj_edge_coordinates['right_x'] > max_edge_coordinates['right_x']:
        max_edge_coordinates['right_x'] = obj_edge_coordinates['right_x']
    if obj_edge_coordinates['top_y'] < max_edge_coordinates['top_y']:
        max_edge_coordinates['top_y'] = obj_edge_coordinates['top_y']
    if obj_edge_coordinates['bottom_y'] > max_edge_coordinates['bottom_y']:
        max_edge_coordinates['bottom_y'] = obj_edge_coordinates['bottom_y']

    if max_edge_coordinates['left_x'] % 2 != 0:
        max_edge_coordinates['left_x'] += 1
    if max_edge_coordinates['right_x'] % 2 != 0:
        max_edge_coordinates['right_x'] += 1
    if max_edge_coordinates['top_y'] % 2 != 0:
        max_edge_coordinates['top_y'] += 1
    if max_edge_coordinates['bottom_y'] % 2 != 0:
        max_edge_coordinates['bottom_y'] += 1


def get_pos_to_crop(im_path):
    left_x = None
    right_x = None
    top_y = None
    bottom_y = None

    im = imread(im_path)
    indices = np.dstack(np.indices(im.shape[:2]))
    data = np.concatenate((im, indices), axis=-1)

    # [r g b a y x]
    for element in data:
        for elementItem in element:
            statement = left_x is not None and elementItem[3] != 0
            if statement and elementItem[5] < left_x:
                left_x = elementItem[5]
            elif statement and elementItem[5] > right_x:
                right_x = elementItem[5]
            if statement and elementItem[4] < top_y:
                top_y = elementItem[4]
            elif statement and elementItem[4] > bottom_y:
                bottom_y = elementItem[4]
            if left_x is None and elementItem[3] != 0:
                left_x = elementItem[5]
                right_x = elementItem[5]
                top_y = elementItem[4]
                bottom_y = elementItem[4]

    dim = dict()

    dim['left_x'] = left_x
    dim['right_x'] = right_x
    dim['top_y'] = top_y
    dim['bottom_y'] = bottom_y

    return dim


def save_cropped_images():
    from main import init_objs
    for animation_name in os.listdir(init_objs):
        path_to_angle = init_objs + animation_name + '/'
        for angle in os.listdir(path_to_angle):
            img_path = path_to_angle + angle
            for img_name in os.listdir(img_path):
                img = Image.open(img_path + '/' + img_name)
                img2 = img.crop((max_edge_coordinates['left_x'], max_edge_coordinates['top_y'],
                                 max_edge_coordinates['right_x'], max_edge_coordinates['bottom_y']))
                from main import cropped_objs
                path_to_save = cropped_objs + animation_name + '/' + angle + '/'
                Path(path_to_save).mkdir(parents=True, exist_ok=True)
                img2.save(path_to_save + img_name)
