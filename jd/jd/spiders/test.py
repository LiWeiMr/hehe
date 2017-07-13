# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["item.jd.com/1566538462.html"]
    start_urls = 'http://item.jd.com/1566538462.html'

    def start_requests(self):
        dr = webdriver.PhantomJS()
        dr.get(self.start_urls)
        time.sleep(3)
        body = dr.page_source
        print(body)


    def parse(self, response):

        # demo=BeautifulSoup(response.text,'lxml').find('div',class_="tab-main small").find_all('a',href="#none")
        # for i in demo:

        #     print(i.get_text())
        # demo1=BeautifulSoup(response.text,'lxml').find_all('div',class_="comment-item")
        # for i in demo1:
        #     print(i.find('div',class_="user-info").get_text().strip())
        #     #
        #     print(i.find('div', class_="comment-star star5")["class"][1])
        #     print(i.find('a',class_="J-nice").get_text())


