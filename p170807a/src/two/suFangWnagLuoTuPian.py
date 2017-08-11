# -*- coding:utf-8 -*-
''''' tk_image_view_url_io_resize.py
display an image from a URL using Tkinter, PIL and data_stream
also resize the web image to fit a certain size display widget
retaining its aspect ratio
Pil facilitates resizing and allows file formats other then gif
tested with Python27 and Python33 by vegaseat 18mar2013
'''
''''' tk_image_view_url_io_resize.py 
用Tkinter, PIL和data_stream从一个url地址加载图片， 
能保持比例缩放适应显示大小， Pil便于缩放和读取各种图像格式， 
在Python27和Python33上都测试过了 by vegaseat 18mar2013 
'''

import io
from PIL import Image, ImageTk

try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen


def resize(w, h, w_box, h_box, pil_image):
    '''''
    resize a pil_image object so it will fit into
    a box of size w_box times h_box, but retain aspect ratio
    对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例
    '''

    f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
    f2 = 1.0 * h_box / h
    factor = min([f1, f2])
    # print(f1, f2, factor) # test
    # use best down-sizing filter
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)


root = tk.Tk()
# size of image display box you want
# 期望图像显示的大小
w_box = 400
h_box = 400
# find yourself a picture on an internet web page you like
# (right click on the picture, under properties copy the address)
# a larger (1600 x 1200) picture from the internet
# url name is long, so split it
# 从网页上找到一个图片，复制它的网址，这里网址太长，所以分开了
url1 = "http://freeflowerpictures.net/image/flowers/petunia/"
url2 = "petunia-flower.jpg"
url = url1 + url2
image_bytes = urlopen(url).read()
# internal data file
data_stream = io.BytesIO(image_bytes)

# open as a PIL image object
# 以一个PIL图像对象打开
pil_image = Image.open(data_stream)

# get the size of the image
# 获取图像的原始大小
w, h = pil_image.size

# resize the image so it retains its aspect ration
# but fits into the specified display box
# 缩放图像让它保持比例，同时限制在一个矩形框范围内
pil_image_resized = resize(w, h, w_box, h_box, pil_image)

# optionally show resized image info ...
# get the size of the resized image
# 也可以显示缩放后的图像信息，获取大小
wr, hr = pil_image_resized.size

# split off image file name
# 标题栏显示：缩放后的图像文件名和大小
fname = url.split('/')[-1]
sf = "resized {} ({}x{})".format(fname, wr, hr)
root.title(sf)

# convert PIL image object to Tkinter PhotoImage object
# 把PIL图像对象转变为Tkinter的PhotoImage对象
tk_image = ImageTk.PhotoImage(pil_image_resized)

# put the image on a widget the size of the specified display box
# Label: 这个小工具，就是个显示框，小窗口，把图像大小显示到指定的显示框
label = tk.Label(root, image=tk_image, width=w_box, height=h_box)
# padx,pady是图像与窗口边缘的距离
label.pack(padx=5, pady=5)
root.mainloop()


#http://blog.csdn.net/wuzuyu365/article/details/52488009