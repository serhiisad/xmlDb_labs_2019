import scrapy
from lxml import etree
import lxml.html


class MySpider(scrapy.Spider):
    name = "shop-spider"

    def start_requests(self):
        urls = [
            'https://tennismag.com.ua/catalog/muzhskie-krossovki-nike/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for item in response.xpath('//div[@class="bxr-element-container"]')[:20]:
            image_url = item.xpath('.//div[@class="bxr-element-image"]/a/img/@src').extract_first()

            yield {
                'title': item.xpath('.//div[@class="bxr-element-name"]/a/text()').extract_first(),
                'price': item.xpath('.//span[@class="bxr-market-current-price bxr-market-format-price"]/text()').extract_first(),
                'image_urls': "https://tennismag.com.ua" + image_url
            }

from scrapy.crawler import CrawlerProcess
#
# c = CrawlerProcess({
#     'FEED_FORMAT': 'xml',
#     'FEED_URI': 'tennis-shoes.xml',
# })
#
# c.crawl(MySpider)
# c.start()



