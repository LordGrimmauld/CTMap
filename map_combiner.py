from tkinter import filedialog
import os
from shutil import copyfile, SameFileError
from PIL import Image, UnidentifiedImageError

files1 = list(filedialog.askopenfilenames(title="Map Sections", filetypes=[("Map Sections", ".png")]))
files2 = list(filedialog.askopenfilenames(title="Map Sections", filetypes=[("Map Sections", ".png")]))

out_path = filedialog.askdirectory(title="Save Map Sections at...")


def merge(file1, file2, out):
    print(f"merging {file1} + {file2} to {out}")
    try:
        background = Image.open(file1)
        foreground = Image.open(file2)
        Image.alpha_composite(background, foreground).save(out)
    except UnidentifiedImageError:
        pass


for file1 in set(files1) - set(files2):
    filename1 = os.path.split(file1)[-1]
    for file2 in files2[:]:
        filename2 = os.path.split(file2)[-1]
        if filename1 == filename2:
            merge(file1, file2, os.path.join(out_path, filename1))
            files2.remove(file2)
            break
    else:
        try:
            copyfile(file1, os.path.join(out_path, os.path.split(file1)[-1]))
        except SameFileError:
            pass

for file1 in files2:
    try:
        copyfile(file1, os.path.join(out_path, os.path.split(file1)[-1]))
    except SameFileError:
        pass
