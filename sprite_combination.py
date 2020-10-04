from pathlib import Path
from PIL import Image, ImageOps
import json
import os

resolutions = {
    'highResolution': 1.0,
    'mediumResolution': 0.7,
    'lowResolution': 0.4
}


def create_sprites_and_json():
    sprite_json = {'spriteObjs': {}}
    from main import cropped_objs
    for obj in os.listdir(cropped_objs):
        obj_path = cropped_objs + obj + '/'
        frames = []
        obj_frames = os.listdir(obj_path)
        obj_frames.sort()
        for obj_frame in obj_frames:
            try:
                with Image.open(obj_path + obj_frame) as im:
                    frames.append(im.getdata())
            except:
                print(obj + '/' + obj_frame + ' is not a valid image')

        sprite_data = launch_sprite(frames)
        save_dif_res(obj, sprite_data)

        from sprite_json import get_json_obj
        tile_s = {'width': frames[0].size[0], 'height': frames[0].size[1]}
        # print(get_json_obj(obj, tile_s, len(frames), resolutions))
        sprite_json['spriteObjs'].update(get_json_obj(obj, tile_s, len(frames), resolutions))
    # sprite_json = dict(sorted(sprite_json['spriteObjs'].items()))
    # sprite_json = {k: sprite_json[k] for k in sorted(sprite_json)}
    with open('result.json', 'w') as fp:
        json.dump(sprite_json, fp, indent=4)
    # print(sprite_json)


def launch_sprite(frames):
    tile_width = frames[0].size[0]
    tile_height = frames[0].size[1]

    sprite_line_w = tile_width * len(frames)
    sprite_line_h = tile_height

    sprite_line = Image.new('RGBA', (int(sprite_line_w), int(sprite_line_h)))

    for current_frame in frames:
        top = 0
        left = tile_width * (frames.index(current_frame))
        bottom = top + tile_height
        right = left + tile_width

        box = (left, top, right, bottom)
        box = [int(i) for i in box]
        cut_frame = current_frame.crop((0, 0, tile_width, tile_height))

        sprite_line.paste(cut_frame, box)

    sprite_data = dict()
    sprite_data['sprite_line'] = sprite_line
    sprite_data['sprite_line_w'] = sprite_line_w
    sprite_data['sprite_line_h'] = sprite_line_h
    return sprite_data


def save_dif_res(obj, orig_sprite_data):
    from main import saved_sprites
    Path(saved_sprites).mkdir(parents=True, exist_ok=True)

    spr_l = orig_sprite_data['sprite_line']
    spr_l_w = orig_sprite_data['sprite_line_w']
    spr_l_h = orig_sprite_data['sprite_line_h']

    coef_med_res = resolutions['mediumResolution']
    coef_low_res = resolutions['lowResolution']

    f_spr_w = int(spr_l_w)
    f_spr_h = int(spr_l_h + spr_l_h * coef_med_res + spr_l_h * coef_low_res)

    future_sprite = Image.new('RGBA', (f_spr_w, f_spr_h))

    for image_resolution in resolutions:
        if image_resolution == 'highResolution':
            bottom = int(spr_l_h)
            right = int(spr_l_w)
            box = (0, 0, right, bottom)
            future_sprite.paste(spr_l, box)
        elif image_resolution == 'mediumResolution':
            top = spr_l_h
            bottom = top + int(spr_l_h * coef_med_res)
            right = int(spr_l_w * coef_med_res)
            box = (0, top, right, bottom)
            ratio = (int(spr_l_w * coef_med_res), int(spr_l_h * coef_med_res))
            resized_img = ImageOps.fit(spr_l, ratio)
            future_sprite.paste(resized_img, box)
        elif image_resolution == 'lowResolution':
            top = int(spr_l_h + spr_l_h * coef_med_res)
            bottom = top + int(spr_l_h * coef_low_res)
            right = int(spr_l_w * coef_low_res)
            box = (0, top, right, bottom)
            ratio = (int(spr_l_w * coef_low_res), int(spr_l_h * coef_low_res))
            resized_img = ImageOps.fit(spr_l, ratio)
            future_sprite.paste(resized_img, box)

    future_sprite.save(saved_sprites + 'Sprite' + obj + '.png', 'PNG')
