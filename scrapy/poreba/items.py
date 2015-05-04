# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BikeItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    category_image = scrapy.Field()
    main_image = scrapy.Field()
    big_image = scrapy.Field()
    
    price = scrapy.Field()
    promo_price = scrapy.Field()
    
    rama = scrapy.Field()
    dumper = scrapy.Field()
    widelec = scrapy.Field()
    stery = scrapy.Field()
    os_supportu = scrapy.Field()
    korby = scrapy.Field()
    wspor_kier = scrapy.Field()
    wspor_siodla = scrapy.Field()
    kierownica = scrapy.Field()
    przerzutka_przod = scrapy.Field()
    przerzutka_tyl = scrapy.Field()
    hamulce = scrapy.Field()
    manetki = scrapy.Field()
    siodlo = scrapy.Field()
    kola = scrapy.Field()
    kaseta = scrapy.Field()
    opony = scrapy.Field()
    waga = scrapy.Field()
    rozmiar = scrapy.Field()
