# -*- coding:utf-8 -*-
'''5.与Checkbutton类似，每个Radiobutton可以有自己的处理函数，每当点击按钮时，系统会调用相应的处理函数'''
# -*- coding: cp936 -*-
from tkinter import *

root = Tk()
v = IntVar()
v.set(0)

# ctrl+r是替换的意思 r表示replace


def r1():
    print('call r1')


def r2():
    print('call r2')


def r3():
    print('call r3')


def r4():
    print('call r4')


i = 0
# 创建8个按钮，其中两个两个的value值相同
for r in [r1, r2, r3, r4]:
    Radiobutton(root,
                variable=v,#variable是组的标志
                text='radio button',
                value=i,
                command=r
                ).pack()
    Radiobutton(root,
                variable=v,
                text='radio button',
                value=i,
                command=r
                ).pack()
    i += 1

root.mainloop()
# 注意虽然同时可以选中两个按钮，但每次点击按钮，执行的代码只有一次