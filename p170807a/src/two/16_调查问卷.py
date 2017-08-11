from tkinter import *
top=Tk()
top.title('test')
label_title1=Label(top,text="心理测试")
n=0
m=0
def answer1():
    global n
    n=var1.get()
    label["text"] = n+m
    print(n+m)

def answer2():
    global m
    m=var2.get()
    label["text"] = n+m
    print(n+m)
buttons1=[('1',1),('2',2),('3',3),('4',4),('5',5)]
var1=IntVar()
var1.set(0)
label=Label(top,bg="red",text="0")
label_title1.pack(anchor=W)
for judge1,score1 in buttons1:
    r1=Radiobutton(top,text=judge1,variable=var1,value=score1,command=answer1)
    r1.pack(anchor=W,padx=20)

buttons2=[('1',1),('2',2),('3',3),('4',4),('5',5)]
label_title2=Label(top,text="心理测试")
var2=IntVar()
var2.set(0)
label_title2.pack(anchor=W)
for judge2,score2 in buttons2:
    r2=Radiobutton(top,text=judge2,variable=var2,value=score2,command=answer2)
    r2.pack(anchor=W,padx=20)
label.pack(anchor=W)

top.mainloop()
