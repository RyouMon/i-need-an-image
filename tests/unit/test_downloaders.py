from unittest import TestCase
from unittest.mock import patch
from need_an_image import downloader


class BingImageTest(TestCase):

    @patch('need_an_image.downloader.BytesIO')
    @patch('need_an_image.downloader.Image')
    @patch('need_an_image.downloader.BingImage.download_image')
    @patch('need_an_image.downloader.BingImage.get_image_source_url')
    def test_get_an_image(self, mock_get_image_source_url, mock_download_image, mock_image_class, mock_BytesIO):
        bing = downloader.BingImage()
        mock_get_image_source_url.return_value = 'https://example.com/exmple.jpg'

        bing.get_an_image('Cat')

        mock_get_image_source_url.assert_called_once_with('Cat')
        mock_download_image.assert_called_once_with('https://example.com/exmple.jpg')
        mock_BytesIO.assert_called_once_with(mock_download_image.return_value)
        mock_image_class.open.assert_called_once_with(mock_BytesIO.return_value)

    @patch('need_an_image.downloader.BingImage.search_request')
    @patch('need_an_image.downloader.BingImage.parse_source')
    def test_get_image_info(self, mock_parse_source, mock_search_request):
        bing = downloader.BingImage()

        bing.get_image_source_url('Cat')

        mock_search_request.assert_called_once_with(keyword='Cat')
        mock_parse_source.assert_called_once_with(mock_search_request.return_value)

    @patch('need_an_image.downloader.requests')
    @patch('need_an_image.downloader.BingImage.get_search_params')
    def test_search_request(self, mock_get_search_params, mock_requests):
        bing = downloader.BingImage()

        bing.search_request('Cat')

        mock_get_search_params.assert_called_once_with(keyword='Cat')
        mock_requests.get.assert_called_once_with(bing.url, params=mock_get_search_params.return_value)

    @patch('need_an_image.downloader.requests')
    def test_download_image_return_bytes(self, mock_requests):
        bing = downloader.BingImage()

        content = bing.download_image('https://example.com/example.jpg')

        mock_requests.get.assert_called_once_with('https://example.com/example.jpg')
        self.assertEqual(content, mock_requests.get.return_value.content)
