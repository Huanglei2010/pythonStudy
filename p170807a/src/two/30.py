import urllib.request
f = urllib.request.urlopen('http://www.baidu.com/')
firstLine = f.readline()   #读取html页面的第一行
firstLine
print(firstLine)