from tkinter import *

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.geometry("200x200")
        self.master.title("Title")

        self.btn = Button(self.master, text="Hello", command=self.func, width=20, height=10)
        self.btn.place(x=0,y=0)

        self.frame.pack()

    def func(self):
        print('button click')
        
def main(): 
    root = Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()


