from io import BytesIO
import requests
from PIL import Image


class BingImage:

    url = 'https://cn.bing.com/images/search'

    def get_image_source_url(self, keyword):
        response = self.search_request(keyword=keyword)
        return self.parse_source(response)

    def get_an_image(self, keyword):
        source_url = self.get_image_source_url(keyword)
        image_content = self.download_image(source_url)
        return Image.open(BytesIO(image_content))

    def get_search_params(self, keyword):
        return {'q': keyword}

    def download_image(self, source_url):
        response = requests.get(source_url)
        return response.content

    def parse_source(self, response):
        return 'https://example.com/image.png'

    def search_request(self, keyword):
        """
        Send an image search search_request
        """
        payload = self.get_search_params(keyword=keyword)
        return requests.get(self.url, params=payload)
