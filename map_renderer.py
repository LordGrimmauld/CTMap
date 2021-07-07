import re
from tkinter import filedialog
from PIL import Image, UnidentifiedImageError

files = list(filedialog.askopenfilenames(title="Map Sections", filetypes=[("Map Sections", ".png")]))
out_path = filedialog.asksaveasfilename(title="Save Map render at...", filetypes=[("Map Sections", ".png")])

minx = 1000000000
maxx = -1000000000
minz = 1000000000
maxz = -1000000000

for fn in files:
    x, z = (*map(int, re.findall("-?[0-9]+", fn)),)
    if x < minx:
        minx = x
    if x > maxx:
        maxx = x
    if z < minz:
        minz = z
    if z > maxz:
        maxz = z

canvas_x = (1 + maxx - minx) * 512
canvas_z = (1 + maxz - minz) * 512

img = Image.new("RGBA", (canvas_x, canvas_z), color=0xffffff)
for fn in files:
    x, z = (*map(int, re.findall("-?[0-9]+", fn)),)
    print(f"Adding {fn} to render")

    x -= minx
    z -= minz
    x *= 512
    z *= 512

    part = Image.open(fn)
    img.paste(part, (x, z))

print("saving file...")
img.save(out_path)
