from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack(fill=BOTH, expand=TRUE)

l1 = Label(frame, text="Tkinter Label1", bg="red", fg="white")
l1.pack(side=TOP, padx=10, pady=10)

l2 = Label(frame, text="Tkinter Label2", bg="yellow", fg="black")
l2.pack(side=LEFT, padx=10, pady=10)

l3 = Label(frame, text="Tkinter Label3", bg="blue", fg="white")
l3.pack(side=LEFT, padx=10, pady=10)

mainloop()
