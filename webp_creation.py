import os
import re
from pathlib import Path


# convert -delay 2 -loop 0 -dispose Background *.png JumpToRun.gif
def webp_creation():
    files_from = '/home/fehty/BlenderCompilation/BlenderRes/RendersRotateAround/object24_bod_1_0_0_001/RunAnimation/'
    output_animated = '/home/fehty/BlenderCompilation/BlenderRes/RendersRotateAround/object24_bod_1_0_0_001/Animated/RunAnimation/'
    Path(output_animated).mkdir(parents=True, exist_ok=True)
    current_folder = 0
    for folder in os.listdir(files_from):
        current_folder += 1
        print('Folder ' + str(current_folder) + '/' + str(len(os.listdir(files_from))))
        folder_files = files_from + folder
        sorted_files_temp = sorted(os.listdir(folder_files), key=natural_keys)
        sorted_files = []

        for file in sorted_files_temp:
            if file.endswith(".png"):
                sorted_files.append('"' + file + '"')

        sorted_files_path = [folder_files + '/' + file for file in sorted_files]
        formatted_files = ' '.join(sorted_files_path)
        # os.system(f'img2webp -d 16 -lossy -q 15 {formatted_files} -o {cropped_files + "RunLossy55.webp"}')
        # os.system(f'img2webp -d 300 -lossy {formatted_files} -o {cropped_files + "RunLossy55.webp"}')
        os.system(
            f'convert -delay 2 -loop 0 -resize 55% -dispose Background {formatted_files} {output_animated + folder + ".gif"}')


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]
