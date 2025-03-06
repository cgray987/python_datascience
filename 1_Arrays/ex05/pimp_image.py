import numpy as np


""" All of these are returning a np.array,
even though subject has non-existing expected
'array' type return """


def ft_invert(array: np.array) -> np.array:
    """
    Inverts color of the image received.
    """
    return 255 - array


def ft_red(array: np.array) -> np.array:
    """
    isolate red channel of image
    """
    red = array[:, :, 0]
    img = np.zeros_like(array)
    img[:, :, 0] = red
    return img


def ft_green(array: np.array) -> np.array:
    """
    isolate green channel of image
    """
    green = array[:, :, 1]
    img = np.zeros_like(array)
    img[:, :, 1] = green
    return img


def ft_blue(array: np.array) -> np.array:
    """
    isolate blue channel of image
    """
    blue = array[:, :, 2]
    img = np.zeros_like(array)
    img[:, :, 2] = blue
    return img


def ft_gray(array: np.array) -> np.array:
    """
    Grayscale (I refuse to use 'grey')
    formula: ITU-R 601-2 luma transform
    """
    img = array.copy()
    r = array[:, :, 0]
    g = array[:, :, 1]
    b = array[:, :, 2]
    img = r * (299 / 1000) + g * (587 / 1000) + b * (114 / 1000)
    return img
