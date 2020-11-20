from common_foldering import common_foldering
from sprite_combinating import create_sprites_and_json
from sprite_cropping import save_cropped_objs
from sprite_stylizing import create_stylized_imgs
from resolution_division import division_launcher

# Objects
# init_objs = '/home/fehty/BlenderCompilation/BlenderRes/EachFrameRender/'
init_objs = '/home/fehty/BlenderCompilation/BlenderRes/ClosestRotateRender/'
cropped_objs = '/home/fehty/PycharmProjects/SpriteLauncher/CroppedObjects/'
# stylized_cropped_objs = '/home/fehty/PycharmProjects/SpriteLauncher/StylizedCroppedObjects/'
stylized_cropped_objs = '/home/fehty/PycharmProjects/SpriteLauncher/StylizedObjects3 (copy)/'
saved_resolutions = '/home/fehty/PycharmProjects/SpriteLauncher/SavedResolutions/'
# saved_sprites = '/home/fehty/PycharmProjects/SpriteLauncher/Sprites/'

# Images
# init_imgs= '/home/fehty/BlenderCompilation/BlenderRes/ExportedImages/'

if __name__ == '__main__':
    # Objects
    # save_cropped_objs()
    # create_stylized_imgs()
    division_launcher()

    # create_sprites_and_json()


    # common_foldering("/home/fehty/PycharmProjects/SpriteLauncher/CroppedObjects3/", '/home/fehty/PycharmProjects/SpriteLauncher/CommonObjects/')