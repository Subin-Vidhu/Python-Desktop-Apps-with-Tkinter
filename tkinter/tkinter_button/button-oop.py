from tkinter import *

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.geometry("200x200")
        self.master.title("Title")

        self.btn = Button(self.master, text="Hello", command=self.func, width=10, height=5)
        self.btn.place(x=0,y=0)

        self.btn = Button(self.master, text="Quit", command=self.quit, width=10, height=5)
        self.btn.place(x=0,y=100)

        self.frame.pack()

    def func(self):
        print('button click')
    
    def quit(self):
        print('quit')
        self.master.destroy()

        
def main(): 
    root = Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()


