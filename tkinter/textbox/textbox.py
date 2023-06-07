from tkinter import *

root = Tk()

T = Text(root, height=20, width=60)
S = Scrollbar(root)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
T.pack()

root.mainloop()