import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "plitkanadompars"
    allowed_domains = ["https://plitkanadom.ru"]
    start_urls = ["https://www.plitkanadom.ru/svet/lyustry"]

    def parse(self, response):
        lyustry = response.css('div.bx_catalog_item_container')
        for lyustra in lyustry:
            yield {
                'name' : lyustra.css('div.bx_catalog_item_title span::text').get(),
                'price' : lyustra.css('div.bx_price span::text').get(),
                'url' : lyustra.css('a.bx_catalog_item_title').attrib['href']
            }
# spyder1 = DivannewparsSpider()
# spyder1.parse()



