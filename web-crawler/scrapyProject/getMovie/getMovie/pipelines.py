# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time

class GetmoviePipeline(object):
    def process_item(self, item, spider):
        now = time.strftime('%Y-%m-%d', time.localtime())
        fileName = 'Movie' + now + '.txt'
        with open(fileName, 'a') as f:
            f.write(item['movieName'][0].encode('utf8') + '\n\n')
        return item
