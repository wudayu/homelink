import scrapy
from homelink.items import HomelinkItem
import csv

class HlSpider(scrapy.Spider):
    base_url = "http://nj.lianjia.com/ershoufang/y3f2f5sf1l4l5/"
    url_suffix = "/"
    init_url = base_url + url_suffix

    name = "hl"
    allowed_domains = ["nj.lianjia.com"]
    start_urls = [
        init_url
    ]

    csvfile = file('csv_test.csv', 'wb')
    writer = csv.writer(csvfile)

    def parse(self, response):
        page_count_unicode = response.xpath('//div[@class="page-box house-lst-page-box"]//@page-data').extract_first()
        page_count = int(filter(str.isdigit, page_count_unicode[:18].encode('utf-8')))

        for curr_page in range(1, page_count + 1):
            print str(curr_page)
            yield scrapy.Request(response.urljoin(self.base_url + "pg" + str(curr_page) + self.url_suffix), self.parse_list_page)

        #csvfile.close()

    def parse_list_page(self, response):
        links = []
        for link in response.xpath('//div[@class="title"]/a/@href'):
            links.append(link.extract())
        for inner_page_url in links:
            yield scrapy.Request(response.urljoin(inner_page_url), self.parse_inner_page)

    def parse_inner_page(self, response):
        item = HomelinkItem()
        item['communityName'] = response.xpath('//div[@class="communityName"]/a[@class="info"]/text()').extract_first().encode('utf-8')
        item['url'] = response.url
        item['title'] = response.xpath('//h1[@class="main"]/text()').extract_first().encode('utf-8')
        item['houseType'] = response.xpath('//div[@class="room"]/div[@class="mainInfo"]/text()').extract_first().encode('utf-8')
        item['unitPrice'] = int(response.xpath('//span[@class="unitPriceValue"]/text()').extract_first())
        item['totalPrice'] = int(response.xpath('//span[@class="total"]/text()').extract_first())
        item['area'] = float(response.xpath('//div[@class="area"]/div[@class="mainInfo"]/text()').extract_first().encode('utf-8')[:-6])
        item['floor'] = response.xpath('//div[@class="room"]/div[@class="subInfo"]/text()').extract_first().encode('utf-8')
        item['heading'] = response.xpath('//div[@class="type"]/div[@class="mainInfo"]/text()').extract_first().encode('utf-8')
        item['decoration'] = response.xpath('//div[@class="type"]/div[@class="subInfo"]/text()').extract_first().encode('utf-8')
        item['builtYear'] = int(filter(str.isalnum, response.xpath('//div[@class="area"]/div[@class="subInfo"]/text()').extract_first().encode('utf-8')))
        item['schoolNames'] = response.xpath('//div[@class="schoolName"]/span[@class="info"]/a/text()').extract()
        item['district'] = response.xpath('//div[@class="areaName"]/span[@class="info"]/a/text()').extract()[0].encode('utf-8')
        item['token'] = response.xpath('//div[@class="areaName"]/span[@class="info"]/a/text()').extract()[1].encode('utf-8')
        item['metro'] = response.xpath('//div[@class="areaName"]/a/text()').extract_first(default='N/A').encode('utf-8')

        '''
        print "CommunityName : " + item['communityName']
        print "Url : " + item['url']
        print "Title : " + item['title']
        print "HouseType : " + item['houseType']
        print "UnitPrice : " + str(item['unitPrice'])
        print "TotalPrice : " + str(item['totalPrice']) + "w"
        print "Area : " + str(item['area']) + "m2"
        print "Floor : " + item['floor']
        print "Heading : " + item['heading']
        print "Decoration : " + item['decoration']
        print "BuiltYear : " + str(item['builtYear'])
        for schoolName in item['schoolNames']:
            print "School : " + schoolName
        print "District : " + item['district']
        print "Token : " + item['token']
        if item['metro']:
            print "Metro : " + item['metro']

        print '\n'
        '''
        schoolNames = ""
        for schoolName in item['schoolNames']:
            schoolNames = schoolNames + schoolName.encode('utf-8') + ' '

        self.writer.writerow([item['communityName'], item['url'], item['title'], item['houseType'], str(item['unitPrice']), str(item['totalPrice']), str(item['area']), item['floor'], item['heading'], item['decoration'], str(item['builtYear']), schoolNames, item['district'], item['token'], item['metro']])
