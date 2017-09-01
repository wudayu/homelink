# -*- coding: utf-8 -*-

# Scrapy settings for homelink project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'homelink'

SPIDER_MODULES = ['homelink.spiders']
NEWSPIDER_MODULE = 'homelink.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'homelink (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'homelink.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'homelink.middlewares.RandomUserAgent': 1,
    'homelink.middlewares.ProxyDownloaderMiddleware': 125,
    # 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'homelink.pipelines.CsvPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# USER_AGENTS
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

# IP proxy for testing
IPPOOL=[
  {"ipAddr":"52.80.55.38:3386"},
  {"ipAddr":"142.4.214.9:8"},
  {"ipAddr":"87.120.55.115:5328"},
  {"ipAddr":"141.196.144.222:808"},
  {"ipAddr":"180.210.205.199:888"},
  {"ipAddr":"121.234.37.19:80"},
  {"ipAddr":"170.84.93.130:6530"},
  {"ipAddr":"123.96.240.243:811"},
  {"ipAddr":"163.172.178.93:312"},
  {"ipAddr":"195.136.6.147:5328"},
  {"ipAddr":"41.76.150.154:6530"},
  {"ipAddr":"183.152.148.74:80"},
  {"ipAddr":"46.101.108.112:8"},
  {"ipAddr":"138.59.176.244:808"},
  {"ipAddr":"89.249.245.223:5328"},
  {"ipAddr":"75.102.38.13:312"},
  {"ipAddr":"202.129.207.182:5328"},
  {"ipAddr":"36.111.38.9:1702"},
  {"ipAddr":"163.172.156.142:312"},
  {"ipAddr":"112.86.163.64:888"},
  {"ipAddr":"177.91.79.25:5328"},
  {"ipAddr":"128.199.75.57:44"},
  {"ipAddr":"197.156.128.34:6530"},
  {"ipAddr":"187.71.184.221:808"},
  {"ipAddr":"200.111.121.21:808"},
  {"ipAddr":"118.242.0.109:890"},
  {"ipAddr":"83.11.20.235:808"},
  {"ipAddr":"103.25.64.124:8"},
  {"ipAddr":"182.93.169.250:808"},
  {"ipAddr":"62.205.245.173:5328"},
  {"ipAddr":"91.205.238.14:312"},
  {"ipAddr":"31.44.249.132:808"},
  {"ipAddr":"95.79.26.9:808"},
  {"ipAddr":"101.4.136.34:8"},
  {"ipAddr":"111.13.7.42:84"},
  {"ipAddr":"185.17.132.66:5328"},
  {"ipAddr":"82.130.196.153:6530"},
  {"ipAddr":"117.33.176.198:8"},
  {"ipAddr":"94.21.32.223:5328"},
  {"ipAddr":"141.105.53.157:808"},
  {"ipAddr":"14.139.229.45:808"},
  {"ipAddr":"202.79.27.50:808"},
  {"ipAddr":"202.162.217.6:808"},
  {"ipAddr":"77.120.246.66:5328"},
  {"ipAddr":"63.142.242.57:8"},
  {"ipAddr":"139.255.97.10:6530"},
  {"ipAddr":"178.245.241.187:808"},
  {"ipAddr":"61.160.208.222:808"},
  {"ipAddr":"190.121.29.235:6530"},
  {"ipAddr":"37.143.96.236:808"},
  {"ipAddr":"103.195.26.59:6530"},
  {"ipAddr":"83.71.175.121:808"},
  {"ipAddr":"110.73.8.118:812"},
  {"ipAddr":"103.15.83.129:6530"},
  {"ipAddr":"46.44.52.61:808"},
  {"ipAddr":"165.16.3.82:5328"},
  {"ipAddr":"189.113.81.62:5328"},
  {"ipAddr":"207.226.141.117:3386"},
  {"ipAddr":"61.42.18.132:5328"},
  {"ipAddr":"207.226.141.176:3386"},
  {"ipAddr":"118.144.148.140:312"},
  {"ipAddr":"222.243.213.117:5328"},
  {"ipAddr":"177.128.158.61:6530"},
  {"ipAddr":"183.89.21.199:808"},
  {"ipAddr":"187.49.83.18:600"},
  {"ipAddr":"84.0.236.166:5328"},
  {"ipAddr":"70.162.84.164:3640"},
  {"ipAddr":"60.24.159.63:811"},
  {"ipAddr":"187.160.245.156:312"},
  {"ipAddr":"60.178.139.82:808"},
  {"ipAddr":"120.199.64.163:808"},
  {"ipAddr":"186.46.192.242:5328"},
  {"ipAddr":"113.128.91.94:4888"},
  {"ipAddr":"152.251.220.64:808"},
  {"ipAddr":"190.202.185.4:808"},
  {"ipAddr":"203.74.4.1:8"},
  {"ipAddr":"2.93.3.111:808"},
  {"ipAddr":"177.71.17.70:808"},
  {"ipAddr":"185.112.148.142:808"},
  {"ipAddr":"185.5.18.169:312"},
  {"ipAddr":"198.71.161.163:8"},
  {"ipAddr":"110.77.215.175:6530"},
  {"ipAddr":"54.222.222.79:3386"},
  {"ipAddr":"121.232.147.125:900"},
  {"ipAddr":"141.196.64.38:808"},
  {"ipAddr":"203.192.229.153:808"},
  {"ipAddr":"200.255.122.170:808"},
  {"ipAddr":"85.133.177.177:808"},
  {"ipAddr":"95.143.139.149:6530"},
  {"ipAddr":"202.115.73.202:808"},
  {"ipAddr":"131.221.217.136:312"},
  {"ipAddr":"212.231.65.8:5328"},
  {"ipAddr":"43.252.159.124:6390"},
  {"ipAddr":"66.82.221.49:8"},
  {"ipAddr":"96.9.90.90:808"},
  {"ipAddr":"110.170.150.130:808"},
  {"ipAddr":"115.88.6.155:6530"},
  {"ipAddr":"169.239.209.108:5328"},
  {"ipAddr":"187.49.94.1:600"},
  {"ipAddr":"203.207.56.67:80"},
]
