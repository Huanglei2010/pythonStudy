import urllib.request as ulb
import matplotlib.pyplot as plt
import numpy as np
import PIL.ImageFile as ImageFile

#用urllib2库链接网络图像
response=ulb.Request('http://s14.sinaimg.cn/mw690/5562b044tx6BkMgSR09ad&690')
fp=ulb.urlopen(response)        #打开网络图像文件句柄
p = ImageFile.Parser()              #定义图像IO
while 1:                                     #开始图像读取
     s = fp.read(1024)
     if not s:
        break
     p.feed(s)
im = p.close()                           #得到图像
arr=np.array(im)                       #将图像转换成numpy矩阵
print (np.shape(arr))                   #显示矩阵的维数
plt.imshow(im)                         #显示图像

# http://blog.sina.com.cn/s/blog_5562b0440102va9f.html