#coding:utf-8
import threading
import time
from time import ctime

gl_num = 0

def show(arg):
    global gl_num #使之为全局变量
    time.sleep(1)
    gl_num +=1
    print (gl_num,ctime())

for i in range(10):
    t = threading.Thread(target=show, args=(i,))
    t.start()

print ('main thread stop')