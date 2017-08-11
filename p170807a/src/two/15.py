from tkinter import *

class ChangeLabelDemo:
    def __init__(self):

        window = Tk()
        window.title = "改变labeldemo"

        frame1= Frame(window)
        frame1.pack()
        self.lb1 = Label(frame1, text = "Programming is fun")
        self.lb1.pack()

        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text = "输入")
        self.msg = StringVar()
        entry = Entry(frame2, textvariable = self.msg)
        btChangeText = Button(frame2, text = "改变text", command = self.processButton)
        self.v1 = StringVar()
        rbRed = Radiobutton(frame2,text = "Red", bg="red",variable=self.v1,value="R",command = self.processRadiobutton)
        rbYellow = Radiobutton(frame2, text="Yellow", bg="yellow", variable=self.v1, value="Y", command=self.processRadiobutton)

        label.grid(row = 1, column = 1)
        entry.grid(row = 1, column = 2)
        btChangeText.grid(row = 1, column = 3)
        rbRed.grid(row = 1, column = 4)
        rbYellow.grid(row = 1, column = 5)

        window.mainloop()

    def processButton(self):
        self.lb1["text"] = self.msg.get()
    def processRadiobutton(self):
        if self.v1.get() == "R":
            self.lb1["fg"] = "red"
        elif self.v1.get() == "Y":
            self.lb1["fg"] = "yellow"
ChangeLabelDemo()

# 作者：__雪夜__
# 链接：http://www.jianshu.com/p/5c7a1af4aa53
# 來源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。