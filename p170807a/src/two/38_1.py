#encoding: UTF-8
print("黄雷")
f=open('f.txt','ab')
for i in range(10):
    s=str(i)+"黄雷必胜"+'\n'
    f.write(s.encode('utf-8'))
f.close()


