import os
from unittest import TestCase
from PIL import Image
import need_an_image


class NeedImageFromTest(TestCase):

    def test_need_image_from_bing(self):
        image = need_an_image.need_image_from('bing', keyword='Cat')

        self.assertIsInstance(image, Image.Image)
