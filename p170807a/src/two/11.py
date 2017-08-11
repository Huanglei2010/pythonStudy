from tkinter import *
master = Tk()
Label(master, text="First").grid(row=0)#row表示行
Label(master, text="Second").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)#第0行 第一列
e2.grid(row=1, column=1)
mainloop()

# 作者：__雪夜__
# 链接：http://www.jianshu.com/p/5c7a1af4aa53
# 來源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。