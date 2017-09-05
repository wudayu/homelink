import scrapy
from homelink.items import HomelinkItem

class HlSpider(scrapy.Spider):
    url_suffix = "/"

    handle_httpstatus_list = [302]
    name = "hl"
    allowed_domains = ["nj.lianjia.com"]
    start_urls = [
        "https://nj.lianjia.com/ershoufang/gulou/l1l2/",
        "https://nj.lianjia.com/ershoufang/gulou/l3l4l5/",
        "https://nj.lianjia.com/ershoufang/jianye//",
        "https://nj.lianjia.com/ershoufang/qinhuai//",
        "https://nj.lianjia.com/ershoufang/xuanwu//",
        "https://nj.lianjia.com/ershoufang/yuhuatai//",
        "https://nj.lianjia.com/ershoufang/qixia//",
        "https://nj.lianjia.com/ershoufang/jiangning/l1l2/",
        "https://nj.lianjia.com/ershoufang/jiangning/l3/",
        "https://nj.lianjia.com/ershoufang/jiangning/l4l5/",
        "https://nj.lianjia.com/ershoufang/pukou/l1l2/",
        "https://nj.lianjia.com/ershoufang/pukou/l3l4l5/"
    ]

    def parse(self, response):
        page_count_unicode = response.xpath('//div[@class="page-box house-lst-page-box"]//@page-data').extract_first()
        page_count = int(filter(str.isdigit, page_count_unicode[:18].encode('utf-8')))

        # respons.url eg.
        # https://nj.lianjia.com/ershoufang/gulou/l3l4l5/ --> ['https:', '', 'nj.lianjia.com', 'ershoufang', 'gulou', 'l3l4l5', '']
        # https://nj.lianjia.com/ershoufang/jiangning/l1l2/ --> ['https:', '', 'nj.lianjia.com', 'ershoufang', 'jiangning', 'l1l2', '']
        # https://nj.lianjia.com/ershoufang/qinhuai// --> ['https:', '', 'nj.lianjia.com', 'ershoufang', 'qinhuai', '', '']
        # https://nj.lianjia.com/ershoufang/jiangning/l3/ --> ['https:', '', 'nj.lianjia.com', 'ershoufang', 'jiangning', 'l3', '']
        # https://nj.lianjia.com/ershoufang/jianye// --> ['https:', '', 'nj.lianjia.com', 'ershoufang', 'jianye', '', '']

        for curr_page in range(0, page_count):
            url_split = response.url.split("/")
            init_url = "%s//%s/%s/%s/pg%d%s/" % (url_split[0], url_split[2], url_split[3], url_split[4], curr_page + 1, url_split[5])
            print init_url

            request = scrapy.Request(response.urljoin(init_url), self.parse_list_page)
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
        # Put 302 status code back to url request list, warning, this could raise infinite circle.
        # To use this, we need the server got some ways to change its ip address dynamically.
        if response.status == 302:
            request = scrapy.Request(response.urljoin(response.url), self.parse, dont_filter=True)
            request.meta['dont_redirect'] = True
            yield request

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
