import os
from PIL import Image 
import math

directory = os.fsencode('in')
dirs = ['']

file_types = ['.jpg', '.jpeg', '.png']

files = []

while len(dirs) > 0:
    dirPath = dirs.pop(0)
    inDir = f"in{dirPath}" if dirPath != '' else 'in'
    outDir = f"out{dirPath}" if dirPath != '' else 'out'
    for file in os.listdir(inDir):
        filename = os.fsdecode(file)
        if filename.startswith('.'):
            continue
        if os.path.isdir(f"{inDir}/{filename}"):
            try:
                os.mkdir(f"{outDir}/{filename}")
            except:
                print(f"Directory {outDir}/{filename} already exists")
            dirs.append(f"{dirPath}/{filename}")
            continue
        for file_type in file_types:
            if filename.endswith(file_type):
                files.append(f"{dirPath}/{filename}")
                break

goal = 19_999_999

def resize_image(path):
    img_in = Image.open(f"in/{path}")

    width, height = img_in.size 
    pixels = width * height
    new_width = math.floor(width * math.sqrt(goal / pixels)) if pixels > goal else width
    new_height = math.floor(height * math.sqrt(goal / pixels)) if pixels > goal else height
    img_out = img_in.resize((new_width, new_height))
    img_out.save(f"out/{path}")
    print(f"{path}: {pixels/1_000_000}MP ({width}x{height}) -> {new_width*new_height/1_000_000}MP ({new_width}x{new_height})")


for file in files:
    if file == 'in/.gitkeep':
        continue
    resize_image(file)
