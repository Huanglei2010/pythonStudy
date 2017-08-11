#!/usr/bin/env python3
# coding=utf-8

from tkinter import *
from tkinter import ttk

__author__ = 'Administrator'

root = Tk()
frame = ttk.Frame(root, padding=10, relief="solid", borderwidth=2)
frame.grid(padx=10, pady=10)
label_1 = ttk.Label(frame, relief="solid", borderwidth=1, justify="left")
label_2 = ttk.Label(frame, relief="solid", borderwidth=1, justify="center")
label_3 = ttk.Label(frame, relief="solid", borderwidth=1, justify="right")
label_4 = ttk.Label(frame, relief="solid", borderwidth=1, wraplength="100")
label_5 = ttk.Label(frame, relief="solid", borderwidth=1)

label_1["text"] = "这是多行\n文字\n这是另一行"
label_2["text"] = "这是多行\n文字\n这是另一行"
label_3["text"] = "这是多行\n文字\n这是另一行"
label_4["text"] = "这是一行长文字，根据长度自动换行这是一行长文字，根据长度自动换行"

label_5["text"] = "PYTHON"
image = PhotoImage(file="python.gif")
label_5["image"] = image
label_5["compound"] = "left"

label_1.grid(row=0, column=0)
label_2.grid(row=0, column=1)
label_3.grid(row=0, column=2)
label_4.grid(row=1, column=0, columnspan=3)
label_5.grid(row=2, column=0, columnspan=3)

for child in frame.winfo_children():
    child.grid(padx=3, pady=3)

root.mainloop()