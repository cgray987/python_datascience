from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt
import os
import sys


def zoom(img: Image) -> list[int]:
    """
    calculates crop box for zoom of image, if image is large
    enough, it creates a 400x400 box at 40%x10% position of image
    """
    img_width, img_height = img.size

    # Default crop dimensions
    width, height = (400, 400)
    left_ratio, upper_ratio = 0.4, 0.1  # Relative position (40%, 10%)

    # Adjust if image is too small
    if img_width < 800 or img_height < 500:
        width = min(400, int(img_width * 0.5))
        height = min(400, int(img_height * 0.8))
        left_ratio = 0.25
        upper_ratio = 0.1

    # Calculate crop coordinates
    left = int(img_width * left_ratio)
    upper = int(img_height * upper_ratio)
    right = left + width
    lower = upper + height

    # Ensure crop box doesn't exceed image bounds
    right = min(right, img_width)
    lower = min(lower, img_height)
    width = right - left
    height = lower - upper
    return [left, upper, right, lower]


def get_abs_path(path: str) -> os.path:
    """
    gets abs path from relative
    (assuming file is in same dir as this file)
    """
    dir = os.path.dirname(__file__)
    abs_path = os.path.join(dir, path)
    if not os.path.exists(abs_path):
        raise AssertionError("File not found!")
    return abs_path


def rotate(img: Image) -> Image:
    """
    rotates image by swaping x and y dimensions,
    manually for some god-forsaken reason
    """
    w, h = img.size
    trans = Image.new(img.mode, (h, w))
    for y in range(h):
        for x in range(w):
            trans.putpixel((y, x), img.getpixel((x, y)))
    return trans


def main():
    """
    loads image(s) from command line args,
    crops and grayscales them, then rotates.
    """
    try:
        img_paths = sys.argv[1:]
        if not img_paths:
            img_paths.append("animal.jpeg")
        print(img_paths)

        for path in img_paths:
            path = path.removeprefix("ex04/")
            print("The shape of the image is: ", end=" ")
            print(ft_load(path))
            with Image.open(get_abs_path(path)) as img:
                new_img = img.crop(zoom(img))
                new_img = new_img.convert("L")

                dir = os.path.dirname(__file__)
                if not os.path.exists(dir + "/new_imgs"):
                    os.mkdir(dir + "/new_imgs")
                abs_path = os.path.join(dir + "/new_imgs/",
                                        "gray_zoom_" + path)
                new_img = rotate(new_img)
                new_img.save(abs_path)

                print("The shape of the new image is: ", end=" ")
                print(ft_load(abs_path))
                plt.figure()
                plt.imshow(new_img, cmap="gray")
                plt.title("zoomed/grayed " + path)
                plt.axis("on")
        plt.show()
    except Exception as e:
        print(f"Exception:  {e}")


if __name__ == "__main__":
    main()
