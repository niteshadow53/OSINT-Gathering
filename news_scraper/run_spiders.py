from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def main():
    spiders = [
        "TrendMicro",
        "CiscoTalos",
        "SecurityIntelligence",
        "WeLiveSecurity",
        "WallStreetJournal",
    ]

    process = CrawlerProcess(get_project_settings())

    for spider in spiders:
        # process = CrawlerProcess(get_project_settings())
        process.crawl(spider)
    process.start()


if __name__ == "__main__":
    main()
