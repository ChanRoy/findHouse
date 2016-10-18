# -*- coding=UTF-8 -*-

from scrapy import Spider
from scrapy.selector import Selector
from findHouse.items import FindhouseItem

class findHouseSpider(Spider):
    name = "findHouse"
    allowed_domains = ["hk.qfang.com"]
    start_urls = [
        "http://hk.qfang.com/sale",
    ]
 
    def parse(self, response):

        houses = Selector(response).xpath('//*[@class="listings-item-title clearfix"]/h3')
 
        for house in houses:
            item = FindhouseItem()
            text = house.xpath(
                'a[@class="showKeyword"]/text()').extract()[0]
            url = house.xpath(
                'a[@class="showKeyword"]/@href').extract()[0]

            item['text'] = text;
            item['url'] = url;

            yield item