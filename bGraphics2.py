# blurb
import sys
from IPython.display import SVG
import chess
import chess.svg

class TerminalBoard():
    def __init__(self):
        self.board = chess.Board(fen='q6k/8/8/8/8/8/8/7K w - - 0 0')

    def printBoard(self):
        print(self.board)

    def makeMoveAI(self, move):
        move = chess.Move.from_uci(move)
        self.board.push(move)

    def makeMoveHuman(self):
        move = input("Type move in string representation: ")
        move = chess.Move.from_uci(move)
        while goodInput == False:
            if move in board.legal_moves:
                goodInput = True
                board.push(move)
            else:
                move = input("Invalid move, type another move: ")
                move = chess.Move.from_uci(move)
        self.board.push(move)

def main():
    board = chess.Board(fen='q6k/8/8/8/8/8/8/7K w - - 0 0')
    print(board)
    print(list(board.legal_moves))
    goodInput = False
    move = input("Type move in string representation: ")
    move = chess.Move.from_uci(move)
    while goodInput == False:
        if move in board.legal_moves:
            goodInput = True
            board.push(move)
        else:
            move = input("Invalid move, type another move: ")
            move = chess.Move.from_uci(move)
    print(board)
    goodInput = False
    print(list(board.legal_moves))
    while goodInput == False:
        if move in board.legal_moves:
            goodInput = True
            board.push(move)
        else:
            move = input("Invalid move, type another move: ")
            move = chess.Move.from_uci(move)
    print(board)
    # SVG(chess.svg.board(board=board))

if __name__ == "__main__":
    main()
