# blurb
import sys
import chess
import chess.svg
from ChessSimAI import *

class TerminalBoard():
    def __init__(self):
        self.board = chess.Board(fen='q6k/8/8/8/8/8/8/7K w - - 0 0')

    def printBoard(self):
        print(self.board)

    def getBoard(self):
        return self.board

    def makeMoveAI(self):
        board = fenToBoard(self.getBoard().board_fen())
        AI = ChessSimAI()
        move = AI.makeAIMove(board)

        if move not in self.board.legal_moves:
            print("The AI hath broketh the law")
        self.board.push(move)

    def makeMoveHuman(self):
        b = self.board
        print(b)
        print(list(b.legal_moves))
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
        b.push(move)

# def boardTestOne():
#     board = chess.Board(fen='q6k/8/8/8/8/8/8/7K w - - 0 0')
#     print(board)
#     print(board.board_fen())

#     # newB = ChessSimAI.fenToBoard(board.board_fen())
#     # print(newB)
#     # print(ChessSimAI.moveToString(((0,0),(1,0))))

#     print(list(board.legal_moves))
#     goodInput = False
#     move = input("Type move in string representation: ")
#     move = chess.Move.from_uci(move)
#     while goodInput == False:
#         if move in board.legal_moves:
#             goodInput = True
#             board.push(move)
#         else:
#             move = input("Invalid move, type another move: ")
#             move = chess.Move.from_uci(move)
#     print(board)
#     goodInput = False
#     print(list(board.legal_moves))
#     while goodInput == False:
#         if move in board.legal_moves:
#             goodInput = True
#             board.push(move)
#         else:
#             move = input("Invalid move, type another move: ")
#             move = chess.Move.from_uci(move)
#     print(board)
#     print(board.board_fen())

# def main():
#     board = chess.Board(fen='k7/p7/1p6/8/8/8/8/K5Q1 w - - 0 0')
#     print(board)
#     print(list(board.legal_moves))
#     goodInput = False
#     move = input("Type move in string representation: ")
#     move = chess.Move.from_uci(move)
#     while goodInput == False:
#         if move in board.legal_moves:
#             goodInput = True
#             board.push(move)
#         else:
#             move = input("Invalid move, type another move: ")
#             move = chess.Move.from_uci(move)
#     print(board)
#     print(list(board.legal_moves))
#     goodInput = False
#     move = input("Type move in string representation: ")
#     move = chess.Move.from_uci(move)
#     while goodInput == False:
#         if move in board.legal_moves:
#             goodInput = True
#             board.push(move)
#         else:
#             move = input("Invalid move, type another move: ")
#             move = chess.Move.from_uci(move)
#     print(board)
#     print(board.board_fen())

#Check to see if board is done here
def gameNotDone():
    return True


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

    while gameNotDone():

        if (turn == 1):
            # print(board)
            # print(list(board.legal_moves))
            # goodInput = False
            # move = input("Type move in string representation: ")
            # move = chess.Move.from_uci(move)
            # while goodInput == False:
            #     if move in board.legal_moves:
            #         goodInput = True
            #         board.push(move)
            #     else:
            #         move = input("Invalid move, type another move: ")
            #         move = chess.Move.from_uci(move)

            board.makeMoveHuman()
            turn = 0

        else:
            board.makeMoveAI()
            turn = 1
            
        
        
        

if __name__ == "__main__":
    main()
