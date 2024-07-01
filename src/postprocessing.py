
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from rembg import remove
from pathlib import Path


def postprocess(image: Path, dimensions: tuple[int, int] = (32, 32), remove_bg: bool = True):
    if isinstance(img, Path):
        img = Image.open(image)
    else:
        img = image
    if remove_bg:
        img = remove(img)
    img = img.resize(dimensions, resample=Image.Resampling.NEAREST)
    return img
    


if __name__ == "__main__":
    # img = postprocess(r".\assets\pickaxe.png")
    # plt.imshow(img)
    # plt.show()
    img = Image.open(r".\assets\pickaxe.png")
    print(type(img))