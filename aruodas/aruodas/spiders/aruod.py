import scrapy


class AruodSpider(scrapy.Spider):
    name = "aruod"
    allowed_domains = ["en.aruodas.lt"]
    start_urls = ["https://en.aruodas.lt/butai/kaune/"]

    def parse(self, response):
        # Find all elements with the class 'list-row-v2'
        list_row_elements = response.css('div.list-row-v2')

        for element in list_row_elements:
            # You can yield the HTML content of each element
            yield {
                'element_html': element.extract()
            }
