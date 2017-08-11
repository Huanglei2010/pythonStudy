# -*- coding:utf-8 -*-
'''4.如果同一个组中的按钮使用相同的alue，则这两个按钮的工作方式完全相同'''
# -*- coding: cp936 -*-
from tkinter import *
root = Tk()
v = IntVar()
v.set(1)
for i in range(3):
    Radiobutton(root,
                variable = v,
                value = 1,
                text = 'python' + str(i)
                ).pack()
for i in range(3):
    Radiobutton(root,
                    variable = v,
                    value = i,
                    text = 'python' + str(2 + i)
                    ).pack()
root.mainloop()
#上述的例子中共有4个alue为1的值，当选中其中的一个时，其他三个也会被选中；选中除了这四个只外的按钮时，四个按钮全部取消