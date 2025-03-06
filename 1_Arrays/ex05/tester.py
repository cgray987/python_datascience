from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_blue
from pimp_image import ft_green
from pimp_image import ft_gray

"""
Tester is slightly different than subject due to inconsistency with pimp_image
prototypes. each function is required to return an array, rather than img,
so I have to build images in my tester.py. Also must show and label images,
though that's not shown in the given tester.
"""

print("The shape of the image is: ", end="")
arr = ft_load("landscape.jpg")

img0 = Image.fromarray(arr)
img1 = Image.fromarray(ft_invert(arr))
img2 = Image.fromarray(ft_red(arr))
img3 = Image.fromarray(ft_green(arr))
img4 = Image.fromarray(ft_blue(arr))
img5 = Image.fromarray(ft_gray(arr))

print(ft_invert.__doc__)

imgs = [img0, img1, img2, img3, img4, img5]
titles = ["Original", "Inverted", "Red", "Green", "Blue", "Gray"]
fig, axes = plt.subplots(3, 2, figsize=(15, 10))

for ax, img, title in zip(axes.flat, imgs, titles):
    ax.imshow(img)
    ax.set_title(title, y=-0.2)

plt.tight_layout()
plt.show()
