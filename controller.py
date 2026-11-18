from ai import Ai
from tictactoe import TicTacToe

game = TicTacToe()
computer = Ai("o" , game)

def printBoard(state):
    for i in range(3):
        print(state[i*3:(i+1)*3])

print("Initial Board:")
printBoard(game.state)

while(game.isRunning):
    row = int(input("Enter 'x' in which row : "))
    col = int(input("Enter 'x' in which column : "))

    game.makeMove(row , col)
    print("Player's turn:")
    printBoard(game.state)

    computer.makeTurn()
    print("Computer's turn:")
    printBoard(game.state)

print(f"The winner is {game.winner}")