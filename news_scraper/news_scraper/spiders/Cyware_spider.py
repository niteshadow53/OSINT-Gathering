import scrapy
import json
import datetime

class Cyware_spider(scrapy.Spider):
    name = "Cyware"

    def start_requests(self):
        urls = [
            "https://cyware.com/cyber-security-news-articles"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Get webpage
    # Parse out article data
    # Store and dedupe (not finished yet)
    def parse(self, response):
        articles = response.css('div#card-stack div.post')
        # for a in articles:
        #     self.log(a.extract())

        article_title = ""
        date_published = ""
        short_description = ""
        article_link = ""
        author = ""

        articles_parsed = []
        for a in articles:
            article_title = a.css("h2.post-title a::text").extract_first()
            date_published = a.css("ul.meta li.date::text").extract_first()
            short_description = ""
            article_link = a.css("h2.post-title a::attr(href)").extract_first()
            author = ""

            date_published = datetime.datetime.strptime(date_published, "%b %d, %Y").isoformat()
            a_dict = {
                "article_title": article_title.strip(),
                "date_published": date_published,
                "short_description": short_description,
                "article_link": article_link,
                "author": author,
                "source": "Cyware"
            }

            print(a_dict)
            articles_parsed.append(a_dict)
            print("================")
            # print(elt)

        with open('cyware.json', 'w') as f:
            f.write(json.dumps(articles_parsed))
