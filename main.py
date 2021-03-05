from bmp_converter import convert_to_bmp
from common_foldering import common_foldering
from sprite_combinating import create_sprites_and_json
# from sprite_cropping import save_cropped_objs
from sprite_cropping_for_animation import save_cropped_objs
from sprite_stylizing import create_stylized_imgs
from resolution_division import division_launcher
import asyncio

import sys
# Objects
# init_objs = '/home/fehty/BlenderCompilation/BlenderRes/EachFrameRender/'
# init_objs = '/home/fehty/BlenderCompilation/BlenderRes/ClosestRotateRender/'
from webp_creation import webp_creation

init_objs = '/home/fehty/BlenderCompilation/BlenderRes/RendersRotateAround/object24_bod_1_0_0_001_copy_async/'
cropped_objs = '/home/fehty/BlenderCompilation/BlenderRes/RendersRotateAround/object24_bod_1_0_0_001_copy_async/cropped/'
# cropped_objs = '/home/fehty/PycharmProjects/SpriteLauncher/CroppedObjects/'
# stylized_cropped_objs = '/home/fehty/PycharmProjects/SpriteLauncher/StylizedCroppedObjects/'
# stylized_cropped_objs = '/home/fehty/BlenderCompilation/BlenderRes/RendersRotateAround/objectBody001/test_final/cropped/'
# stylized_cropped_objs = '/home/fehty/PycharmProjects/SpriteLauncher/StylizedObjects3 (copy)/'
# saved_resolutions = '/home/fehty/PycharmProjects/SpriteLauncher/RendersAround/'
# saved_sprites = '/home/fehty/PycharmProjects/SpriteLauncher/Sprites/'
# saved_sprites = '/home/fehty/BlenderCompilation/BlenderRes/RendersRotateAround/objectBody001/test/test_run/sprite/'
# saved_sprites = '/home/fehty/BlenderCompilation/BlenderRes/RendersRotateAround/objectBody001/test_final/cropped/'
# saved_sprites = ''
# Images
# init_imgs= '/home/fehty/BlenderCompilation/BlenderRes/ExportedImages/'

if __name__ == '__main__':
    # Objects
    # async def run_cropping_async():
    #     await
    # asyncio.run(save_cropped_objs())
    import time
    s = time.perf_counter()
    save_cropped_objs()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


    # create_stylized_imgs()
    # division_launcher()
    # create_sprites_and_json()
    # webp_creation()
    # common_foldering("/home/fehty/PycharmProjects/SpriteLauncher/CroppedObjects3/", '/home/fehty/PycharmProjects/SpriteLauncher/CommonObjects/')
