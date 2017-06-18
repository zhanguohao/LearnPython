#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import time
import platform
import os


def clear():
    print(u"内容较多，显示3秒后翻页.")
    time.sleep (3)
    OS = platform.system ()
    if OS == u'Windows':
        os.system ('cls')
    else:
        os.system ('clear')


def linkbaidu():
    url = 'http://www.baidu.com'
    try:
        response=urllib2.urlopen(url,timeout=3)
    except urllib2.URLError :
        print(u'网络地址错误')
        exit()
    with open('./baidu.txt','w') as f:
        f.write(response.read())
    print u"获取url信息，response.geturl() \n %s " %response.geturl()
    print u"获取返回代码，response.getcode() \n %s " %response.getcode()
    print u"获取返回信息，respponse.getinfo() \n %s " %response.info()

if __name__ == "__main__":
    linkbaidu()

