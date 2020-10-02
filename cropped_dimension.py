from imageio import imread
from PIL import Image
import numpy as np
import os

# imgs_dir = '/home/fehty/BlenderCompilation/BlenderRes/CamClosestFrame/Obj0/'
imgs_dir = '/home/fehty/BlenderCompilation/BlenderRes/EachFrameRender/Obj8/'


def through_dir():
    all_objs = dict()
    for filename in os.listdir(imgs_dir):
        all_objs[filename] = get_pos_to_crop(imgs_dir + filename)
    l_dim = get_largest_dimension(all_objs)

    get_cropped_imgs(all_objs, l_dim)


def get_largest_dimension(all_objs):
    # Optimize inside dimensions(find instantly boundaries)
    largest_dimension = dict()
    length_arr = [abs(all_objs[dict_item]['left_x'] - all_objs[dict_item]['right_x'])
                  for dict_item in all_objs]
    largest_dimension['length'] = max(length_arr)
    height_arr = [abs(all_objs[dict_item]['top_y'] - all_objs[dict_item]['bottom_y'])
                  for dict_item in all_objs]
    largest_dimension['height'] = max(height_arr)
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


def get_cropped_imgs(all_objs, l_dim):
    for filename in os.listdir(imgs_dir):
        img = Image.open(imgs_dir + filename)

        length = abs(all_objs[filename]['left_x'] - all_objs[filename]['right_x'])
        empty_length = abs(l_dim['length'] - length)
        left_x = all_objs[filename]['left_x'] + 0.0 - empty_length / 2
        right_x = all_objs[filename]['right_x'] + 0.0 + empty_length / 2

        height = abs(all_objs[filename]['top_y'] - all_objs[filename]['bottom_y'])
        empty_height = abs(l_dim['height'] - height)
        top_y = all_objs[filename]['top_y'] + 0.0 - empty_height / 2
        bottom_y = all_objs[filename]['bottom_y'] + 0.0 + empty_height / 2

        # left_x = all_objs[filename]['left_x']
        # right_x = all_objs[filename]['right_x']
        # top_y = all_objs[filename]['top_y']
        # bottom_y = all_objs[filename]['bottom_y']
        img2 = img.crop((left_x, top_y, right_x, bottom_y))
        img2.save('/home/fehty/PycharmProjects/SpriteLauncher/Images/' + filename + ".png")
