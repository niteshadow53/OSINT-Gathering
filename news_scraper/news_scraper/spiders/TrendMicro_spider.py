import scrapy
import json

class TrendMicro_spider(scrapy.Spider):
    name = "TrendMicro"

    def start_requests(self):
        urls = [
            "https://blog.trendmicro.com/trendlabs-security-intelligence/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Get webpage
    # Parse out article data
    # Store and dedupe (not finished yet)
    def parse(self, response):
        articles = ""
