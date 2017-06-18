# -*- coding: utf-8 -*-

import urllib2
import useragent

class Urllib2ModifyHeader(object):
    def __init__(self):
        PIUA = useragent.pcUserAgent.get('IE 9.0')
        MUUA = useragent.mobileUserAgent.get('UC standard')
        self.url = 'http://fanyi.youdao.com'
        self.useUserAgent(PIUA,1)
        self.useUserAgent(MUUA,2)

    def useUserAgent(self,userAgent,name):
        request = urllib2.Request(self.url)
        request.add_header(userAgent.split(':')[0],userAgent.split(':')[1])
        response = urllib2.urlopen(request)
        fileName = str(name) + '.html'
        with open(fileName,'a') as fp:
            fp.write('%s\n\n' %userAgent)
            fp.write(response.read())

if __name__ == "__main__":
    umh = Urllib2ModifyHeader()