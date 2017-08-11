from itertools import *
import time
a=count(5,3)
# for i in a:
#     print(i)
#     time.sleep(1)

s=cycle('xyz')
# for i in s:
#     print(i)
#     time.sleep(1)

s2=repeat(3.14)
# for i in s2:
#     print(i)
#     time.sleep(1)
s3=repeat(3,5)
# for i in s3:
#     print(i)
#     time.sleep(1)
s4=starmap(pow,[(1,1),(2,2),(3,3)])
# for i in s4:
#     print(i)
#     time.sleep(1)

s5 = takewhile(lambda x: x < 5, [1,2,3,4,5,6,7])
for i in s5:
    print(i)
s6 = dropwhile(lambda x: x < 5, [1,2,3,4,5,6,7])
for i in s6:
    print(i)

'''http://www.cnblogs.com/ping-y/p/6208539.html'''