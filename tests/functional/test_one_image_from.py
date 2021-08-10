import os
from unittest import TestCase
from PIL import Image
import need_an_image


class OneImageFromBingTest(TestCase):

    def test_save_an_image_from_bing(self):
        file_nums = len(os.listdir('tests'))
        filename = need_an_image.from_bing(keyword='猫')

        self.assertEqual(len(os.listdir('tests')), file_nums + 1)
        Image.open(filename)  # should not raise

    def test_create_an_image_from_bing(self):
        image = need_an_image.from_bing(keyword='猫', save=False)

        image.show()
        self.assertIsInstance(image, Image.Image)
