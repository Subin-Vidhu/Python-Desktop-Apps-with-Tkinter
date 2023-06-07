from tkinter import *

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.geometry("200x200")
        self.master.title("Tic Tac Toe")
        self.buttonList = []
        self.currentPlayer = 0
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.game_over = False

        index = 0
        for y in range(0, 3):
            for x in range(0, 3):
                bt = Button(self.frame, text=" ", width=5, height=3, command=lambda index=index: self.click(index))
                bt.grid(row=y, column=x, sticky='NSEW')
                index = index + 1
                self.buttonList.append(bt)

        self.frame.pack()

    def click(self, index):
        if not self.game_over and self.board[index // 3][index % 3] == ' ':
            if self.currentPlayer == 0:
                self.buttonList[index].config(text='X')
                self.board[index // 3][index % 3] = 'X'
                self.currentPlayer = 1
            else:
                self.buttonList[index].config(text='O')
                self.board[index // 3][index % 3] = 'O'
                self.currentPlayer = 0

            if self.check_win('X'):
                print('Player X wins!')
                self.game_over = True
            elif self.check_win('O'):
                print('Player O wins!')
                self.game_over = True
            elif self.check_draw():
                print('It\'s a draw!')
                self.game_over = True

    def check_win(self, player):
        for i in range(3):
            # Check rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            # Check columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def check_draw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

def main():
    root = Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
