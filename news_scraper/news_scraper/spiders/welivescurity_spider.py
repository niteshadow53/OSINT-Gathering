import scrapy

class WeLiveSecurity_spider(scrapy.Spider):
    name = "WeLiveSecurity"

    def start_requests(self):
        urls = [
            "https://www.welivesecurity.com"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        articles = response.css('.news-feed-item')
        # for a in articles:
        #     self.log(a.extract())

        article_title = ""
        date_published = ""
        article_link = ""

        for a in articles:
            article_title = a.css(".text-wrapper a::text").extract_first()
            print(elt)

        date_published = ""
        article_link = ""
        # self.log(articles)
        # self.log(response.body)
        # with open('welivesecurity.txt', 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved data from We Live Security')
