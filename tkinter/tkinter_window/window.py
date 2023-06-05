#!/usr/bin/python3

# To use tkinter, load it with import tkinter.  This works for Python 3 only.
import tkinter

# Then initialize the window with  root = tkinter.Tk().  You can set the title with  the function .title(name) and the size with .geometry().
# Make Tkinter run with .mainloop().
if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Title World")
    root.geometry("300x300")
    root.mainloop()
