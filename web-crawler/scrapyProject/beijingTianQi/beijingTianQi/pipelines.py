# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import time
import urllib2


class BeijingtianqiPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d', time.localtime())
        fileName = today + '.txt'
        with open(fileName, 'a') as fp:
            fp.write(item['cityDate'].encode('utf-8') + '\t')
            fp.write(item['week'].encode('utf-8') + '\t')
            imageName = os.path.basename(item['img'])
            fp.write(imageName + '\t')
            if os.path.exists(imageName):
                pass
            else:
                with open(imageName, 'wb') as im:
                    response = urllib2.urlopen(item['img'])
                    im.write(response.read())
            fp.write(item['temperature'].encode('utf-8')+'\t')
            fp.write(item['weather'].encode('utf-8')+'\t')
            fp.write(item['wind'].encode('utf-8')+'\n\n')

        return item
