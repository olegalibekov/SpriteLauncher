from imageio import imread
from pathlib import Path
from PIL import Image
import numpy as np
import os

objs_dir = '/home/fehty/BlenderCompilation/BlenderRes/EachFrameRender/'
dir_to_save = '/home/fehty/PycharmProjects/SpriteLauncher/Images/'


def through_dir():
    for obj in os.listdir(objs_dir):
        all_objs = dict()
        obj_path = objs_dir + obj
        for obj_img in os.listdir(obj_path):
            all_objs[obj_img] = get_pos_to_crop(obj_path + '/' + obj_img)
        l_dim = get_largest_dimension(all_objs)
        get_cropped_imgs(obj, all_objs, l_dim)


def get_largest_dimension(all_objs):
    largest_dimension = dict()

    first_el = list(all_objs.keys())[0]
    largest_dimension['length'] = abs(all_objs[first_el]['left_x'] - all_objs[first_el]['right_x'])
    largest_dimension['height'] = abs(all_objs[first_el]['top_y'] - all_objs[first_el]['bottom_y'])

    for dict_item in all_objs:
        length = abs(all_objs[dict_item]['left_x'] - all_objs[dict_item]['right_x'])
        if length > largest_dimension['length']:
            largest_dimension['length'] = length

        height = abs(all_objs[dict_item]['top_y'] - all_objs[dict_item]['bottom_y'])
        if height > largest_dimension['height']:
            largest_dimension['height'] = height

    return largest_dimension


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


def get_cropped_imgs(obj, all_objs, l_dim):
    obj_path = objs_dir + obj
    for obj_img in os.listdir(obj_path):
        img = Image.open(obj_path + '/' + obj_img)
        length = abs(all_objs[obj_img]['left_x'] - all_objs[obj_img]['right_x'])
        empty_length = abs(l_dim['length'] - length)
        left_x = all_objs[obj_img]['left_x'] - (empty_length / 2)
        right_x = all_objs[obj_img]['right_x'] + (empty_length / 2)
        height = abs(all_objs[obj_img]['top_y'] - all_objs[obj_img]['bottom_y'])
        empty_height = abs(l_dim['height'] - height)
        top_y = all_objs[obj_img]['top_y'] + 0.0 - empty_height / 2
        bottom_y = all_objs[obj_img]['bottom_y'] + 0.0 + empty_height / 2

        img2 = img.crop((left_x, top_y, right_x, bottom_y))
        path_to_save = dir_to_save + obj + '/'
        Path(path_to_save).mkdir(parents=True, exist_ok=True)
        img2.save(path_to_save + obj_img)
