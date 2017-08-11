'''2.创建一个Radiobutton组，使用绑定变量来设置选中哦的按钮'''
from tkinter import *
root = Tk()
#创建一个Radiobutton组，创建三个Radiobutton，并绑定到整型变量v
#选中value=1的按钮
v = IntVar()
v.set(1)
for i in range(3):
    Radiobutton(root,variable = v,text = 'python',value = i).pack()

root.mainloop()