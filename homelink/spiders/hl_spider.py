import scrapy
from homelink.items import HomelinkItem

class HlSpider(scrapy.Spider):
    name = "hl"
    allowed_domains = ["nj.lianjia.com"]
    start_urls = [
        "http://nj.lianjia.com/ershoufang/y2/"
    ]

    def parse(self, response):
        links = []

        for link in response.xpath('//div[@class="title"]/a/@href'):
            links.append(link.extract())

        for inner_page_url in links:
            yield scrapy.Request(response.urljoin(inner_page_url), self.parse_inner_page)


        # filename = response.url.split("/")[-2] + '.html'
        # f = open(filename, 'wb')
        # for linker in links:
        #     f.write(linker)
        #     f.write('\n')


    def parse_inner_page(self, response):
        item = HomelinkItem()
        item['communityName'] = response.xpath('//div[@class="communityName"]/a[@class="info"]/text()').extract_first()
        item['url'] = response.url
        item['title'] = response.xpath('//h1[@class="main"]/text()').extract_first()
        item['houseType'] = response.xpath('//div[@class="room"]/div[@class="mainInfo"]/text()').extract_first()
        item['unitPrice'] = int(response.xpath('//span[@class="unitPriceValue"]/text()').extract_first())
        item['totalPrice'] = int(response.xpath('//span[@class="total"]/text()').extract_first())
        item['area'] = float(response.xpath('//div[@class="area"]/div[@class="mainInfo"]/text()').extract_first().encode('utf-8')[:-6])
        item['floor'] = response.xpath('//div[@class="room"]/div[@class="subInfo"]/text()').extract_first()
        item['heading'] = response.xpath('//div[@class="type"]/div[@class="mainInfo"]/text()').extract_first()
        item['decoration'] = response.xpath('//div[@class="type"]/div[@class="subInfo"]/text()').extract_first()
        item['builtYear'] = int(filter(str.isalnum, response.xpath('//div[@class="area"]/div[@class="subInfo"]/text()').extract_first().encode('utf-8')))
        item['schoolNames'] = response.xpath('//div[@class="schoolName"]/span[@class="info"]/a/text()').extract()
        item['district'] = response.xpath('//div[@class="areaName"]/span[@class="info"]/a/text()').extract()[0]
        item['token'] = response.xpath('//div[@class="areaName"]/span[@class="info"]/a/text()').extract()[1]
        item['metro'] = response.xpath('//div[@class="areaName"]/a/text()').extract_first()

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