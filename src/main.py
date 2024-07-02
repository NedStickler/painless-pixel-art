from PIL import Image

if __name__ == "__main__":
    img = Image.open("./assets/apple_ppa.png")
    img = img.resize((1024, 1024), resample=Image.Resampling.NEAREST)
    img.save("./assets/apple_ppa_large.png")