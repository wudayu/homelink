# -*- coding: utf-8 -*-
import random
from homelink.settings import IPPOOL

class RandomUserAgent(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))

class ProxyDownloaderMiddleware(object):
    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        proxyIp = random.choice(IPPOOL)
        print("==== ====== ==this is request ip:" + proxyIp["ipAddr"])
        request.meta["proxy"] = "http://%s" % proxyIp["ipAddr"]

    def process_response(self, request, response, spider):
        if response.status != 200:
            proxyIp = random.choice(IPPOOL)
            print("===== ===== ==this is response ip:" + proxy["ipAddr"])
            request.meta['proxy'] = "http://%s" % proxyIp["ipAddr"]
            return request
        return response
