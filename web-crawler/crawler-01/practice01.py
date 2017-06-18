
import urllib2

proxy_info = { 'host' : '127.0.0.1',
               'port' : 1087
             }

print "http://%(host)s:%(port)d" % proxy_info
# We create a handler for the proxy
proxy_support = urllib2.ProxyHandler({"http": "http://%(host)s:%(port)d" % proxy_info})

# We create an opener which uses this handler:
opener = urllib2.build_opener(proxy_support)

# Then we install this opener as the default opener for urllib2:
urllib2.install_opener(opener)

# Now we can send our HTTP request:
htmlpage = urllib2.urlopen("http://www.baidu.com",timeout=10).read(200)

print htmlpage

