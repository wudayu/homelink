import scrapy
from homelink.items import HomelinkItem

class HlSpider(scrapy.Spider):
    base_url = "https://nj.lianjia.com/ershoufang"
    url_suffix = "/"
    init_url = base_url + url_suffix

    name = "hl"
    allowed_domains = ["nj.lianjia.com"]
    start_urls = [
        init_url
    ]

    def parse(self, response):
        page_count_unicode = response.xpath('//div[@class="page-box house-lst-page-box"]//@page-data').extract_first()
        page_count = int(filter(str.isdigit, page_count_unicode[:18].encode('utf-8')))

        for curr_page in range(0, 100):
            print str(curr_page)
            # request = scrapy.Request(response.urljoin(self.init_url + "pg" + str(curr_page + 1) + "rs%e6%96%87%e5%8c%96%e5%90%8d%e5%9b%ad" + self.url_suffix), self.parse_list_page)
            request = scrapy.Request(response.urljoin(self.init_url + "pg" + str(curr_page + 1) + self.url_suffix), self.parse_list_page)
            request.meta['dont_redirect'] = True
            yield request

    def parse_list_page(self, response):
        links = []
        for link in response.xpath('//div[@class="title"]/a/@href'):
            links.append(link.extract())
        for inner_page_url in links:
            request = scrapy.Request(response.urljoin(inner_page_url), self.parse_inner_page)
            request.meta['dont_redirect'] = True
            yield request

    def parse_inner_page(self, response):
        item = HomelinkItem()
        item['communityName'] = response.xpath('//div[@class="communityName"]/a[@class="info "]/text()').extract_first().encode('utf-8')
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
        schoolNames = response.xpath('//div[@class="schoolName"]/span[@class="info"]/a/text()').extract()
        item['district'] = response.xpath('//div[@class="areaName"]/span[@class="info"]/a/text()').extract()[0].encode('utf-8')
        item['token'] = response.xpath('//div[@class="areaName"]/span[@class="info"]/a/text()').extract()[1].encode('utf-8')
        item['metro'] = response.xpath('//div[@class="areaName"]/a/text()').extract_first(default='N/A').encode('utf-8')

        item['schoolNames'] = ''
        for schoolName in schoolNames:
            item['schoolNames'] = item['schoolNames'] + schoolName.encode('utf-8') + ' '

        yield item
