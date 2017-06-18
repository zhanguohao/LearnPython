# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sqlite3
import time
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class BeijingtianqiPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d', time.localtime())
        cityDate = item['cityDate'].encode('utf-8')
        week = item['week'].encode('utf-8')
        imageName = os.path.basename(item['img'])
        if os.path.exists(imageName):
            pass
        else:
            with open(imageName, 'wb') as im:
                response = urllib2.urlopen(item['img'])
                im.write(response.read())
        temperature = item['temperature'].encode('utf-8')
        weather = item['weather'].encode('utf-8')
        wind = item['wind'].encode('utf-8')

        fileName = today + '.db'
        conn = sqlite3.connect(fileName)
        cursor = conn.cursor()
        #cursor.execute(
        #     'CREATE TABLE weather1 (id INTEGER PRIMARY KEY AUTOINCREMENT, cityDate TEXT, week TEXT,img TEXT,temperature TEXT,weather TEXT,wind TEXT)')
        cursor.execute('INSERT INTO weather1 (cityDate,week,img,temperature,weather,wind) VALUES (%r,%r,%r,%r,%r,%r)' % (cityDate,week,imageName,temperature,weather,wind,))
        cursor.close()
        conn.commit()
        conn.close()

        return item
