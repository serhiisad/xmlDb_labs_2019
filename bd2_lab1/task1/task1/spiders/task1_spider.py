import scrapy
from scrapy import Selector
from lxml import etree

#TASK1 - parse webpages

class MySpider(scrapy.Spider):
    name = "osvita-news-spider"
    # result file root
    root = etree.Element("data")
    start_urls = ['http://osvita.ua/news/', ]
    # start_urls.extend(['http://osvita.ua/news/list/%s/' % str(i+20) for i in range(0, 440, 20)])
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 20
    }

    def parse(self, response):
        if response.body is not None:
            page = etree.SubElement(self.root, 'page')
            page.attrib['url'] = response.url
            print("Parsing URL: ", response.url)

            all_images = response.xpath("//img[@class='h92']/@src").extract()
            all_text = response.xpath("//span[@class='bhead']/a/text()").extract()
            news = zip(all_images, all_text)

            for n in news:
                fragment = etree.SubElement(page, "fragment")
                fragment.attrib['type'] = 'image'
                fragment.text = n[0]
                fragment = etree.SubElement(page, "fragment")
                fragment.attrib['type'] = 'text'
                fragment.text = n[1]
            self.write_to_xml()

            #finding next url in pagination
            pagin_url =  response.xpath(f"//li[@class='current']/following::li/a/@href").extract_first()
            next_url = response.urljoin(pagin_url)
            yield scrapy.Request(url=next_url, callback=self.parse)

    def write_to_xml(self, filename="parsed_news.xml"):
        with open(filename, "wb") as f:
            if self.root.getchildren() is None:
                f.write("No pages to parse")
            else:
                xml_str = etree.tostring(self.root, pretty_print=True, xml_declaration=True, encoding='utf-8')
                f.write(xml_str)
                self.log('SUCCESS: Saved file %s' % filename)

            # yield {
            #     "page": {
            #         "image": news[0],
            #         "text": news[1]
            #     }
            # }
        # next_url = response.xpath(f"//li[@class='current']/following::li/a/@href").extract_first()
        # yield scrapy.Request(next_url, self.parse)
from scrapy.crawler import CrawlerProcess

# c = CrawlerProcess({
#     # 'USER_AGENT': 'Mozilla/5.0',
#
#     'FEED_FORMAT': 'xml',
#     'FEED_URI': 'scraped_news.xml',
#
# })

c = CrawlerProcess()
c.crawl(MySpider)
c.start()

#TASK2 - Кількість текстових фрагментів по кожному документу
def countTextFragments(xml_path):
    count_list = []
    doc_pages = etree.parse(xml_path).xpath("/data/page")
    for page in doc_pages:
        count_list.append(page.xpath("count(./fragment[@type = 'text'])"))
    count_table = dict(zip(list(range(1, len(doc_pages)+1)), count_list))
    return count_table

print(countTextFragments("parsed_news.xml"))