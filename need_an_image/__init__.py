import os.path
import logging
import sys
from uuid import uuid4
from need_an_image.downloader import BingImage

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

bing = BingImage()


DOWNLOADER = {
    'bing': bing,
}


def save_image(image, save_to='.'):
    suffix = '.jpg'
    if image.mode == 'RGBA':
        suffix = '.png'

    filename = uuid4().hex + suffix

    if not os.path.isdir(save_to):
        os.makedirs(save_to)
    filename = os.path.join(save_to, filename)

    image.save(filename)
    return filename


def need_image_from(engine, keyword, exact=True, allow_pos=(), save_to=None, max_retry=3):
    image = DOWNLOADER[engine].get_an_image(keyword=keyword, exact=exact, allow_pos=allow_pos, max_retry=max_retry)

    if save_to:
        filename = save_image(image, save_to=save_to)
        return filename

    return image
