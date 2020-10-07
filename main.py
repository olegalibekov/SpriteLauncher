from sprite_combinating import create_sprites_and_json
from sprite_stylizing import create_stylized_imgs

init_objs = '/home/fehty/BlenderCompilation/BlenderRes/EachFrameRender/'
cropped_objs = '/home/fehty/PycharmProjects/SpriteLauncher/CroppedObjects/'
stylized_cropped_objs = '/home/fehty/PycharmProjects/SpriteLauncher/StylizedObjects/'
saved_sprites = '/home/fehty/PycharmProjects/SpriteLauncher/Sprites/'

if __name__ == '__main__':
    # save_cropped_objs()
    # create_sprites_and_json()
    create_stylized_imgs()
# can be optimized without saving intermediate images for creating a sprite
