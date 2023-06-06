#!/usr/bin/python3

import tkinter
from tkinter import *

def func():
    print(wb.get())

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Title World")
    root.geometry("300x300")

    wb = Spinbox(root, from_=0, to=100)
    wb.place(x=30, y=100)

    bt = Button(root, text="click", command=func)
    bt.place(x=30, y=120)

    root.mainloop()
