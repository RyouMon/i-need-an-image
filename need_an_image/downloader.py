import json
import random
from io import BytesIO

import requests
from PIL import Image
from bs4 import BeautifulSoup


class BingImage:

    url = 'https://cn.bing.com/images/search'

    def get_image_source_url(self, keyword):
        response = self.search_request(keyword=keyword)
        return self.parse_source(response)

    def get_an_image(self, keyword):
        """
        return an Image matching keyword from web
        """
        source_url = self.get_image_source_url(keyword)
        image_content = self.download_image(source_url)
        return Image.open(BytesIO(image_content))

    def get_search_params(self, keyword):
        return {'q': keyword}

    def download_image(self, source_url):
        """
        request picture, return binary data
        """
        response = requests.get(source_url)
        return response.content

    def parse_source(self, response):
        soup = BeautifulSoup(response.text, features='lxml')

        image_component = soup.find(id='mmComponent_images_1')
        images = image_component.find_all('a', class_='iusc')
        image = random.choice(images)
        metadata = json.loads(image['m'])
        source_url = metadata['murl']

        return source_url

    def search_request(self, keyword):
        """
        Send an image search search_request
        """
        payload = self.get_search_params(keyword=keyword)
        return requests.get(self.url, params=payload)
