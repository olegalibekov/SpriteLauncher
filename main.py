from sprite_combinating import create_sprites_and_json
from sprite_cropping import save_cropped_objs
from sprite_stylizing import create_stylized_imgs

# init_objs = '/home/fehty/BlenderCompilation/BlenderRes/EachFrameRender/'
init_objs = '/home/fehty/BlenderCompilation/BlenderRes/ClosestRotateRender/'
cropped_objs = '/home/fehty/PycharmProjects/SpriteLauncher/CroppedObjects/'
stylized_cropped_objs = '/home/fehty/PycharmProjects/SpriteLauncher/StylizedObjects/'
saved_sprites = '/home/fehty/PycharmProjects/SpriteLauncher/Sprites/'

if __name__ == '__main__':
    # save_cropped_objs()
    create_stylized_imgs()
    # create_sprites_and_json()

# can be optimized without saving intermediate images for creating a sprite
