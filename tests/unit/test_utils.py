import os
from unittest import TestCase
from unittest.mock import patch, MagicMock
import need_an_image


class SaveImageTest(TestCase):

    @patch('need_an_image.uuid4')
    def test_save_Image_to_current_path(self, mock_uuid4):
        mock_image = MagicMock()
        mock_uuid4.return_value.hex = 'image'
        filename = need_an_image.save_image(mock_image)

        save_to_path = os.path.join('.', 'image.jpg')
        mock_image.save.assert_called_once_with(save_to_path)
        self.assertEqual(filename, save_to_path)

    @patch('need_an_image.uuid4')
    def test_save_Image_to_other_path(self, mock_uuid4):
        mock_image = MagicMock()
        mock_uuid4.return_value.hex = 'image'
        filename = need_an_image.save_image(mock_image, save_to='/tmp/')

        save_to_path = os.path.join('/tmp/', 'image.jpg')
        mock_image.save.assert_called_once_with(save_to_path)
        self.assertEqual(filename, save_to_path)
