# LearningScrapy
To start crawling use the command:
  "scrapy crawl link_checker"

Configurations used can be seen in settings.py file

depth0.txt shows log of crawling "https://www,gmail.com" with no depth limit
depth1.txt shows log of crawling "https://www,gmail.com" with depth limit set as 1
depth2.txt shows log of crawling "https://www,gmail.com" with depth limit set as 2

For crawling with a depth limit of 0, Go to link.py and inside "Rule", set the follow to "False" in CrawlSpider

The log.txt contains information like 
{'downloader/request_bytes', 'downloader/request_count', 'downloader/request_method_count/GET', 'downloader/response_bytes', 'downloader/response_count', 'downloader/response_status_count/200', 'finish_reason': 'closespider_timeout', 'finish_time': datetime.datetime(2019, 1, 17, 16, 11, 35, 503575), 'log_count/INFO', 'request_depth_max', 'response_received_count', 'scheduler/dequeued', 'scheduler/dequeued/memory', 'scheduler/enqueued', 'scheduler/enqueued/memory', 'start_time': datetime.datetime(2019, 1, 17, 16, 11, 24, 635897)}

This can be gemerated using the command "scrapy bench"
