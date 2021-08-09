from unittest import TestCase
from unittest.mock import patch
from need_an_image import downloader


class BingImageTest(TestCase):

    @patch('need_an_image.downloader.Image')
    @patch('need_an_image.downloader.BingImage.download_image')
    @patch('need_an_image.downloader.BingImage.get_image_info')
    def test_get_an_image(self, mock_get_image_info, mock_download_image, mock_image_class):
        bing = downloader.BingImage()
        mock_get_image_info.return_value = ('RBG', (1920, 1080), 'https://example.com/exmple.jpg')

        bing.get_an_image('Cat')

        mock_get_image_info.assert_called_once_with('Cat')
        mock_download_image.assert_called_once_with('https://example.com/exmple.jpg')
        mock_image_class.frombytes.assert_called_once_with(
            mode='RBG', size=(1920, 1080), data=mock_download_image.return_value
        )

    @patch('need_an_image.downloader.BingImage.request')
    @patch('need_an_image.downloader.BingImage.parse_source')
    def test_get_image_info(self, mock_parse_source, mock_request):
        bing = downloader.BingImage()

        bing.get_image_info('Cat')

        mock_request.assert_called_once_with(keyword='Cat')
        mock_parse_source.assert_called_once_with(mock_request.return_value)
