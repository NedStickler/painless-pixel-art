
import matplotlib.pyplot as plt
from PIL import Image
from rembg import remove


if __name__ == "__main__":
    img = Image.open(r".\assets\pickaxe.png")
    resized_img = img.resize((32, 32), resample=Image.Resampling.NEAREST)
    resized_no_bg_img = remove(resized_img)
    plt.imshow(resized_no_bg_img)
    plt.show()