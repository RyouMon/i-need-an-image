from unittest import TestCase
from unittest.mock import patch
import need_an_image


class FromBingTest(TestCase):

    @patch('need_an_image.bing')
    @patch('need_an_image.save_image')
    def test_from_bing_return_filename_if_save_is_True(self, mock_save_image, mock_bing):
        filename = need_an_image.from_bing(keyword='Cat', save=True)
        image = mock_bing.get_an_image.return_value

        mock_bing.get_an_image.assert_called_once_with(keyword='Cat')
        mock_save_image.assert_called_once_with(image)
        self.assertEqual(filename, mock_save_image.return_value)

    @patch('need_an_image.bing')
    @patch('need_an_image.save_image')
    def test_from_bing_return_Image_if_save_is_False(self, mock_save_image, mock_bing):
        image = need_an_image.from_bing(keyword='Cat', save=False)

        mock_bing.get_an_image.assert_called_once_with(keyword='Cat')
        mock_save_image.assert_not_called()
        self.assertEqual(image, mock_bing.get_an_image.return_value)
