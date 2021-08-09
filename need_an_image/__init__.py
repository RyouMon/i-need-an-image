import requests
from PIL import Image


class BingImage:

    def get_an_image(self, keyword):
        response = self.search_request(keyword=keyword)
        source_url = self.parse_source(response)
        image_content = self.download_content(source_url)
        return Image.frombytes(image_content)


bing = BingImage()


def save_image(image):
    pass


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
