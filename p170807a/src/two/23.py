# _*_ coding:utf-8 _*_
from tkinter import *

root = Tk()
Label(root, text='用户名:').grid(row=0, sticky=W)
Entry(root).grid(row=0, column=1, sticky=E)

Label(root, text='密码：').grid(row=1, sticky=W)
Entry(root).grid(row=1, column=1, sticky=E)  # 输入框

Button(root, text='登陆').grid(row=2, column=1, sticky=E)

root.mainloop()