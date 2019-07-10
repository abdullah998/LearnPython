import scrapy
import time
from scrapy.crawler import CrawlerRunner
from scrapy.selector import Selector
from scrapy.utils.log import configure_logging
from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess
from multiprocessing import Process, Queue


class job_spider(scrapy.Spider):
    name = "jobs"

    def start_requests(self):
        urls = [
            'https://news.ycombinator.com/jobs',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        links = Selector(text=response.body).xpath('//tr[@class="athing"]/td/a/@href').getall()
        jobs = Selector(text=response.body).xpath('//tr[@class="athing"]/td/a/text()').getall()
        for index in range(0, len(links)):
            print(links[index], end='\t')
            print(jobs[index])


def print_jobs():
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    runner = CrawlerRunner()
    d = runner.crawl(job_spider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()  # the script will block here until the crawling is finished


def run_spider(spider):
    def cmd_script(q):
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        process.crawl(spider)
        process.start()  # the script will block here until the crawling is finished
        time.sleep(10)
        q.put(None)
    q = Queue()
    proc = Process(target=cmd_script, args=(q,))
    proc.start()
    result = q.get()
    proc.join()


while True:
    run_spider(job_spider)
    time.sleep(3600)