from scrapy import Spider
from scrapy.selector import Selector
from news.items import NewsItem


class NewsSpider(Spider):
    name = "news"
    allowed_domains = ["www.theguardian.com"]
    start_urls = ["https://www.theguardian.com/australia-news/"]

    def parse(self, response):
        headlines = Selector(response).xpath(
            "//*[@id='australia-news']//a[contains(@class, 'js-headline-text')]"
        )

        for headline in headlines:
            item = NewsItem()
            item["title"] = headline.xpath("text()").extract()[0]
            item["url"] = headline.xpath("@href").extract()[0]
            yield item
