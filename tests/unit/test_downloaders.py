from unittest import TestCase
from unittest.mock import patch
from PIL import UnidentifiedImageError
from need_an_image import downloader


class BingImageTest(TestCase):

    @patch('need_an_image.downloader.BytesIO')
    @patch('need_an_image.downloader.Image')
    @patch('need_an_image.downloader.BingImage.download_image')
    @patch('need_an_image.downloader.BingImage.download_search_page')
    @patch('need_an_image.downloader.BingImage.get_image_source_url')
    def test_get_an_image(self, mock_get_image_source_url, download_search_page,
                          mock_download_image, mock_image_class, mock_io_class):
        bing = downloader.BingImage()

        bing.get_an_image('Cat')

        download_search_page.assert_called_once_with('Cat')
        mock_get_image_source_url.assert_called_once_with(download_search_page.return_value)
        mock_download_image.assert_called_once_with(mock_get_image_source_url.return_value)
        mock_io_class.assert_called_once_with(mock_download_image.return_value)
        mock_image_class.open.assert_called_once_with(mock_io_class.return_value)

    @patch('need_an_image.downloader.requests')
    def test_download_image_return_bytes(self, mock_requests):
        bing = downloader.BingImage()

        content = bing.download_image('https://example.com/example.jpg')

        mock_requests.get.assert_called_once()
        self.assertEqual(content, mock_requests.get.return_value.content)
