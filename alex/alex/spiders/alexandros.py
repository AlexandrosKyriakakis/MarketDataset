# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy import Request
from alex.items import AlexItem


class AlexandrosSpider(CrawlSpider):
    name = 'alexandros'
    allowed_domains = ['spitogatos.gr']
    start_urls = ['https://www.spitogatos.gr/πώληση_Μεζονέτα_Άνω_Κυψέλη_-_Ευελπίδων__Κέντρο_Αθήνας_-l9297911']
    #start_urls = ['https://www.xe.gr/property/search?Geo.area_id_new__hierarchy=82271&System.item_type=re_residence&Transaction.type_channel=117518']

    rules = (
        Rule(LinkExtractor(allow=("spitogatos.gr")), callback='parse', follow=True), 
        )
    def parse(self, response):
        print("HEEEEELLLLLLLLLLLLL")
        #url = response.url
        yield { 
            "name": response.xpath('//h1/text()').get(),#response.xpath('//div[@id="breadCrumbs"]/span/text()').get(), #re.search(r"(/d+)",name),
            "price": response.xpath('//h6[@class="text black inline color bold vertical-middle padding-right-small"]/text()').get(),
        }
        

    #def parseInfiniteXe(self,response):
    #    pages =  1691
    #    for page in range(0, pages):
    #        url = 'https://www.xe.gr/property/search?Geo.area_id_new__hierarchy=82271&System.item_type=re_residence&Transaction.type_channel=117518&page={}'.format(page)
    #        yield Request(url, callback = self.parseItemXe) 
#
    #def parseItemXe(self,response):
    #    links = response.xpath('//a[@class="articleLink"]/@href').getall()
    #    for link in links:
    #        url = response.urljoin(link)
    #        yield Request(url,callback=self.parseItem) #"url": response.urljoin(link),
    #        
    #def parseItem(self, response):
    #    #name = response.xpath('//span[@class="codeInfo"]/text()').get()
    #    #name = " ".join(" ".join(name))
    #    yield {
    #        "name": response.xpath('//span[@class="codeInfo"]/text()').get(), #re.search(r"(/d+)",name),
    #        "price": response.xpath('//div[@class="price"]/h1/text()').get(),
    #    }
#