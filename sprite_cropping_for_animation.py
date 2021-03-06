import os
from pathlib import Path

import numpy as np
from PIL import Image
from imageio import imread
from multiprocessing import Process, Manager

max_edge_coordinates = None


def crop_recursively():
    from main import init_objs
    for init_folder_object in os.listdir(init_objs):
        current_folder_object = init_objs + init_folder_object + '/'
        if os.path.isdir(current_folder_object):
            global max_edge_coordinates
            max_edge_coordinates = None
            find_max_coord_recursively(current_folder_object)
            crop_images_recursively(current_folder_object)


def find_max_coord_recursively(subdirectory_path):
    images_name = []

    for subdirectory_item in os.listdir(subdirectory_path):
        if not os.path.isdir(subdirectory_path + '/' + subdirectory_item):
            images_name.append(subdirectory_item)
        else:
            find_max_coord_recursively(subdirectory_path + '/' + subdirectory_item)

    if len(images_name) != 0:
        find_max_coord_among_images(subdirectory_path, images_name)


def find_max_coord_among_images(subdirectory_path, images_name):
    global max_edge_coordinates

    images_for_one_execution = 8
    with Manager() as manager:
        images_in_folder = len(images_name)
        from math import ceil, floor
        iterations_for_one_folder = ceil(images_in_folder / images_for_one_execution)
        equal_images_proportions = images_for_one_execution / images_in_folder

        for iteration in range(0, iterations_for_one_folder):
            img_percentages_from = floor(iteration * equal_images_proportions * images_in_folder)
            img_percentages_to = floor((iteration + 1) * equal_images_proportions * images_in_folder)

            L = manager.list()

            parallel_functions = []
            for img_index in range(img_percentages_from, img_percentages_to):
                if img_index < images_in_folder:
                    parallel_functions.append([get_pos_to_crop, (subdirectory_path + '/' + images_name[img_index], L,)])

            combineParallel([*parallel_functions])

            for l_item in L:
                check_max_edge_coordinates(l_item)


def check_max_edge_coordinates(obj_edge_coordinates):
    global max_edge_coordinates
    if max_edge_coordinates is None:
        max_edge_coordinates = {
            'left_x': obj_edge_coordinates['left_x'],
            'right_x': obj_edge_coordinates['right_x'],
            'top_y': obj_edge_coordinates['top_y'],
            'bottom_y': obj_edge_coordinates['bottom_y']
        }

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


def get_pos_to_crop(im_path, manager_list):
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

    dim = {'left_x': left_x,
           'right_x': right_x,
           'top_y': top_y,
           'bottom_y': bottom_y}

    manager_list.append(dim)


def crop_images_recursively(subdirectory_path):
    for subdirectory_item in os.listdir(subdirectory_path):
        item_path = subdirectory_path + '/' + subdirectory_item
        if not os.path.isdir(item_path):
            from main import init_objs
            recursive_path_to_save = item_path.split(init_objs, 1)[1]
            crop_image(item_path, recursive_path_to_save)
        else:
            crop_images_recursively(subdirectory_path + '/' + subdirectory_item)


def crop_image(image_path_to_open, image_path_to_save):
    splitted_image_path = image_path_to_save.rsplit('/', 1)
    image_path = splitted_image_path[0] + '/'
    image_name = splitted_image_path[1]

    img = Image.open(image_path_to_open)
    img2 = img.crop((max_edge_coordinates['left_x'], max_edge_coordinates['top_y'],
                     max_edge_coordinates['right_x'], max_edge_coordinates['bottom_y']))
    from main import cropped_objs
    path_to_save = cropped_objs + image_path
    Path(path_to_save).mkdir(parents=True, exist_ok=True)
    img2.save(path_to_save + image_name)


def combineParallel(func_and_args):
    proc = []
    for index in range(0, len(func_and_args)):
        p = Process(target=func_and_args[index][0], args=func_and_args[index][1])
        p.start()
        proc.append(p)
    for p in proc:
        p.join()