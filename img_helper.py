"""
Image helper
Main module of the package
All image operations should go thorough this module
"""

from PIL import Image, ImageEnhance, ImageFilter
import logging

# constants
CONTRAST_FACTOR_MAX = 1.5
CONTRAST_FACTOR_MIN = 0.5

SHARPNESS_FACTOR_MAX = 3
SHARPNESS_FACTOR_MIN = -1

BRIGHTNESS_FACTOR_MAX = 1.5
BRIGHTNESS_FACTOR_MIN = 0.5

COLORBALANCE_FACTOR_MIN = 0.0
COLORBALANCE_FACTOR_MAX = 2.0

GAUSSIANBLUR_FACTOR_MIN = 0.0
GAUSSIANBLUR_FACTOR_MAX = 2.0

UNSHARPMASK_FACTOR_MIN = 0.0
UNSHARPMASK_FACTOR_MAX = 2.0


def brightness(img, factor):
    """Adjust image brightness form 0.5-2 (1 - original)"""

    if factor > BRIGHTNESS_FACTOR_MAX or factor < BRIGHTNESS_FACTOR_MIN:
        raise ValueError("factor should be [0-2]")

    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(factor)


def contrast(img, factor):
    """Adjust image contrast form 0.5-1.5 (1 - original)"""

    if factor > CONTRAST_FACTOR_MAX or factor < CONTRAST_FACTOR_MIN:
        raise ValueError("factor should be [0.5-1.5]")

    enhancer = ImageEnhance.Contrast(img)
    return enhancer.enhance(factor)


def sharpness(img, factor):
    """Adjust image sharpness form 0-2 (1 - original)"""

    if factor > SHARPNESS_FACTOR_MAX or factor < SHARPNESS_FACTOR_MIN:
        raise ValueError("factor should be [0.5-1.5]")

    enhancer = ImageEnhance.Sharpness(img)
    return enhancer.enhance(factor)


def color_balance(img, factor):
    """Adjust image color balance form 0-2 (1 - original)"""

    if factor > COLORBALANCE_FACTOR_MAX or factor < COLORBALANCE_FACTOR_MIN:
        raise ValueError("factor should be [0.0-2.0]")

    enhancer = ImageEnhance.Color(img)
    return enhancer.enhance(factor)


def unsharmask(img, factor):
    """adjust image unsharmask form 0-2 (1 - original)"""

    if factor > UNSHARPMASK_FACTOR_MAX or factor < UNSHARPMASK_FACTOR_MIN:
        raise ValueError(f"factor should be [{UNSHARPMASK_FACTOR_MAX}-{UNSHARPMASK_FACTOR_MIN}]")

    filter = ImageFilter.UnsharpMask(img)
    return filter.radius(factor)


def gaussianblur(img, factor):
    """adjust image gaussianblur form 0-2 (1 - original)"""

    if factor > GAUSSIANBLUR_FACTOR_MAX or factor < GAUSSIANBLUR_FACTOR_MIN:
        raise ValueError(f"factor should be [{GAUSSIANBLUR_FACTOR_MAX}-{GAUSSIANBLUR_FACTOR_MIN}]")

    filter = ImageFilter.GaussianBlur(img)
    return filter.radius(factor)


def save(img, path):
    """Save image to hard drive"""

    img.save(path)


def open_img(img):
    """
    Open image in temporary file
    !use it only for debug!
    """

    img.open()
