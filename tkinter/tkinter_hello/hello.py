#!/usr/bin/python3

import tkinter

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Hello World")
    root.geometry("500x400")

    # add label
    label = tkinter.Label(root, text="hello \n Good Day")
    label.pack(expand=tkinter.TRUE)
    
    root.mainloop()
