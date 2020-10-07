import cv2
import os
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from pathlib import Path
import sys

temp_img_path = '/home/fehty/PycharmProjects/SpriteLauncher/temp.png'


def create_stylized_imgs():
    script_descriptor = open("paint_style.py")
    a_script = script_descriptor.read()
    sys.argv = ["paint_style.py", "argName"]
    exec(a_script)
    script_descriptor.close()

    # from main import cropped_objs
    # Path(cropped_objs).mkdir(parents=True, exist_ok=True)
    # for obj in os.listdir(cropped_objs):
    #     obj_path = cropped_objs + obj
    #     for obj_img in os.listdir(obj_path):
    #         get_img_mask(obj_path + '/' + obj_img)
    #         smooth_img()
    #         mask_and_img(obj_path + '/' + obj_img)
    #         make_b_back_transparent(obj, obj_img)
    # Path(temp_img_path).unlink()


def get_img_mask(obj_path):
    img = Image.open(obj_path)
    thresh = 1
    fn = lambda x: 255 if x > thresh else 0
    r = img.convert('L').point(fn, mode='1')
    r.save(temp_img_path)


def smooth_img():
    img_for_smoothing = cv2.imread(temp_img_path)
    blur = cv2.blur(img_for_smoothing, (1, 1))
    plt.imsave(temp_img_path, blur)


def mask_and_img(img_path):
    # src1 = cv2.imread('/home/fehty/PycharmProjects/baseline/chairDiv1.png')
    # src2 = cv2.imread('foo.png')
    src1 = cv2.imread(img_path)
    src2 = cv2.imread(temp_img_path)
    src2 = cv2.resize(src2, src1.shape[1::-1])
    dst = cv2.bitwise_and(src1, src2)
    cv2.imwrite(temp_img_path, dst)


def make_b_back_transparent(obj_name, obj_img):
    img = Image.open(temp_img_path)
    img = img.convert("RGBA")
    data = img.getdata()
    newData = []
    for item in data:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((0, 0, 0, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    from main import stylized_cropped_objs
    path_to_obj = stylized_cropped_objs + obj_name + '/'
    Path(path_to_obj).mkdir(parents=True, exist_ok=True)
    img.save(path_to_obj + obj_img, "PNG")
