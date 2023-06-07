from tkinter import *

root = Tk()
root.geometry("640x480")
root.title("Tkinter Window Title")

frame = Frame(root, bd=2,relief="sunken")
frame.place(x=30, y=30)

bt = Button(frame, text='Button')
bt.pack() 

bt2 = Button(frame, text='Button')
bt2.pack() 

bt3 = Button(frame, text='Button')
bt3.pack() 

root.mainloop()    