# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class CsvPipeline(object):
    def __init__(self):
        self.csvFile = file('csv_test.csv', 'wb')
        self.csvWriter = csv.writer(self.csvFile, delimiter=',')
        self.csvWriter.writerow(['小区', '网页', '标题', '户型', '单价', '总价', '面积', '楼层', '朝向', '装修', '建年', '学校', '区名', '标识', '地铁'])

    def open_spider(self, spider):
        return

    def close_spider(self, spider):
        self.csvFile.close()

    def process_item(self, item, spider):
        self.csvWriter.writerow([item['communityName'], item['url'], item['title'], item['houseType'], str(item['unitPrice']), str(item['totalPrice']), str(item['area']), item['floor'], item['heading'], item['decoration'], str(item['builtYear']), item['schoolNames'], item['district'], item['token'], item['metro']])
        return item
