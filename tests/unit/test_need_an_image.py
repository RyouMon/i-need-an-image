from unittest import TestCase
from unittest.mock import patch
import need_an_image


class NeedImageFromTest(TestCase):

    @patch('need_an_image.ENGINES')
    @patch('need_an_image.save_image')
    def test_call_engine(self, _, mock_ENGINES):
        filename = need_an_image.need_image_from(
            engine='bing', keyword='Cat', exact=True, allow_pos=(), max_retry=3
        )

        mock_ENGINES['bing'].get_an_image.assert_called_once_with(
            keyword='Cat', exact=True, allow_pos=(), max_retry=3
        )

    @patch('need_an_image.ENGINES')
    @patch('need_an_image.save_image')
    def test_need_image_from_return_None_if_engine_return_None(self, save_image, mock_ENGINES):
        mock_ENGINES['bing'].get_an_image.return_value = None

        image = need_an_image.need_image_from(engine='bing', keyword='Cat')
        self.assertIsNone(image)

        image = need_an_image.need_image_from(engine='bing', keyword='Cat', save_to='.')
        self.assertIsNone(image)
        save_image.assert_not_called()

    @patch('need_an_image.ENGINES')
    @patch('need_an_image.save_image')
    def test_need_image_return_Image_if_save_to_is_None(self, save_image, mock_ENGINES):
        image = need_an_image.need_image_from(engine='bing', keyword='Cat', save_to=None)

        self.assertEqual(image, mock_ENGINES['bing'].get_an_image.return_value)
        save_image.assert_not_called()

    @patch('need_an_image.ENGINES')
    @patch('need_an_image.save_image')
    def test_need_image_return_filename_if_save_to_is_path(self, save_image, mock_ENGINES):
        filename = need_an_image.need_image_from(engine='bing', keyword='Cat', save_to='.')

        save_image.assert_called_once_with(mock_ENGINES['bing'].get_an_image.return_value, save_to='.')
        self.assertEqual(filename, save_image.return_value)
