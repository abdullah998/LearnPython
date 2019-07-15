# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
 
 
class QuotesSpider(Spider):
    name = 'quotes'
    start_urls = ('http://quotes.toscrape.com/login',)
 
    def parse(self, response):
        token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()
        return FormRequest.from_response(response,
                                         formdata={'csrf_token': token,
                                                   'password': 'foobar',
                                                   'username': 'foobar'},
                                         callback=self.scrape_pages)
