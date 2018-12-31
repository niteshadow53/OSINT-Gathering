import scrapy

class CiscoTalos_spider(scrapy.Spider):
    name="CiscoTalos"

    def start_requests(self):
        urls = [
            # "https://blog.talosintelligence.com"
            "http://feeds.feedburner.com/feedburner/Talos"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    # Get webpage
    # Parse out article data
    # Store and dedupe (not finished)
    def parse(self, response):
        self.log("did I even get here?")
        articles = response.css('rss item')
        # print(articles)
        for a in articles:
            title = a.css("title::text").extract_first()
            print("Title: " + title)
            link = a.css("link::text").extract_first()
            print("Link: " + link)
            author = a.css("author::text").extract_first()
            print("Author: " + author)
            date = a.css("pubDate::text").extract_first()
            print("Date: " + date)
            print("===========================")
