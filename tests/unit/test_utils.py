from unittest import TestCase
from unittest.mock import patch, MagicMock
import need_an_image


class SaveImageTest(TestCase):

    @patch('need_an_image.uuid4')
    def test_save_Image_to_disk(self, mock_uuid4):
        mock_image = MagicMock()
        mock_uuid4.return_value.hex = 'image'
        filename = need_an_image.save_image(mock_image)

        mock_image.save.assert_called_once_with('image.jpg')
        self.assertEqual(filename, 'image.jpg')
