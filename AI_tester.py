from ChessSimAI import *
from copy import *


def setUpBoard():
	gameBoard = [[0 for i in range(8)] for j in range(8)]
	gameBoard[4][4] = "wqueen"
	gameBoard[0][4] = "wking"
	gameBoard[7][7] = "bking"
	return gameBoard


if __name__ == "__main__":

	board = setUpBoard()
	# temp = copy(board)
	# temp[0][2] = "derp"
	# temp[4] = board[5]
	# temp[4][3] = 2


	ai = ChessSimAI()
	# threat = []
	# threat = ai.AIThreatRepresentation(None, board)

	# print(threat)
	# print (board)
	move = [[0,3],[1,4]]
	print ai.calculateDistance(move[0], move[1])






