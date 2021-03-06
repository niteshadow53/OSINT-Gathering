import scrapy
import json
import datetime
import pprint

class SecurityIntelligence_spider(scrapy.Spider):
    name = "SecurityIntelligence"

    def start_requests(self):
        urls = [
            "https://securityintelligence.com/news/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Get webpage
    # Parse out article data
    # Store and dedupe (not finished yet)
    def parse(self, response):
        articles = response.css('div.news-stream.loop article')
        # for a in articles:
        #     self.log(a.extract())

        article_title = ""
        date_published = ""
        short_description = ""
        article_link = ""
        author = ""

        articles_parsed = []
        for a in articles:
            article_title = a.css("div.content a::text").extract_first()
            date_published = a.css("div.content span.date-time::text").extract_first()
            short_description = a.css("div.img span::text").extract_first()
            article_link = a.css("div.content a::attr(href)").extract_first()
            author = ""

            # try:
            #     date_published = datetime.datetime.strptime(date_published, "%b %d, %Y").isoformat()
            # except:
            #     date_published = datetime.datetime.today().isoformat()
            try:
                date_published = datetime.datetime.strptime(date_published, "%b %d, %Y").isoformat()
            except:
                pass
            print(date_published[1:])
            if date_published[1:].strip() == "days ago":
                time_delta = datetime.timedelta(days=int(date_published[0]))
                date_published = (datetime.datetime.today() - time_delta).isoformat()
            if int(date_published[0:2]) > 10 and date_published[2:].strip() == "days ago":
                time_delta = datetime.timedelta(days=int(date_published[0:2]))
                date_published = (datetime.datetime.today() - time_delta).isoformat()
            if date_published[1:].strip() == "hours ago":
                time_delta = datetime.timedelta(hours=int(date_published[0]))
                date_published = (datetime.datetime.today() - time_delta).isoformat()
            if int(date_published[0:2]) > 10 and date_published[2:].strip() == "hours ago":
                time_delta = datetime.timedelta(hours=int(date_published[0:2]))
                date_published = (datetime.datetime.today() - time_delta).isoformat()
            a_dict = {
                "article_title": article_title.strip(),
                "date_published": date_published,
                "short_description": short_description,
                "article_link": article_link,
                "author": author,
                "source": "IBM Security Intelligence"
            }

            # print(a_dict)
            articles_parsed.append(a_dict)
            # print("================")
            # # print(elt)

        # Need to do some extra parsing to pick out the top story ==========
        a = response.css("div.news-stream.large article")

        article_title = a.css("div.content h4 a::text").extract_first()
        date_published = a.css("div.content span.date-time::text").extract_first()
        short_description = a.css("div.content div.body::text").extract_first()
        article_link = a.css("div.content a::attr(href)").extract_first()
        author = ""

        try:
            date_published = datetime.datetime.strptime(date_published, "%b %d, %Y").isoformat()
        except:
            pass
        if date_published[1:].strip() == "days ago":
            time_delta = datetime.timedelta(days=int(date_published[0]))
            date_published = (datetime.datetime.today() - time_delta).isoformat()
        if int(date_published[0:2]) > 10 and date_published[2:].strip() == "days ago":
            time_delta = datetime.timedelta(days=int(date_published[0:2]))
            date_published = (datetime.datetime.today() - time_delta).isoformat()
        if date_published[1:].strip() == "hours ago":
            time_delta = datetime.timedelta(hours=int(date_published[0]))
            date_published = (datetime.datetime.today() - time_delta).isoformat()
        if int(date_published[0:2]) > 10 and date_published[2:].strip() == "hours ago":
            time_delta = datetime.timedelta(hours=int(date_published[0:2]))
            date_published = (datetime.datetime.today() - time_delta).isoformat()

        # date_published = datetime.datetime.today().isoformat()
        a_dict = {
            "article_title": article_title.strip(),
            "date_published": date_published,
            "short_description": short_description,
            "article_link": article_link,
            "author": author,
            "source": "IBM Security Intelligence"
        }
        articles_parsed.append(a_dict)
        # End top story parsing ============================================

        for each in articles_parsed:
            pprint.pprint(each)



        with open('securityintelligence.json', 'w') as f:
            f.write(json.dumps(articles_parsed))
        # self.log(articles)
        # self.log(response.body)
        # with open('welivesecurity.txt', 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved data from We Live Security')
