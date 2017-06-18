#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import sys
import re


def test_argument():
    if len(sys.argv) != 2:
        print "只需要一个参数就够了。。。"
        tipUse()
        exit()
    else:
        TP = TestProxy(sys.argv[1])

def tipUse():
    """显示提示信息"""
    print u'该程序只有一个参数可以输入，参数为可用的proxy'
    print u'use python urllibWithProxy.py http://1.2.3.4:5'
    print u'use python urllibWithProxy.py https://1.2.3.4:5'

class TestProxy(object):

    def __init__(self,proxy):
        self.proxy = proxy
        self.url = 'http://www.google.com'
        self.timeout = 5
        self.flagword = 'google'
        self.check_proxy_format(proxy)
        self.use_proxy(self.proxy)
    def check_proxy_format(self, proxy):
        try:
            proxy_match = re.compile('http[s]?://[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}:[\d]{1,5}$')
            re.search(proxy_match, proxy).group()
        except AttributeError:
            tipUse()
            exit()
        flag = 1
        proxy = proxy.replace('//', '')
        try:
            protocol = proxy.split(':')[0]
            ip = proxy.split(':')[1]
            port = proxy.split(':')[2]
        except IndexError:
            print u"下标越界"
            tipUse()
            exit()

        flag = flag and len(proxy.split(':')) == 3 and len(ip.split('.')) == 4
        flag = ip.split('.')[0] in map(str,xrange(1, 256)) and flag
        flag = ip.split('.')[1] in map(str,xrange(256)) and flag
        flag = ip.split('.')[2] in map(str,xrange(256)) and flag
        flag = ip.split('.')[3] in map(str,xrange(1, 255)) and flag
        if flag:
            print "输入的代理服务器格式符合标准"
        else:
            tipUse()
            exit()

    def use_proxy(self,proxy):
        """利用代理访问百度，并查找关键词"""
        protocol = proxy.split('//')[0].replace(':', '')
        ip = proxy.split('//')[1]
        print protocol
        print ip
        opener = urllib2.build_opener(urllib2.ProxyHandler({protocol: ip}))
        urllib2.install_opener(opener)
        try:
            resonpse_ab = urllib2.urlopen(self.url, timeout=self.timeout)
        except:
            print "连接错误，退出程序"
            exit()

        str1 = resonpse_ab.read()
        if re.search(self.flagword, str1):
            print '已经取得特征词，代理可用'
        else:
            print '代理不可用'

if __name__ == '__main__':
    test_argument()

