import os
from PIL import Image 
import math

directory = os.fsencode('in')

file_type = 'jpg'

files = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(file_type):
        files.append(filename)

goal = 19_999_999

for file in files:
    print(file)
    if file == '.gitkeep':
        continue
    img_in = Image.open(f"in/{file}") 

    width, height = img_in.size 
    pixels = width * height
    new_width = math.floor(width * math.sqrt(goal / pixels)) if pixels > goal else width
    new_height = math.floor(height * math.sqrt(goal / pixels)) if pixels > goal else height
    img_out = img_in.resize((new_width, new_height))
    img_out.save(f"out/{file}")
    print(f"{file}: {pixels/1_000_000}MP ({width}x{height}) -> {new_width*new_height/1_000_000}MP ({new_width}x{new_height})")
