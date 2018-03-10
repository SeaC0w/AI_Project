# blurb
import sys
import chess
import chess.svg
from ChessSimAI import *
from BoardGraphics import *
from ChessGameTree import *

class TerminalBoard():
    def __init__(self):
        self.board = chess.Board(fen='6k1/8/8/8/8/7K/8/Q7 b - - 0 0')

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

    def makeMoveTreeAI(self):
        board = fenToBoard(self.getBoard().board_fen())
        AI = AdversSearchAI()
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
            print(potentialMove)

        goodInput = False
        move = input("Type move in string representation: ")
        move = chess.Move.from_uci(move)
        while goodInput == False:
            if move in b.legal_moves:
                goodInput = True
                b.push(move)
                print(b)
            else:
                move = input("Invalid move, type another move: ")
                move = chess.Move.from_uci(move)

    def getFen(self):
        return self.board.epd().split()[0]

    # ONLY used for passing positions to BoardGraphics
    def getPiecePositions(self):
        currFen = self.getFen()
        pieces = ["Q", "K", "k", "q"]
        lines = currFen.split("/")
        piecePlaces = {}
        for i in range(len(lines)):
            j = 0
            for char in lines[i]:
                if char not in pieces:
                    j += int(char)
                else:
                    # piecePlaces[char] = (j,7-i)
                    piecePlaces[char] = (i,j)
                    j += 1
        return piecePlaces


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
    shownBoard = BoardGraphics()
    shownBoard.drawGrid()
    turn = 1

    while not board.getBoard().is_game_over():
        print("~~~~~~~~~~~~~~~~~~~")
        shownBoard.updateBoard(board.getPiecePositions())
        print("~~~~~~~~~~~~~~~~~~~")

        if (turn == 1):
            board.makeMoveHuman()
            turn = 0

        else:
            board.makeMoveAI()
            turn = 1





if __name__ == "__main__":
    main()
