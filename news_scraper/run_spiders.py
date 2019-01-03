from scrapy import cmdline

def main():
    spiders = [
        "CiscoTalos",
        "TrendMicro",
        "SecurityIntelligence",
        "WeLiveSecurity"
    ]

    for spider in spiders:
        cmd = "scrapy crawl " + spider
        cmdline.execute(cmd.split())

if __name__ == "__main__":
    main()
