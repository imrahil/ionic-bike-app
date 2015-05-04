# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy import Request
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from poreba.items import BikeItem


class DetailsSpider(CrawlSpider):
    name = 'details'
    allowed_domains = ['porebarowery.pl']
    # kategorie: 
    # szosowe: 86, pages: 1-4
    # mtb: 87, pages: 1-8
    # trekingowe: 88, pages: 1-2
    # miejskie: 89, pages: 0
    start_urls = ['http://porebarowery.pl/main/offer/producer:5,category:88,page:1']

    rules = [
        Rule(LinkExtractor(allow=r'main/offer/producer:5,category:88,page:[1-2]'), 
            callback='parse_category', follow=True)
    ]

    def parse_category(self, response):
        items = Selector(response).xpath('//li[@class="item"]')

        for item in items:
            bike = BikeItem()
            bike['link'] = item.xpath('a/@href').extract()[0]
            bike['name'] = item.xpath('a/strong/text()').extract()[0]
            bike['category_image'] = item.xpath('a/img/@src').extract()[0]
            
            request = Request('http://porebarowery.pl' + bike['link'], callback=self.parse_item)
            request.meta['bike'] = bike

            yield request

    def parse_item(self, response):
        self.log("Visited %s" % response.url)
        bike = response.meta['bike']
        bike['main_image'] = response.xpath('//div[@class="product_main_picture"]/a/img/@src').extract()[0]
        bike['big_image'] = response.xpath('//div[@class="product_main_picture"]/a/@href').extract()[0]

        spec = response.xpath('//div[@class="product_spec"]/table/tr')
        values = ['rama', 'dumper', 'widelec', 'stery', 'os_supportu', 'korby', 'wspor_kier', 'wspor_siodla', 'kierownica', 'przerzutka_przod', 'przerzutka_tyl', 'hamulce', 'manetki', 'siodlo', 'kola', 'kaseta', 'opony', 'waga', 'rozmiar']

        pos = 0
        for i in values:
            specItem = spec[pos].xpath('td/text()').extract()
            bike[i] = specItem[0] if (len(specItem) != 0) else "-"
            pos += 1
            
        yield bike
