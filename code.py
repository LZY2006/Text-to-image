import math
import random

import matplotlib.pyplot as plt
import PIL
from PIL import Image
import os
import tqdm


def get_img_from_text(path: str):

    with open(path, "r", encoding="utf-8") as f:

        text = f.read()
        width = math.ceil(math.sqrt(len(text)))
        if width == 0:
            width = 1
        img = Image.new("RGB", (width, width))

        x = y = 0
        for c in text:
            index = ord(c)
            red = random.randint(100, 255)
            rgb = (red, (index & 0xFF00) >> 8, index & 0xFF)
            img.putpixel((x, y), rgb)
            if x == width - 1:
                x = 0
                y += 1
            else:
                x += 1
    return img


def get_text_from_img(img: PIL.Image.Image):

    width, height = img.size
    text = []
    for y in range(height):
        for x in range(width):
            red, green, blue = img.getpixel((x, y))
            if red == 0:
                break
            index = (green << 8) + blue
            text.append(chr(index))
    return "".join(text)

def make_bmp(path:str):
    img = get_img_from_text(path)
    # plt.imshow(img)
    img.save(path + ".bmp")
    # plt.show()


if __name__ == "__main__":
    # set the path
    top = r""
    text_files = []
    print("Collecting text files. . .")
    for dirpath, dirnames, filenames in tqdm.tqdm(list(os.walk((top)))):
        for name in filenames:
            filepath = os.path.join(dirpath, name)
            if filepath.endswith(".py"):
                text_files.append(filepath)
    print("Converting files. . .")
    for each in tqdm.tqdm(text_files):
        make_bmp(each)