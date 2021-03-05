import asyncio
import os
from pathlib import Path

import numpy as np
from PIL import Image
from imageio import imread
from multiprocessing import Process, Manager, Array

max_edge_coordinates = None
temp_edge_coordinates = []


def first(arg):
    # print(arg)
    for i in range(0, 5):
        print('First')
        for b in range(105, 112):
            print('First')

            # print(b)


# async def first():
#     for i in range(0, 5):
#         print('First')
#         for b in range(105, 112):
#             print('First')
#             await asyncio.sleep(0.5)
#             # print(b)


async def second():
    for i in range(10, 15):
        # print(i)
        print('Second')
        for b in range(115, 117):
            print('Second')
            await asyncio.sleep(0.5)
            # print(b)


# async def first_and_second():
#     await asyncio.gather(first(), second())


def save_cropped_objs():
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(run_cropping_objs())
    run_cropping_objs()


def angles(animation_name):
    from main import init_objs
    for angle_name in os.listdir(init_objs + animation_name + '/'):
        angle_images(animation_name, angle_name)
    # from main import init_objs
    # angles_name = [angle_images(animation_name, angle_name) for angle_name in
    #                os.listdir(init_objs + animation_name + '/')]
    # await asyncio.gather(*angles_name)


def run_cropping_objs():
    # await asyncio.gather(angle_images('JumpToRunAnimation', 'Lat0Lon0'))
    # angle_images('JumpToRunAnimation', 'Lat0Lon0')
    from main import init_objs
    # global max_edge_coordinates
    for animation_name in os.listdir(init_objs):
        angles(animation_name)

    save_cropped_images()

    # from main import init_objs
    # # global max_edge_coordinates
    # animations_name = [angles(animation_name) for animation_name in os.listdir(init_objs)]
    # await asyncio.gather(*animations_name)
    # save_cropped_images()


def combineParallel(func_and_args):
    proc = []
    for index in range(0, len(func_and_args)):
        p = Process(target=func_and_args[index][0], args=func_and_args[index][1])
        p.start()
        proc.append(p)
    for p in proc:
        p.join()


def angle_images(animation_name, angle_name):
    global max_edge_coordinates
    from main import init_objs

    angle_path = init_objs + animation_name + '/' + angle_name
    images_dir = os.listdir(angle_path)

    images_for_one_execution = 30
    with Manager() as manager:
        images_in_folder = len(os.listdir(angle_path))
        from math import ceil, floor
        iterations_for_one_folder = ceil(images_in_folder / images_for_one_execution)
        equal_images_proportions = images_for_one_execution / images_in_folder

        for iteration in range(0, iterations_for_one_folder):
            img_percentages_from = floor(iteration * equal_images_proportions * images_in_folder)
            img_percentages_to = floor((iteration + 1) * equal_images_proportions * images_in_folder)

            L = manager.list()

            for img_index in range(img_percentages_from, img_percentages_to):
                if img_index < images_in_folder:
                    parallel_functions = [[get_pos_to_crop, (angle_path + '/' + images_dir[img_index], L,)]]

            combineParallel([*parallel_functions])
            for l_item in L:
                check_max_edge_coordinates(l_item)

    # for img_name in os.listdir(angle_path):
    #     edge_coordinates = get_pos_to_crop(angle_path + '/' + img_name)
    #     print(animation_name + ' ' + angle_name + ' ' + img_name)
    #     if max_edge_coordinates is None:
    #         max_edge_coordinates = edge_coordinates
    #     check_max_edge_coordinates(edge_coordinates)

    # print(max_edge_coordinates)


def check_max_edge_coordinates(obj_edge_coordinates):
    global max_edge_coordinates
    if max_edge_coordinates is None:
        max_edge_coordinates = dict()
        max_edge_coordinates['left_x'] = obj_edge_coordinates['left_x']
        max_edge_coordinates['right_x'] = obj_edge_coordinates['right_x']
        max_edge_coordinates['top_y'] = obj_edge_coordinates['top_y']
        max_edge_coordinates['bottom_y'] = obj_edge_coordinates['bottom_y']

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


def compare_max_edge_coordinates(max_edge_coordinates, obj_edge_coordinates):
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

    dim = dict()

    dim['left_x'] = left_x
    dim['right_x'] = right_x
    dim['top_y'] = top_y
    dim['bottom_y'] = bottom_y

    manager_list.append(dim)
    # return dim


