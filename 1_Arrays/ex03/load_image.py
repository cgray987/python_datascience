from PIL import Image
import numpy as np
import os


def ft_load(path: str) -> np.array:
    """
    loads image at path (in same dir as script), prints
    shape (height, width, channels) and
    pixel content as RGB
    """

    try:
        dir = os.path.dirname(__file__)
        abs_path = os.path.join(dir, path)
        if not os.path.exists(abs_path):
            raise AssertionError("File not found!")
        with Image.open(abs_path) as img:
            img_shape = f"({img.height}, {img.width}, {len(img.getbands())})"
            print(img_shape)
            return np.array(img)
    except Exception as e:
        print(f"Exception: {e}")
