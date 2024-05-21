import scrapy


class Plitkanadompars2Spider(scrapy.Spider):
    name = "plitkanadompars2"
    allowed_domains = ["https://plitkanadom.ru"]
    start_urls = ["https://plitkanadom.ru/svet/lyustry"]

    def parse(self, response):
        lyustry = response.css('div.bx_catalog_item_container')
        for lyustra in lyustry:
            yield {
                'name' : lyustra.css('div.bx_catalog_item_title a::text').get(),
                'price': lyustra.css('div.bx_price::text').get().strip(),
                # 'price_numeric': lyustra.css('div.bx_price::text').get().strip().split()[0],
                'url' : lyustra.css('a.bx_catalog_item_images').attrib['href']
            }