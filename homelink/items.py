# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HomelinkItem(scrapy.Item):
    communityName = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    houseType = scrapy.Field()
    unitPrice = scrapy.Field()
    totalPrice = scrapy.Field()
    area = scrapy.Field()
    floor = scrapy.Field()
    heading = scrapy.Field()
    decoration = scrapy.Field()
    builtYear = scrapy.Field()
    schoolNames = scrapy.Field()
    district = scrapy.Field()
    token = scrapy.Field()
    metro = scrapy.Field()
