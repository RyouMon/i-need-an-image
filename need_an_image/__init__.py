from uuid import uuid4
from need_an_image.downloader import BingImage


bing = BingImage()


def save_image(image):
    suffix = '.jpg'
    if image.mode == 'RGBA':
        suffix = '.png'
    filename = uuid4().hex + suffix
    image.save(filename)
    return filename


def from_bing(keyword, save=True, exact=True, allow_pos=()):
    """
    Get an image from Bing image.
    if save = True , image with save in disk and return a filename,
    if save = False, return an PIL.Image object.
    """
    image = bing.get_an_image(keyword=keyword, exact=exact, allow_pos=allow_pos)

    if save:
        return save_image(image)

    return image
