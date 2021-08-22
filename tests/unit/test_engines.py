from unittest import TestCase
from unittest.mock import patch, call
from PIL import UnidentifiedImageError
from need_an_image import engines


class BingImageTest(TestCase):

    @patch('need_an_image.engines.bing.BytesIO')
    @patch('need_an_image.engines.bing.Image')
    @patch('need_an_image.engines.bing.BingImage.download_image')
    @patch('need_an_image.engines.bing.BingImage.download_search_page')
    @patch('need_an_image.engines.bing.BingImage.get_image_source_url')
    def test_get_an_image(self, mock_get_image_source_url, download_search_page,
                          mock_download_image, mock_image_class, mock_io_class):
        bing = engines.BingImage()

        bing.get_an_image('Cat')

        download_search_page.assert_called_once_with('Cat')
        mock_get_image_source_url.assert_called_once_with(download_search_page.return_value)
        mock_download_image.assert_called_once_with(mock_get_image_source_url.return_value)
        mock_io_class.assert_called_once_with(mock_download_image.return_value)
        mock_image_class.open.assert_called_once_with(mock_io_class.return_value)

    @patch('need_an_image.engines.bing.requests')
    def test_download_image_return_bytes(self, mock_requests):
        bing = engines.BingImage()

        content = bing.download_image('https://example.com/example.jpg')

        mock_requests.get.assert_called_once()
        self.assertEqual(content, mock_requests.get.return_value.content)

    @patch('need_an_image.engines.bing.BytesIO')
    @patch('need_an_image.engines.bing.Image')
    @patch('need_an_image.engines.bing.BingImage.download_image')
    @patch('need_an_image.engines.bing.BingImage.download_search_page')
    @patch('need_an_image.engines.bing.BingImage.get_image_source_url')
    def test_retry_when_get_an_image_raiseUnidentifiedImageError(self, mock_get_image_source_url,
                                                                 mock_download_search_page,
                                                                 mock_download_image, mock_image_class,
                                                                 mock_io_class,
                                                                 ):
        bing = engines.BingImage()
        mock_image_class.open.side_effect = UnidentifiedImageError()

        image = bing.get_an_image('Cat', max_retry=3)

        self.assertIsNone(image)
        mock_download_search_page.assert_called_once_with('Cat')

        calls = [call(mock_download_search_page.return_value)] * 4
        mock_get_image_source_url.assert_has_calls(calls)

        calls = [call(mock_get_image_source_url.return_value)] * 4
        mock_download_image.assert_has_calls(calls)
