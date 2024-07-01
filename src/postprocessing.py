
from PIL import Image
from rembg import remove
from pathlib import Path


def postprocess(image_path: str | Path, save_path: str | Path | None = None, dimensions: tuple[int, int] = (32, 32), remove_bg: bool = True):
    img = Image.open(image_path)
    if remove_bg:
        img = remove(img)
    img = img.resize(dimensions, resample=Image.Resampling.NEAREST)
    if save_path is None:
        save_path = image_path[:-4] + "_ppa.png"
    img.save(save_path)
    
if __name__ == "__main__":
    postprocess(r".\assets\pickaxe.png", dimensions=(64, 64))