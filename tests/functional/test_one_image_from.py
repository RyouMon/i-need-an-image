import os
from unittest import TestCase
from PIL import Image
import need_an_image


class OneImageFromBingTest(TestCase):

    def test_save_an_image_from_bing(self):
        file_nums = len(os.listdir())
        filename = need_an_image.from_bing(keyword='猫')

        self.assertEqual(len(os.listdir()), file_nums + 1)
        with Image.open(filename):
            pass  # should not raise

        os.remove(filename)

    def test_create_an_image_from_bing(self):
        image = need_an_image.from_bing(keyword='猫', save=False)

        self.assertIsInstance(image, Image.Image)
