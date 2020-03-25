# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['baidu.com']
    start_urls = [
        'https://www.zeaho.com/'
    ]

    def parse(self, response):
        print(response.xpath(
            '//li[@class="dropdown"]/a/text()').get(default='not-found'))
