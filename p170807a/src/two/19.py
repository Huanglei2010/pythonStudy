'''3.创建两个不同的组'''
from tkinter import *
root = Tk()
vLang = IntVar()
vOS = IntVar()
vLang.set(1)
vOS.set(2)

for v in [vLang,vOS]:    #创建两个组
    for i in range(3):    #每个组含有3个按钮
        Radiobutton(root,
                    variable = v,
                    value = i,
                    text = 'python' + str(i)
                    ).pack()
root.mainloop()
#不同的组，各个按钮互不影响。