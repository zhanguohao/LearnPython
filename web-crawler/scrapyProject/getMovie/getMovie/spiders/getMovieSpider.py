# -*- coding: utf-8 -*-

import scrapy


from getMovie.items import GetmovieItem

class GetmoviespiderSpider(scrapy.Spider):
    name = "getMovieSpider"
    allowed_domains = ["theater.mtime.com"]
    start_urls = ['http://theater.mtime.com/China_Beijing/']

    def parse(self, response):
        subSelector = response.xpath('//li[@class="clearfix"]')
        items = []
        for sub in subSelector:
            item = GetmovieItem()
            item['movieName'] = sub.xpath('./a/@title').extract()
            items.append(item)
        return items
