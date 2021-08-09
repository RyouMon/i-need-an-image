from unittest import TestCase
from unittest.mock import patch
import need_an_image


class OneImageFromBingTest(TestCase):

    @patch('need_an_image.bing')
    def test_call_bing_get_an_image(self, mock_bing):
        filename = need_an_image.from_bing(keyword='猫')

        mock_bing.get_an_image.assert_called_once_with(keyword='猫')
        self.assertEqual(filename, mock_bing.get_an_image.return_value)
