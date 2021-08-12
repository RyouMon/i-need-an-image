import json
import random
from io import BytesIO

import requests
from PIL import Image
from bs4 import BeautifulSoup


class BingImage:

    url = 'https://cn.bing.com/images/search'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'
    }

    def get_image_source_url(self, response):
        soup = BeautifulSoup(response.text, features='lxml')

        image_component = soup.find(id='mmComponent_images_1')
        images = image_component.find_all('a', class_='iusc')
        image = random.choice(images)
        metadata = json.loads(image['m'])
        source_url = metadata['murl']

        return source_url

    def get_an_image(self, keyword):
        """
        return an Image matching keyword from web
        """
        response = self.download_search_page(keyword)
        source_url = self.get_image_source_url(response)
        image_content = self.download_image(source_url)
        return Image.open(BytesIO(image_content))

    def download_image(self, source_url):
        """
        request picture, return binary data
        """
        response = requests.get(source_url, headers=self.headers)
        return response.content

    def download_search_page(self, keyword):
        """
        Send an image search search_request
        """
        payload = {'q': keyword}
        return requests.get(self.url, params=payload, headers=self.headers)
