# blurb
import sys
import chess
import chess.svg
from ChessSimAI import *

class TerminalBoard():
    def __init__(self):
        self.board = chess.Board(fen='6k1/8/8/8/8/8/8/Q6K b - - 0 0')

    def printBoard(self):
        print(self.board)

    def getBoard(self):
        return self.board

    def makeMoveAI(self):
        board = fenToBoard(self.getBoard().board_fen())
        AI = ChessSimAI()
        move = AI.makeAIMove(board)
        move = chess.Move.from_uci(move)


        if move not in self.board.legal_moves:
            print("The AI hath broketh the law")
        self.board.push(move)

    def makeMoveHuman(self):
        b = self.board
        print(b)
        print("Potential moves: ")
        for potentialMove in list(b.legal_moves):
            print potentialMove

        goodInput = False
        move = input("Type move in string representation: ")
        move = chess.Move.from_uci(move)
        while goodInput == False:
            if move in b.legal_moves:
                goodInput = True
                b.push(move)
            else:
                move = input("Invalid move, type another move: ")
                move = chess.Move.from_uci(move)


def fenToBoard(fen):
    piecesDict = {"Q":"wqueen", "K":"wking", "k":"bking", "q":"bqueen"}
    lines = fen.split("/")
    board = []
    for line in lines:
        row = []
        for char in line:
            if char in list(piecesDict.keys()):
                row.append(piecesDict[char])
            else:
                num = int(char)
                for i in range(num):
                    row.append(0)
        board.append(row)
    return board

def main():
    #board = chess.Board(fen='k7/p7/1p6/8/8/8/8/K5Q1 w - - 0 0')
    board = TerminalBoard()
    turn = 1

    while not board.getBoard().is_game_over():

        if (turn == 1):
            board.makeMoveHuman()
            turn = 0

        else:
            board.makeMoveAI()
            turn = 1
            
        
        
        

if __name__ == "__main__":
    main()
