import scrapy
import json
import datetime

class WallStreetJournal_spider(scrapy.Spider):
    name = "WallStreetJournal"

    def start_requests(self):
        urls = [
            "http://www.wsj.com/xml/rss/3_7455.xml"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Get webpage
    # Parse out article data
    # Store and dedupe (not finished yet)
    def parse(self, response):
        articles = response.css('item')
        # for a in articles:
        #     self.log(a.extract())

        article_title = ""
        date_published = ""
        short_description = ""
        article_link = ""
        author = ""

        articles_parsed = []
        for a in articles:
            article_title = a.css("title::text").extract_first()
            date_published = a.css("pubDate::text").extract_first()
            short_description = a.css("description::text").extract_first()
            article_link = a.css("link::text").extract_first()
            author = ""

            date_published = datetime.datetime.strptime(date_published, "%a, %d %b %Y %H:%M:%S EST").isoformat()
            a_dict = {
                "article_title": article_title.strip(),
                "date_published": date_published,
                "short_description": short_description,
                "article_link": article_link,
                "author": author,
                "source": "Wall Street Journal"
            }

            print(a_dict)
            articles_parsed.append(a_dict)
            print("================")
            # print(elt)

        with open('trendmicro.json', 'w') as f:
            f.write(json.dumps(articles_parsed))
