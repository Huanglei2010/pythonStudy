# encoding: UTF-8
import threading
import time

event = threading.Event()


def func():
    # 等待事件，进入等待阻塞状态
    print ('%s wait for event...' % threading.currentThread().getName(),time.ctime())
    event.wait() #wait([timeout]): 如果标志为True将立即返回，否则阻塞线程至等待阻塞状态，等待其他线程调用set()。

    # 收到事件后进入运行状态
    print ('%s recv event.' % threading.currentThread().getName(),time.ctime())


t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t1.start()
t2.start()

time.sleep(2)

# 发送事件通知
print ('MainThread set event.')
event.set()  #　set(): 将标志设为True，并通知所有处于等待阻塞状态的线程恢复运行状态。 

'''http://www.cnblogs.com/tkqasn/p/5700281.html'''