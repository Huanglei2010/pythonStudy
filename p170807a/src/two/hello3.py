from tkinter import *
def cal(text,tex2):
    tex2.delete(0,END)
    tex2.insert(END,str(text.get()))

root = Tk()
frame = Frame(height=200, width=500)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)
text = Entry(root, background = 'red')
text.pack()
text2 = Entry(root, background = 'green')
text2.pack()
calBut = Button(text="计算",command=lambda:cal(text,text2))
calBut.pack()
root.mainloop()