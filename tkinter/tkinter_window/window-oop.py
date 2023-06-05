from tkinter import *

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.geometry("200x200")
        self.master.title("Title")
        self.frame.pack()

def main(): 
    root = Tk()
    app = Demo1(root) #object oriented version (OOP)
    root.mainloop()

if __name__ == '__main__':
    main()


