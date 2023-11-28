import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = [
        "https://www.imdb.com/chart/top/"
    ]

    def parse(self, response):
        title = response.css('span::secondaryInfo').get()
        yield {'title': title}
