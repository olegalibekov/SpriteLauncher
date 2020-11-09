from common_foldering import common_foldering
from sprite_combinating import create_sprites_and_json
from sprite_cropping import save_cropped_objs
from sprite_stylizing import create_stylized_imgs

# Objects
# init_objs = '/home/fehty/BlenderCompilation/BlenderRes/EachFrameRender/'
# init_objs = '/home/fehty/BlenderCompilation/BlenderRes/ClosestRotateRender/objectBookshelf_002/'
cropped_objs = '/home/fehty/PycharmProjects/SpriteLauncher/CroppedObjects/'
stylized_cropped_objs = '/home/fehty/PycharmProjects/SpriteLauncher/StylizedObjects/'
saved_sprites = '/home/fehty/PycharmProjects/SpriteLauncher/Sprites/'

# Images
init_objs = '/home/fehty/BlenderCompilation/BlenderRes/ExportedImages/'

if __name__ == '__main__':
    # Objects
    save_cropped_objs()
    create_stylized_imgs()
    create_sprites_and_json()

    # Images

    # common_foldering("/home/fehty/PycharmProjects/SpriteLauncher/CroppedObjects3/", '/home/fehty/PycharmProjects/SpriteLauncher/CommonObjects/')