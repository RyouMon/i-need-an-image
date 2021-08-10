from uuid import uuid4
from need_an_image.downloader import BingImage


bing = BingImage()


def save_image(image):
    filename = uuid4().hex + '.jpg'
    image.save(filename, 'JPEG')
    return filename


def from_bing(keyword, save=True):
    """
    Get an image from Bing image.
    if save = True , image with save in disk and return a filename,
    if save = False, return an PIL.Image object.
    """
    image = bing.get_an_image(keyword=keyword)

    if save:
        return save_image(image)

    return image
