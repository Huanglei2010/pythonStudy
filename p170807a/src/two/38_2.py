#encoding: utf-8
import codecs
data=codecs.open('f.txt','r+','utf-8')
s=data.readlines()
data.close()
for line in s:
    print(line)