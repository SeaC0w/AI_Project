# blurb
import sys
import chess
import chess.svg
import ChessSimAI

class TerminalBoard():
    def __init__(self):
        self.board = chess.Board(fen='q6k/8/8/8/8/8/8/7K w - - 0 0')

    def printBoard(self):
        print(self.board)

    def makeMoveAI(self, move):
        move = chess.Move.from_uci(move)
        if move not in self.board.legal_moves:
            print("just sayin, the AI broek the law")
        self.board.push(move)

    def makeMoveHuman(self):
        b = self.board
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

def boardTestOne():
    board = chess.Board(fen='q6k/8/8/8/8/8/8/7K w - - 0 0')
    print(board)
    print(board.board_fen())

    # newB = ChessSimAI.fenToBoard(board.board_fen())
    # print(newB)
    # print(ChessSimAI.moveToString(((0,0),(1,0))))

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
    print(board.board_fen())

def main():
    board = chess.Board(fen='k7/p7/1p6/8/8/8/8/K5Q1 w - - 0 0')
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
    print(board.board_fen())

if __name__ == "__main__":
    main()
