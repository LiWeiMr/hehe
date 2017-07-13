# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["item.jd.com/941189.html"]
    start_urls = ['http://item.jd.com/941189.html/']

    def parse(self, response):
        print(response.text)
