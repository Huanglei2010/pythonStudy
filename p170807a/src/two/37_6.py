#coding:utf-8
import threading
import time

def action(arg):
    time.sleep(1)
    print  ('sub thread start!the thread name is:%s    ' % threading.currentThread().getName())
    print ('the arg is:%s   ' %arg)
    time.sleep(1)

thread_list = []    #线程存放列表
for i in range(4):
    t =threading.Thread(target=action,args=(i,))
    t.setDaemon(True)
    thread_list.append(t)

for t in thread_list:
    t.start()

for t in thread_list:
    t.join()

'''http://www.cnblogs.com/tkqasn/p/5700281.html'''