# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from poreba.items import BikeItem

class CategorySpider(CrawlSpider):
    name = "category"
    allowed_domains = ["porebarowery.pl"]
    # kategorie: 
    # szosowe: 86, pages: 1-4
    # mtb: 87, pages: 1-8
    # trekingowe: 88, pages: 1-2
    # miejskie: 89, pages: 0
    start_urls = ['http://porebarowery.pl/main/offer/producer:5,category:89,page:1']
    
    rules = [
        Rule(LinkExtractor(allow=r'main/offer/producer:5,category:89,page:[1-8]'),
             callback='parse_category', follow=True)
    ]

    def parse_category(self, response):
        items = Selector(response).xpath('//li[@class="item"]')

        for item in items:
            bike = BikeItem()
            bike['link'] = item.xpath('a/@href').extract()[0]
            bike['name'] = item.xpath('a/strong/text()').extract()[0]
            bike['category_image'] = item.xpath('a/img/@src').extract()[0]
            
            yield bike
