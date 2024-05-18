import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        divans = response.css('div._Ud0k')
        for divan in divans:
            yield {
                'name' : divan.css('div.lsooF span::text').get(),
                'price' : divan.css('div.q5Uds span::text').get(),
            }



