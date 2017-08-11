#encoding: UTF-8
import urllib
import urllib.request as urllib2
res=urllib2.urlopen("http://baidu.com")
print(res.read())
