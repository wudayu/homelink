# -*- coding: utf-8 -*-
import random
from homelink.settings import IPPOOL

class ProxyDownloaderMiddleware(object):
    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        thisIp = random.choice(IPPOOL)
        print("==== ====== ==this is ip:" + thisIp["ipAddr"])
        request.meta["proxy"] = "http://" + thisIp["ipAddr"]