# async def get_pos_to_crop(im_path):
#     im = imread(im_path)
#     indices = np.dstack(np.indices(im.shape[:2]))
#     data = np.concatenate((im, indices), axis=-1)
#
#     print(im_path)
#     img_edges = []
#
#     # # [r g b a y x]
#     async def image_edges():
#
#         def maxEdgesInRange(startPercentages, endPercentages):
#             left_x = None
#             right_x = None
#             top_y = None
#             bottom_y = None
#             for element in range(int(len(data) * startPercentages), int(len(data) * endPercentages)):
#                 for dataIndex in range(0, len(data[element])):
#                     elementItem = data[element][dataIndex]
#                     statement = left_x is not None and elementItem[3] != 0
#                     if statement and elementItem[5] < left_x:
#                         left_x = elementItem[5]
#                     elif statement and elementItem[5] > right_x:
#                         right_x = elementItem[5]
#                     if statement and elementItem[4] < top_y:
#                         top_y = elementItem[4]
#                     elif statement and elementItem[4] > bottom_y:
#                         bottom_y = elementItem[4]
#                     if left_x is None and elementItem[3] != 0:
#                         left_x = elementItem[5]
#                         right_x = elementItem[5]
#                         top_y = elementItem[4]
#                         bottom_y = elementItem[4]
#
#             # if left_x is not None and right_x is not None and top_y is not None and bottom_y is not None:
#             #     array_l.append({'left_x': left_x,
#             #               'right_x': right_x,
#             #               'top_y': top_y,
#             #               'bottom_y': bottom_y})
#
#         # async def parallelCycles(threads):
#         #     img_max_edges = []
#         #     division_percentages = 1 / threads
#         #
#         #     for thread in range(0, threads):
#         #         thread_max_edges = await maxEdgesInRange(division_percentages * thread,
#         #                                                  division_percentages * (thread + 1))
#         #         if thread_max_edges['left_x'] is not None and thread_max_edges['right_x'] is not None and \
#         #                 thread_max_edges['top_y'] is not None and thread_max_edges['bottom_y'] is not None:
#         #             img_max_edges.append(thread_max_edges)
#         #
#         #     final_img_max_edges = {
#         #         'left_x': img_max_edges[0]['left_x'],
#         #         'right_x': img_max_edges[0]['right_x'],
#         #         'top_y': img_max_edges[0]['top_y'],
#         #         'bottom_y': img_max_edges[0]['bottom_y']
#         #     }
#         #     for edgesIndex in range(0, len(img_max_edges)):
#         #         compare_max_edge_coordinates(final_img_max_edges, img_max_edges[edgesIndex])
#         #     return final_img_max_edges
#
#         def combineParallel(func_and_args):
#             proc = []
#             for index in range(0, len(func_and_args)):
#                 p = Process(target=func_and_args[index][0], args=func_and_args[index][1])
#                 p.start()
#                 proc.append(p)
#             for p in proc:
#                 p.join()
#
#         def parallelCycles(threads):
#             # img_max_edges = []
#             division_percentages = 1 / threads
#
#             parallel_functions = []
#             with Manager() as manager:
#                 L = manager.list()
#                 for thread in range(0, threads):
#                     parallel_functions.append(
#                         [maxEdgesInRange, (division_percentages * thread, division_percentages * (thread + 1))])
#                     # print(parallel_functions)
#                     L.append(thread)
#                     # print(L)
#             combineParallel([*parallel_functions])
#
#             # final_img_max_edges = {
#             #     'left_x': img_max_edges[0]['left_x'],
#             #     'right_x': img_max_edges[0]['right_x'],
#             #     'top_y': img_max_edges[0]['top_y'],
#             #     'bottom_y': img_max_edges[0]['bottom_y']
#             # }
#             # for edgesIndex in range(0, len(img_max_edges)):
#             #     compare_max_edge_coordinates(final_img_max_edges, img_max_edges[edgesIndex])
#             # return final_img_max_edges
#
#         return parallelCycles(4)
#
#     dim = await image_edges()
#
#     return dim


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

# from multiprocessing import Process
# p1 = Process(target=maxEdgesInRange, args=(division_percentages * 0, division_percentages * (0 + 1)))
# p1.start()
# p2 = Process(target=maxEdgesInRange, args=(division_percentages * 1, division_percentages * (1 + 1)))
# p2.start()
# p1.join()
# p2.join()
#
# runInParallel([[maxEdgesInRange, (division_percentages * 0, division_percentages * (0 + 1))],
#                [maxEdgesInRange, (division_percentages * 1, division_percentages * (1 + 1))]])
