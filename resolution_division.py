from pathlib import Path
from enum import Enum
from PIL import Image, ImageOps
import json
import os
import math

# resolutions = {
#     'highResolution': 1.0,
#     'mediumResolution': 0.7,
#     'lowResolution': 0.4
# }

class Resolutions(Enum):
    HIGH = 1
    MEDIUM = 0.7
    LOW = 0.4

def division_launcher():
    from main import stylized_cropped_objs
    for obj in os.listdir(stylized_cropped_objs):
        obj_path = stylized_cropped_objs + obj + '/'
        # frames = []
        obj_frames = os.listdir(obj_path)
        obj_frames.sort()
        for obj_frame in obj_frames:
            try:
                with Image.open(obj_path + obj_frame) as im:
                    # frames.append(im.getdata())
                    export_three_sizes(obj, im)
            except:
                print(obj + '/' + obj_frame + ' is not a valid image')

def export_three_sizes(obj, img):
    # from main import saved_resolutions
    coef_high_res = Resolutions.HIGH.value
    coef_med_res = Resolutions.MEDIUM.value
    coef_low_res = Resolutions.LOW.value

    for image_resolution in Resolutions:
        save_resolution_image(obj, img, image_resolution)
        # if image_resolution == Resolutions.HIGH:
        #    save_resolution_image()
        # elif image_resolution == 'mediumResolution':
        #     top = spr_l_h
        #     bottom = top + math.ceil(spr_l_h * coef_med_res)
        #     right = math.ceil(spr_l_w * coef_med_res)
        #     box = (0, top, right, bottom)
        #     ratio = (math.ceil(spr_l_w * coef_med_res), math.ceil(spr_l_h * coef_med_res))
        #     resized_img = ImageOps.fit(spr_l, ratio)
        #     future_sprite.paste(resized_img, box)
        # elif image_resolution == 'lowResolution':
        #     top = math.ceil(spr_l_h + spr_l_h * coef_med_res)
        #     bottom = top + math.ceil(spr_l_h * coef_low_res)
        #     right = math.ceil(spr_l_w * coef_low_res)
        #     box = (0, top, right, bottom)
        #     # ratio = (int(spr_l_w * coef_low_res), int(spr_l_h * coef_low_res))
        #     ratio = (math.ceil(spr_l_w * coef_low_res), math.ceil(spr_l_h * coef_low_res))
        #     resized_img = ImageOps.fit(spr_l, ratio)
        #     future_sprite.paste(resized_img, box)

    # future_sprite.save(saved_sprites + obj + '.png', 'PNG')

def save_resolution_image(obj, img, resolution):
    from main import saved_resolutions
    Path(saved_resolutions).mkdir(parents=True, exist_ok=True)
    width = img.getdata().size[0]
    height = img.getdata().size[1]
    path_to_save = saved_resolutions + obj
    if (resolution == Resolutions.HIGH):
        img.save(path_to_save + "HighRes" + '.png')
    elif (resolution == Resolutions.MEDIUM):
        ratio = (math.ceil(width * resolution.value), math.ceil(height * resolution.value))
        resized_img = ImageOps.fit(img, ratio)
        resized_img.save(path_to_save + "MedRes" + '.png')
    elif (resolution == Resolutions.LOW):
        ratio = (math.ceil(width * resolution.value), math.ceil(height * resolution.value))
        resized_img = ImageOps.fit(img, ratio)
        resized_img.save(path_to_save + "LowRes" + '.png')