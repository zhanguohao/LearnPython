# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
# print soup.prettify()

links = soup.find_all('a')
for link in links:
    print link.name,link['href'],link.get_text()

print "获取lacie链接"

href = soup.find('a',id='link2')
print href.name,href['href'],href['id'],href.get_text()

print "正则匹配："
href = soup.find('a',href=re.compile(r'ill'))
print href.name,href['href'],href['id'],href.get_text()

print ""
href = soup.find('a',href=re.compile(r'ill'))
print href.name,href['href'],href['id'],href.get_text()