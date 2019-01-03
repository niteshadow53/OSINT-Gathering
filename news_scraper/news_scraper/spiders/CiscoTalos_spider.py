import scrapy
import json
import datetime

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

        article_title = ""
        date_published = ""
        short_description = ""
        article_link = ""
        author = ""

        articles_parsed = []
        for a in articles:
            article_title = a.css("title::text").extract_first()
            print("Title: " + article_title)
            article_link = a.css("link::text").extract_first()
            print("Link: " + article_link)
            author = a.css("author::text").extract_first()
            print("Author: " + author)
            date_published = a.css("pubDate::text").extract_first()
            print("Date: " + date_published)
            print("===========================")

            date_published = datetime.datetime.strptime(date_published, "%a, %d %b %Y %H:%M:%S PST") + datetime.timedelta(hours=3)
            date_published = date_published.isoformat()
            a_dict = {
                "article_title": article_title.strip(),
                "date_published": date_published,
                "short_description": short_description,
                "article_link": article_link,
                "author": author,
                "source": "Cisco Talos Intelligence Blog"
            }

            articles_parsed.append(a_dict)

        with open('ciscotalos.json', 'w') as f:
            f.write(json.dumps(articles_parsed))
