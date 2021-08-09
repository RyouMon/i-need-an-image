from PIL import Image


class BingImage:

    def get_image_info(self, keyword):
        response = self.request(keyword=keyword)
        return self.parse_source(response)

    def get_an_image(self, keyword):
        mode, size, source_url = self.get_image_info(keyword)
        image_content = self.download_image(source_url)
        return Image.frombytes(size=size, mode=mode, data=image_content)

    def download_image(self, source_url):
        pass

    def parse_source(self, response):
        return 'RGB', (1, 1), 'https://example.com/image.png'

    def request(self, keyword):
        pass
