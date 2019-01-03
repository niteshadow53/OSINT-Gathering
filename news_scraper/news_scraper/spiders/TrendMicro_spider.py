import scrapy
import json
import datetime

class WeLiveSecurity_spider(scrapy.Spider):
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
        articles = response.css('#pageContent div.post')
        # for a in articles:
        #     self.log(a.extract())

        article_title = ""
        date_published = ""
        short_description = ""
        article_link = ""
        author = ""

        articles_parsed = []
        for a in articles:
            article_title = a.css("div.post-title h1::text").extract_first()
            date_published = a.css("li.post-date a::text").extract_first() + " " + a.css("li.post-date span::text").extract_first()
            short_description = a.css("div.post-text p::text").extract_first()
            article_link = a.css("div.post-title a::attr(href)").extract_first()
            author = ""

            date_published = datetime.datetime.strptime(date_published, "%B %d, %Y at %H:%M %p").isoformat()
            a_dict = {
                "article_title": article_title.strip(),
                "date_published": date_published,
                "short_description": short_description,
                "article_link": article_link,
                "author": author,
                "source": "Trend Micro"
            }

            print(a_dict)
            articles_parsed.append(a_dict)
            print("================")
            # print(elt)

        with open('trendmicro.json', 'w') as f:
            f.write(json.dumps(articles_parsed))
