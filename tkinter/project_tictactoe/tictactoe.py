from tkinter import *

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.geometry("200x200")
        self.master.title("Tic Tac Toe")
        self.buttonList = []
        self.currentPlayer = 0

        index = 0
        for y in range(0,3):
            for x in range(0,3):
                bt = Button(self.frame, text=" ", width=5, height=3, command=lambda index=index:self.click(index))
                bt.grid(row=y, column=x,sticky='NSEW')
                index = index + 1
                self.buttonList.append(bt)

        self.frame.pack()

    def click(self, index):
        print('click ' + str(index))

        if self.currentPlayer == 0:
            self.buttonList[index].config(text='X')
            self.currentPlayer = 1
        else:
            self.buttonList[index].config(text='O')
            self.currentPlayer = 0

def main(): 
    root = Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()


