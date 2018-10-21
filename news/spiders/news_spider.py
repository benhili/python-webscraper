from scrapy import Spider, Request
from scrapy.selector import Selector
from news.items import NewsItem
from urllib.parse import urljoin
from bs4 import BeautifulSoup


class NewsSpider(Spider):
    name = "news"
    allowed_domains = ["www.theguardian.com"]
    start_urls = ["https://www.theguardian.com/australia-news/"]

    def parse(self, response):
        headlines = Selector(response).xpath(
            "//*[@id='australia-news']//a[contains(@class, 'js-headline-text')]/@href"
        )
        for headline in headlines:
            headline_url = urljoin(response.url, headline.extract())
            yield Request(headline_url, callback=self.parse_article)

    def parse_article(self, response):
        item = NewsItem()
        item["url"] = response.url
        soup = BeautifulSoup(response.text, "html.parser")
        item["headline"] = soup.find("h1", class_="content__headline").text
        item["author"] = soup.find("p", class_="byline").text

        # Strip social media from body
        soup.find("div", class_="submeta").decompose()
        item["body"] = soup.find("div", class_="content__article-body").text
        yield item
