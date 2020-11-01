from PIL import Image
from pathlib import Path
import os


def common_foldering(path_from, path_to):
    for obj in os.listdir(path_from):
        obj_path = path_from + obj
        obj_frames = os.listdir(obj_path)
        obj_frames.sort()
        for obj_frame in obj_frames:
            try:
                with Image.open(obj_path + "/" + obj_frame) as im:
                    Path(path_to).mkdir(parents=True, exist_ok=True)
                    im.save(path_to + obj + ".png", "PNG")
            except:
                print(obj + '/' + obj_frame + ' is not a valid image')
