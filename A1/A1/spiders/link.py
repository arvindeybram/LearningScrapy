import time
import logging
import scrapy
from scrapy.utils.log import configure_logging

from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field
timeout = time.time()
import os
import psutil
process = psutil.Process(os.getpid())
#logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(levelname)s:%(message)s:%(asctime)s:')
class MySpider(CrawlSpider):
    start_urls = ['https://www.gmail.com']
    name = 'link_checker'
	
    configure_logging(install_root_handler=True)
    logging.basicConfig(
        filename='log.txt',
        format='%(levelname)s: %(message)s',
        level=logging.INFO
    )
    custom_settings = {
        'DEPTH_LIMIT': '2'}
    rules = (Rule(LinkExtractor(), callback='parse_url', follow=True), )
    def parse_url(self, response):
        logging.info("\n")
        logging.info(os.system('time.time()'))
        logging.info(response.url)
        #logging.info('\n\n\n')
        #logging.debug(response.body)
        #logging.info('\n\n\n')
        #logging.debug(process.memory_info().rss)
        #logging.info('\n\n\n')