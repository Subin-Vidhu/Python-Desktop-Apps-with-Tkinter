from tkinter import *

root = Tk()
root.geometry("320x200")

status = Label(root, text="This is the status bar", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()