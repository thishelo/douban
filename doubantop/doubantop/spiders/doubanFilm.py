# -*- coding: utf-8 -*-
import scrapy

from doubantop.items import DoubantopItem


class DoubanfilmSpider(scrapy.Spider):
    name = 'doubanFilm'
    allowed_domains = ['douban.com']
    offset = 0

    url = "https://movie.douban.com/top250?start="
    start_urls = [url+str(offset),]

    def parse(self, response):
        items = DoubantopItem()

        Films = response.xpath()

        for each in Films:
        	item['title'] = each.xpath(".//span[@class='title'][1]/text()").extract()[0]
            # 信息
            item['bd'] = each.xpath(".//div[@class='bd']/p/text()").extract()[0]
            # 评分
            item['star'] = each.xpath(".//div[@class='star']/span[@class='rating_num']/text()").extract()[0]
            # 简介
            item['quote'] = each.xpath(".//p[@class='quote']/span/text()").extract()[0]
            yield item
        if self.offset < 225:
            	self.offset += 25
            	yield scrapy.Request(self.url + str(self.offset), callback = self.parse)    