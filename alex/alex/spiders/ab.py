# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy import Request
from alex.items import AlexItem
#from alex.settings import AB_VARS

class DogSpider(CrawlSpider):
    name = 'ab'
    allowed_domains = ['ab.gr']
    kava_urls = ['https://www.ab.gr/click2shop/Krasia-pota-anapsyktika-nera/c/008?pageNumber={}'.format(x) for x in range(0,54)]
    oporopoleio_urls = ['https://www.ab.gr/click2shop/Oporopoleio/c/001?pageNumber={}'.format(x) for x in range(0,11)]
    kreata_urls = ['https://www.ab.gr/click2shop/Fresko-Kreas-and-Psaria/c/002?pageNumber={}'.format(x) for x in range(0,7)]
    psigeiou_urls = ['https://www.ab.gr/click2shop/Galaktokomika-and-Eidi-Psygeioy/c/003?pageNumber={}'.format(x) for x in range(0,38)]
    proswpikis_urls = ['https://www.ab.gr/click2shop/Eidi-prosopikis-peripoiisis/c/012?pageNumber={}'.format(x) for x in range(0,90)]
    katoikidia_urls = ['https://www.ab.gr/click2shop/Gia-katoikidia/c/014?pageNumber={}'.format(x) for x in range(0,12)]
    spitiou_urls = ['https://www.ab.gr/click2shop/Katharistika-Chartika-and-eidi-spitioy/c/013?pageNumber={}'.format(x) for x in range(0,64)]
    urls = kava_urls + oporopoleio_urls + kreata_urls + psigeiou_urls + katoikidia_urls + spitiou_urls
    start_urls = urls[:]
    


    rules = (
        Rule(LinkExtractor(allow=("Katharistika/","Axesoyar-katharismoy/","Aporrypantika-piaton/","Aporrypantika-plyntirioy-roychon/","Malaktika-roychon/"),deny=("c/")), callback='parse_AB_spitiou', follow=True), 
        Rule(LinkExtractor(allow=("Leykantika-Enischytika/","Aposkliryntika-plyntirioy/","Aporrypantika-cherioy/","Charti-oikiakis-chrisis/","Eidi-oikiakis-chrisis","Epochiaka/"),deny=('c/')), callback='parse_AB_spitiou', follow=True), 
        Rule(LinkExtractor(allow=("Entomoktona-Entomoapothitika/","Fylaxi-roychon/","Eidi-sideromatos-aplomatos","Aromatika-Keria/","/Grafiki-yli-Analosima","Dora-Paichnidia/","Eidi-aytokinitoy/"),deny=('c/')), callback='parse_AB_spitiou', follow=True), 
        Rule(LinkExtractor(allow=("Gia-gates/","Gia-skyloys/","Ygieini-zoon/"),deny=('c/')), callback='parse_AB_katoikidia', follow=True), 
        Rule(LinkExtractor(allow=("/Krasia/","Anapsyktika","Nera","Pota"),deny=('c/')), callback='parse_AB_kava', follow=True), 
        Rule(LinkExtractor(allow=("Froyta/","Lachanika/","Nopoi-xiroi-karpoi/"),deny=('c/')), callback='parse_AB_freska', follow=True),
        Rule(LinkExtractor(allow=("Loykanika/","Etoimes-Lyseis/","/Kynigi/","Freska-psaria-and-thalassina/"),deny=('c/')), callback='parse_AB_freska', follow=True),
        Rule(LinkExtractor(allow=("/Gala/","Giaoyrtia/","Kremes-Glykismata/","Voytyro-Margarini/","Kremes-galaktos-and-santigy/","Freskes-zymes-Fylla-Magia/","Freskoi-Zomoi/","Chymoi-psygeioy/","Ayga"),deny=('c/')), callback='parse_AB_psigeiou', follow=True),
        Rule(LinkExtractor(allow=("Fresko-Kreas-and-Psaria","Moschari-gia-tin-katsarola-i-to-foyrno","Moschari-gia-tin-schara-i-to-tigani/","Choirino-gia-tin-schara-i-to-tigani/","Choirino-gia-ti-gastra-tin-katsarola-i-to-foyrno/","Kotopoylo-gia-to-tigani/c","Choirino-gia-ti-gastra-tin-katsarola-i-to-foyrno/","/Kotopoylo-gia-psito-i-vrasto/","Galopoyla/","Kimas/"),deny=('c/')), callback='parse_AB_freska', follow=True),
        Rule(LinkExtractor(allow=("Andriki-peripoiisi","Gynaikeia-peripoiisi","Prosopiki-ygieini/","Frontida-somatos/","Frontida-mallion/","Stomatiki-ygieini/","Antiiliaka","Parafarmakeytika"),deny=('c/')), callback='parse_AB_proswpikis', follow=True),
        )



    def parse_AB_kava(self,response):
        producer = response.xpath('//p[@class="page-title-info"]/text()').get()
        producer = re.sub(r'\n|\s\s',"",producer)
        if producer is None or len(producer) < 2:
            producer = "Τοπικός Παραγωγός"
        yield{
            "category": "Κάβα",
            "name": response.xpath('//h1/text()').get(),
            "producer": producer, #re.sub(r'\n|\s\s',"",response.xpath('//p[@class="page-title-info"]/text()').get()),
            "price": re.search(r'(\d+),(\d+)',response.xpath('//span[@class="ultra-bold test-price-property"]/text()').get()).group(0),
            "barcode": re.search(r'(\d+)',response.xpath('//div[@class="col-sm-60 product-description-id"]/p/text()|//div[@class="color_grey_5"]/p/text()').get()).group(0),
            "url": response.url
        }

    def parse_AB_freska(self,response):
        producer = response.xpath('//p[@class="page-title-info"]/text()').get()
        producer = re.sub(r'\n|\s\s',"",producer)
        if producer is None or len(producer) < 2:
            producer = "Τοπικός Παραγωγός"
        yield{
            "category": "Φρέσκα Προϊόντα",
            "name": response.xpath('//h1/text()').get(),
            "producer": producer,#re.sub(r'\n|\s\s',"",response.xpath('//p[@class="page-title-info"]/text()').get()),
            "price": re.search(r'(\d+),(\d+)',response.xpath('//span[@class="ultra-bold test-price-property"]/text()').get()).group(0),
            "barcode": re.search(r'(\d+)',response.xpath('//div[@class="col-sm-60 product-description-id"]/p/text()|//div[@class="color_grey_5"]/p/text()').get()).group(0),
            "url": response.url
        }

    def parse_AB_psigeiou(self,response):
        producer = response.xpath('//p[@class="page-title-info"]/text()').get()
        producer = re.sub(r'\n|\s\s',"",producer)
        if producer is None or len(producer) < 2:
            producer = "Τοπικός Παραγωγός"
        yield{
            "category": "Ποϊόντα Ψυγείου",
            "name": response.xpath('//h1/text()').get(),
            "producer": producer,#re.sub(r'\n|\s\s',"",response.xpath('//p[@class="page-title-info"]/text()').get()),
            "price": re.search(r'(\d+),(\d+)',response.xpath('//span[@class="ultra-bold test-price-property"]/text()').get()).group(0),
            "barcode": re.search(r'(\d+)',response.xpath('//div[@class="col-sm-60 product-description-id"]/p/text()|//div[@class="color_grey_5"]/p/text()').get()).group(0),
            "url": response.url
        }

    def parse_AB_katoikidia(self,response):
        producer = response.xpath('//p[@class="page-title-info"]/text()').get()
        producer = re.sub(r'\n|\s\s',"",producer)
        if producer is None or len(producer) < 2:
            producer = "Τοπικός Παραγωγός"
        yield{
            "category": "Κατοικίδια",
            "name": response.xpath('//h1/text()').get(),
            "producer": producer, #re.sub(r'\n|\s\s',"",response.xpath('//p[@class="page-title-info"]/text()').get()),
            "price": re.search(r'(\d+),(\d+)',response.xpath('//span[@class="ultra-bold test-price-property"]/text()').get()).group(0),
            "barcode": re.search(r'(\d+)',response.xpath('//div[@class="col-sm-60 product-description-id"]/p/text()|//div[@class="color_grey_5"]/p/text()').get()).group(0),
            "url": response.url
        }

    def parse_AB_spitiou(self,response):
        producer = response.xpath('//p[@class="page-title-info"]/text()').get()
        producer = re.sub(r'\n|\s\s',"",producer)
        if producer is None or len(producer) < 2:
            producer = "Τοπικός Παραγωγός"
        yield{
            "category": "Είδη Σπιτιού",
            "name": response.xpath('//h1/text()').get(),
            "producer": producer, #re.sub(r'\n|\s\s',"",response.xpath('//p[@class="page-title-info"]/text()').get()),
            "price": re.search(r'(\d+),(\d+)',response.xpath('//span[@class="ultra-bold test-price-property"]/text()').get()).group(0),
            "barcode": re.search(r'(\d+)',response.xpath('//div[@class="col-sm-60 product-description-id"]/p/text()|//div[@class="color_grey_5"]/p/text()').get()).group(0),
            "url": response.url
        }

    def parse_AB_proswpikis(self,response):
        producer = response.xpath('//p[@class="page-title-info"]/text()').get()
        producer = re.sub(r'\n|\s\s',"",producer)
        if producer is None or len(producer) < 2:
            producer = "Τοπικός Παραγωγός"
        yield{
            "category": "Προσωπικής Περιποίησης",
            "name": response.xpath('//h1/text()').get(),
            "producer": producer, #re.sub(r'\n|\s\s',"",response.xpath('//p[@class="page-title-info"]/text()').get()),
            "price": re.search(r'(\d+),(\d+)',response.xpath('//span[@class="ultra-bold test-price-property"]/text()').get()).group(0),
            "barcode": re.search(r'(\d+)',response.xpath('//div[@class="col-sm-60 product-description-id"]/p/text()|//div[@class="color_grey_5"]/p/text()').get()).group(0),
            "url": response.url
        }
    
 