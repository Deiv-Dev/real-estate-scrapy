import scrapy
from fake_useragent import UserAgent
import random


class AruodSpider(scrapy.Spider):
    name = "aruod"
    allowed_domains = ["en.aruodas.lt"]
    start_urls = ["https://en.aruodas.lt/butai/kaune/"]

    custom_headers = [
        {
            "User-Agent": "User-Agent-1",
            "Accept": "Accept-1",
            "Accept-Language": "Accept-Language-1",
            "Referer": "Referer-1",
            "Connection": "Connection-1",
            "Cache-Control": "Cache-Control-1",
        },
        {
            "User-Agent": "User-Agent-2",
            "Accept": "Accept-2",
            "Accept-Language": "Accept-Language-2",
            "Referer": "Referer-2",
            "Connection": "Connection-2",
            "Cache-Control": "Cache-Control-2",
        },
        # Define similar dictionaries for the other 8 options
    ]

    def start_requests(self):
        for url in self.start_urls:
            headers = self.get_random_headers()
            yield scrapy.Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        # Find all elements with the class 'list-row-v2'
        list_row_elements = response.css('div.list-row-v2')

        for element in list_row_elements:
            # You can yield the HTML content of each element
            yield {
                'element_html': element.extract()
            }

    def get_random_headers(self):
        # Select a random set of headers from the predefined options
        random_headers = random.choice(self.custom_headers)
        return random_headers
