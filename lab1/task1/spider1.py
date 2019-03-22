import scrapy


class QuotesSpider(scrapy.Spider):
    name = "fragments"


    def start_requests(self):
        urls = [
            'https://shkola.ua/shkoli?page='
        ]
        for i in range(3):
            next_url = urls[0]+str(i+1)
            yield scrapy.Request(url=next_url, callback=self.parse)


    def parse(self, response):

        if response.body is not None:
            filename = 'pages.html'
            with open(filename, "a+") as f:
                f.write(response.body)
                f.write("\n\n")
            self.log('Saved file %s' % filename)