# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime
import csv
import MySQLdb
import MySQLdb.cursors
from scrapy.conf import settings

class CsvPipeline(object):
    def __init__(self):
        now = datetime.utcnow().replace(microsecond=0).isoformat(' ')
        self.csvFile = file(now + '.csv', 'wb')
        self.csvWriter = csv.writer(self.csvFile, delimiter=',')
        self.csvWriter.writerow(['小区', '网页', '标题', '户型', '单价', '总价', '面积', '楼层', '朝向', '装修', '建年', '学校', '区名', '标识', '地铁'])

    def open_spider(self, spider):
        return

    def close_spider(self, spider):
        self.csvFile.close()

    def process_item(self, item, spider):
        self.csvWriter.writerow([item['communityName'], item['url'], item['title'], item['houseType'], str(item['unitPrice']), str(item['totalPrice']), str(item['area']), item['floor'], item['heading'], item['decoration'], str(item['builtYear']), item['schoolNames'], item['district'], item['token'], item['metro']])
        return item

class MySqlPipeline(object):
    def __init__(self, dbCursor, connection):
        self.cursor = dbCursor
        self.conn = connection

    @classmethod
    def from_settings(cls, settings):
        connection = MySQLdb.connect(
            host = settings['MYSQL_HOST'],
            db = settings['MYSQL_DBNAME'],
            user = settings['MYSQL_USER'],
            passwd = settings['MYSQL_PASSWORD'],
            charset = 'utf8',
        )
        dbCursor = connection.cursor()
        return cls(dbCursor, connection)

    def process_item(self, item, spider):
        self._do_insert(item)
        # self._do_insert_or_update(item) 判断是否为同一房源可以使用url字段
        return item

    # 追加插入，数据较全，可以通过视图完善数据格式
    def _do_insert(self, item):
        self.cursor.execute(" \
            insert into house_info(community_name, url, title, house_type, unit_price, total_price, area, floor, heading, decoration, built_year, school_names, district, token, metro) \
            values ('%s', '%s', '%s', '%s', %d, %d, %f, '%s', '%s', '%s', %d, '%s', '%s', '%s', '%s');" % (item['communityName'], item['url'], item['title'], item['houseType'], item['unitPrice'], item['totalPrice'], item['area'], item['floor'], item['heading'], item['decoration'], item['builtYear'], item['schoolNames'], item['district'], item['token'], item['metro']))

    def __del__(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
