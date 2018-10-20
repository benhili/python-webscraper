from scrapy import Spider


class NewsSpider(Spider):
    name = "news"
    allowed_domains = ["https://www.theguardian.com/"]
    start_urls = ["https://www.theguardian.com/australia-news"]
