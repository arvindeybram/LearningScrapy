import time
import logging
import scrapy
from scrapy.utils.log import configure_logging
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field
import os
import psutil
import datetime
now = datetime.datetime.now()
#logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(levelname)s:%(message)s:%(asctime)s:')
logging.basicConfig(filename='logfiles.txt',format='%(levelname)s: %(message)s',level=logging.INFO)
class MySpider(CrawlSpider):
    start_urls = ['https://www.gmail.com']
    name = 'link_checker'
    configure_logging(install_root_handler=True)
    custom_settings = {
        'DEPTH_LIMIT': '1'}
    rules = (Rule(LinkExtractor(), callback='parse_url', follow=True), )
    def parse_url(self, response):
        logging.info("\n")
        logging.info("The Response URL is: {}".format(response.url))
        logging.info("The Time of Parsing is: {}".format(now.strftime("%Y-%m-%d %H:%M")))
        #logging.info('\n\n\n')
        logging.info("Source Code is: \n {}".format(response.body))
        #logging.info('\n\n\n')
        #logging.info(process.memory_info().rss)
        #logging.info('\n\n\n')