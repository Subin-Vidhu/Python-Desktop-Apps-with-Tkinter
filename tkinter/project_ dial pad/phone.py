from tkinter import *

root = Tk()
root.geometry("640x480")
root.title("Tkinter Window Title")

frame = Frame(root, bd=2,relief="sunken")
frame.place(x=30, y=30)

def click(e):
    print(e)

values = ['1','2','3','4','5','6','7','8','9','#','0','*','Q']
index = 0
for y in range(0,4):
    for x in range(0,3):
        bt = Button(frame, text=values[index])
        bt.config(command=lambda index=index:click(values[index]))
        bt.grid(row=y,column=x) 
        index = index + 1



root.mainloop()    