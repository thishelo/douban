# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.conf import setting 

class DoubantopPipeline(object):
	def __init__(self):
		host = setting["MONGODB_HOST"]
		port = setting["MONGODB_PORT"]
		dbname = setting["MONGODB_DBNAME"]
		sheetname = setting["MONGODB_SHEETNAME"]

		#创建数据库连接
		client = pymongo.MongoClient(host = host, port = port)

    def process_item(self, item, spider):
        return item
