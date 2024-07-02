
from PIL import Image
from rembg import remove
from pathlib import Path


def postprocess(
    image_path: str | Path,
    save_path: str | Path | None = None,
    dimensions: tuple[int, int] = (32, 32),
    remove_bg: bool = True,
    keep_original: bool = True
) -> None:
    """Apply background removal and downsampling to the provided image.

    Args:
        image_path: Path to the image to post-process.
        save_path: Path to the location to save the post-processed image.
        dimensions: Two-long tuple of integers with the desired dimensions of the downsampled image. Maximum of (1024, 1024).
        remove_bg: Boolean for application of the background removal process.
        keep_original: Boolean for keeping the original file. If set to `False`, `save_path` must be None.
    
    Raises:
        ValueError: If either height or width exceed 1024.
        ValueError: If `keep_original` set to `False` and `save_path` not set to `None`.
    """
    # Validate arguments
    if dimensions[0] > 1024 or dimensions[1] > 1024:
        raise ValueError("Height and width values must not exceed 1024.")
    if keep_original == False and save_path is not None:
        raise ValueError("save_path must be None when original file is overwritten with keep_original = False")

    # Apply post-processing
    img = Image.open(image_path)
    if remove_bg:
        img = remove(img)
    img = img.resize(dimensions, resample=Image.Resampling.NEAREST)

    # Save image
    if keep_original and save_path is None:
        save_path = image_path[:-4] + "_ppa.png"
        img.save(save_path)
    if keep_original and save_path is not None:
        img.save(save_path)
    else:
        img.save(image_path)
