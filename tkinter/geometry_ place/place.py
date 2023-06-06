from tkinter import *

root = Tk()
root.geometry("320x200")

l1 = Label(root, text="Tkinter Label", bg="red", fg="white")
l1.place(x = 0, y = 0)
l2 = Label(root, text="Tkinter Label", bg="yellow", fg="black")
l2.place(x = 0, y = 60)
l3 = Label(root, text="Tkinter Label", bg="blue", fg="white")
l3.place(x = 200, y = 60)

mainloop()
