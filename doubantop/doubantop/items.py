# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubantopItem(scrapy.Item):
    #需要爬取的内容
    #名字
    title = scrapy.Field()
    #信息
    bd = scrapy.Field()
    #评分
    star = scrapy.Field()
    #简介
    quote = scrapy.Field()

