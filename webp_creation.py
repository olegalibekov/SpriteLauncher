import os
import re

cropped_files = '/home/fehty/BlenderCompilation/BlenderRes/RendersRotateAround/objectBody001/croppedCopy/cropped/runCopy/'

files = os.listdir(cropped_files)


def webp_creation():
    sorted_files_temp = sorted(files, key=natural_keys)

    sorted_files = []
    for file in sorted_files_temp:
        if file.endswith(".png"):
            sorted_files.append('"' + file + '"')

    sorted_files_path = [cropped_files + file for file in sorted_files]
    formatted_files = ' '.join(sorted_files_path)
    os.system(f'img2webp -d 16 {formatted_files} -o {cropped_files + "out.webp"}')


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [atoi(c) for c in re.split(r'(\d+)', text)]
