from tkinter import *

root = Tk()

w = Label(root, text="Red", bg="red", fg="white")
w.pack(fill=Y,side=LEFT)
w = Label(root, text="Green", bg="green", fg="black")
w.pack(fill=Y,side=LEFT)
w = Label(root, text="Blue", bg="blue", fg="white")
w.pack(fill=Y,side=LEFT)

mainloop()

# 作者：__雪夜__
# 链接：http://www.jianshu.com/p/5c7a1af4aa53
# 來源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。