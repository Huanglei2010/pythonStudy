#一个小列表占满父容器
from tkinter import *
root = Tk()
listbox = Listbox(root)
listbox.pack(fill=BOTH,expand=1)
for i in range(20):
    listbox.insert(END, str(i))
mainloop()

# 作者：__雪夜__
# 链接：http://www.jianshu.com/p/5c7a1af4aa53
# 來源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。