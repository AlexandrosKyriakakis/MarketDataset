# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AlexItem(scrapy.Item):
    producer =  scrapy.Field()
    price = scrapy.Field()
    name = scrapy.Field()
    barcode =  scrapy.Field()
    category = scrapy.Field()
    url = scrapy.Field()
    # name = scrapy.Field()
    pass
