import scrapy

class WeLiveSecurity_spider(scrapy.Spider):
    name = "WeLiveSecurity"

    def start_requests(self):
        urls = [
            "https://www.welivesecurity.com"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Get webpage
    # Parse out article data
    # Store and dedupe
    def parse(self, response):
        articles = response.css('.news-feed-item')
        # for a in articles:
        #     self.log(a.extract())

        article_title = ""
        date_published = ""
        short_description = ""
        article_link = ""
        author = ""

        articles_parsed = []
        for a in articles:
            article_title = a.css(".text-wrapper a::text").extract_first()
            date_published = a.css(".text-wrapper .meta time::attr(datetime)").extract_first()
            short_description = a.css(".text-wrapper p::text").extract_first()
            article_link = a.css(".text-wrapper h2 a::attr(href)").extract_first()
            author = a.css(".text-wrapper span a::text").extract_first()

            a_dict = {
                "article_title": article_title.strip(),
                "date_published": date_published,
                "short_description": short_description,
                "article_link": article_link,
                "author": author,
            }

            print(a_dict)
            articles_parsed.append(a_dict)
            print("================")
            # print(elt)


        # self.log(articles)
        # self.log(response.body)
        # with open('welivesecurity.txt', 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved data from We Live Security')
