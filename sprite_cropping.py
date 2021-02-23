# from imageio import imread
# from pathlib import Path
# from PIL import Image
# import numpy as np
# import os
#
#
# def save_cropped_objs():
#     from main import init_objs
#     for obj in os.listdir(init_objs):
#         all_objs = dict()
#         obj_path = init_objs + obj
#         for obj_img in os.listdir(obj_path):
#             all_objs[obj_img] = get_pos_to_crop(obj_path + '/' + obj_img)
#         edge_coordinates = get_edge_coordinates(all_objs)
#         get_cropped_imgs(obj, all_objs, edge_coordinates)
#
#
# def get_edge_coordinates(all_objs):
#     # largest_dimension = dict()
#
#     edge_coordinates = dict()
#
#     first_el = list(all_objs.keys())[0]
#
#     edge_coordinates['right_x'] = all_objs[first_el]['right_x']
#     edge_coordinates['left_x'] = all_objs[first_el]['left_x']
#     edge_coordinates['top_y'] = all_objs[first_el]['top_y']
#     edge_coordinates['bottom_y'] = all_objs[first_el]['bottom_y']
#     # largest_dimension['length'] = abs(all_objs[first_el]['left_x'] - all_objs[first_el]['right_x'])
#     # largest_dimension['height'] = abs(all_objs[first_el]['top_y'] - all_objs[first_el]['bottom_y'])
#
#     for dict_item in all_objs:
#         # length = abs(all_objs[dict_item]['left_x'] - all_objs[dict_item]['right_x'])
#         if all_objs[dict_item]['left_x'] < edge_coordinates['left_x']:
#             edge_coordinates['left_x'] = all_objs[dict_item]['left_x']
#         if all_objs[dict_item]['right_x'] > edge_coordinates['right_x']:
#             edge_coordinates['right_x'] = all_objs[dict_item]['right_x']
#         if all_objs[dict_item]['top_y'] < edge_coordinates['top_y']:
#             edge_coordinates['top_y'] = all_objs[dict_item]['top_y']
#         if all_objs[dict_item]['bottom_y'] > edge_coordinates['bottom_y']:
#             edge_coordinates['bottom_y'] = all_objs[dict_item]['bottom_y']
#
#         # height = abs(all_objs[dict_item]['top_y'] - all_objs[dict_item]['bottom_y'])
#         # if height > largest_dimension['height']:
#         #     largest_dimension['height'] = height
#
#     if edge_coordinates['left_x'] % 2 != 0:
#         edge_coordinates['left_x'] += 1
#     if edge_coordinates['right_x'] % 2 != 0:
#         edge_coordinates['right_x'] += 1
#     if edge_coordinates['top_y'] % 2 != 0:
#         edge_coordinates['top_y'] += 1
#     if edge_coordinates['bottom_y'] % 2 != 0:
#         edge_coordinates['bottom_y'] += 1
#
#     return edge_coordinates
#
#
# def get_pos_to_crop(im_path):
#     left_x = None
#     right_x = None
#     top_y = None
#     bottom_y = None
#
#     im = imread(im_path)
#     indices = np.dstack(np.indices(im.shape[:2]))
#     data = np.concatenate((im, indices), axis=-1)
#
#     # [r g b a y x]
#     for element in data:
#         for elementItem in element:
#             statement = left_x is not None and elementItem[3] != 0
#             if statement and elementItem[5] < left_x:
#                 left_x = elementItem[5]
#             elif statement and elementItem[5] > right_x:
#                 right_x = elementItem[5]
#             if statement and elementItem[4] < top_y:
#                 top_y = elementItem[4]
#             elif statement and elementItem[4] > bottom_y:
#                 bottom_y = elementItem[4]
#             if left_x is None and elementItem[3] != 0:
#                 left_x = elementItem[5]
#                 right_x = elementItem[5]
#                 top_y = elementItem[4]
#                 bottom_y = elementItem[4]
#
#     dim = dict()
#
#     dim['left_x'] = left_x
#     dim['right_x'] = right_x
#     dim['top_y'] = top_y
#     dim['bottom_y'] = bottom_y
#
#     return dim
#
#
# def get_cropped_imgs(obj, all_objs, l_coordinates):
#     from main import init_objs
#     obj_path = init_objs + obj
#     for obj_img in os.listdir(obj_path):
#         img = Image.open(obj_path + '/' + obj_img)
#         # length = abs(all_objs[obj_img]['left_x'] - all_objs[obj_img]['right_x'])
#         # empty_length = abs(l_coordinates['length'] - length)
#         # left_x = all_objs[obj_img]['left_x'] - (empty_length / 2)
#         # right_x = all_objs[obj_img]['right_x'] + (empty_length / 2)
#         # height = abs(all_objs[obj_img]['top_y'] - all_objs[obj_img]['bottom_y'])
#         # empty_height = abs(l_coordinates['height'] - height)
#         # top_y = all_objs[obj_img]['top_y'] + 0.0 - empty_height / 2
#         # bottom_y = all_objs[obj_img]['bottom_y'] + 0.0 + empty_height / 2
#
#         img2 = img.crop(
#             (l_coordinates['left_x'], l_coordinates['top_y'], l_coordinates['right_x'], l_coordinates['bottom_y']))
#
#         from main import cropped_objs
#         path_to_save = cropped_objs + obj + '/'
#         Path(path_to_save).mkdir(parents=True, exist_ok=True)
#         img2.save(path_to_save + obj_img)
