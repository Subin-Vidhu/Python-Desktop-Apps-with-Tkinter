from tkinter import *
from tkinter import filedialog

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.geometry("200x200")
        self.master.title("notepad")
        self.textbox(self.master)
        self.addmenu(self.master)
        self.frame.pack()

    def newFile(self):
        self.T.delete('1.0', END)

    def openFile(self):
        self.T.delete('1.0', END)

        fileName = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])    
        print(fileName)

        fobj = open(fileName, "r")
        data = fobj.readlines()
        fobj.close()
        
        self.T.insert(END, data)

    def saveFile(self):
        fileName = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")])
        data = self.T.get(1.0, "end-1c")  
        print(fileName)

        fobj = open(fileName, "w")
        fobj.write(data)
        fobj.close()

    def addmenu(self, root):
        menubar = Menu(root)
        fileMenu = Menu(menubar, tearoff = 0)
        fileMenu.add_command(label="New", command=self.newFile)
        fileMenu.add_command(label = "Open", command=self.openFile)
        fileMenu.add_command(label = "Save", command=self.saveFile)
        fileMenu.add_separator()
        fileMenu.add_command(label = "Exit", command = root.quit)
        menubar.add_cascade(label = "File", menu = fileMenu)
        root.config(menu = menubar)

    def textbox(self, root):
        self.T = Text(root, height=20, width=60)
        self.S = Scrollbar(root)
        self.S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        self.S.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.S.set)
        self.T.pack()


def main(): 
    root = Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()


