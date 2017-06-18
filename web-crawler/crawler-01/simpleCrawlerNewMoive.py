# -*- coding: utf-8 -*-

import re
import urllib2

class TodayMovie(object):
    def __init__(self):
        self.url = 'http://dianying.2345.com/'
        self.timeout = 5
        self.fileName = './TodayNewMoive.txt'
        self.getMovieInfo()

    def getMovieInfo(self):
        response = urllib2.urlopen(self.url,timeout=self.timeout)
        movieList = re.findall('sTit.*',response.read())
        print movieList
        with open(self.fileName,'w') as fp:
            for movie in movieList:
                movie1 = self.subStr(movie)
                # print movie1.decode('utf8')
                fp.write(movie+'\n')

    def subStr(self,st):
        st = st.replace('film-title">','')
        st = st.replace('</h3>','')
        return st

if __name__ == '__main__':
    tm = TodayMovie()