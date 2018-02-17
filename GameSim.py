from ChessSimAI import *


class Game:

	MIN = 0
	MAX = 1
	turn = MAX
	gameBoard = []
	WHITEKING = "wking"
	WHITEQUEEN = "wqueen"
	BLACKKING = "bking"
	AI = ChessSimAI()


	#-------------------INITIALIZATION-------------------#

	def __init__(self):
		#instantiate BoardGraphics
		self.gameBoard = self.setUpBoard()
		


	def setUpBoard(self):
		gameBoard = [[0 for i in range(8)] for j in range(8)]
		gameBoard[0][3] = self.WHITEQUEEN
		gameBoard[1][5] = self.WHITEKING
		gameBoard[6][7] = self.BLACKKING
		return gameBoard
		

	#-------------------------------HUMAN MOVE FUNCTIONS---------------------------#

	#The human move clicks on a piece, and then clicks on where to move it. Then
	def makeHumanMove(self):
		coor1 = [6, 7]
		coor2 = [5, 7]
		pieceSelected = None
		#while not self.isValidMove(coor1, coor2, pieceSelected):
			#pass
			#acquire coordinates of first click
			#pieceSelected = self.getPieceType(coor1)
			#acquire coordinates of second click
		self.updateBoard(coor1, coor2)

	def getPieceType(self, coordinates):
		return self.gameBoard[coordinates[0]][coordinates[1]]

	#Checks to see if a human move is valid
	def isValidMove(self, coor1, coor2, pieceType):
		# if(coor1, coor2, pieceType == None, None, None):
		# 	return False
		# else:
		# 	#Check here if move is valid

		return True

	#---------------------AI MOVE FUNCTIONS------------------------#

	#The AI opponent makes a move
	def makeAIMove(self):
		AImove = self.AI.makeAIMove(self.gameBoard)
		coor1 = AImove[0]
		coor2 = AImove[1]
		self.updateBoard(coor1, coor2)


	#--------------------GENERAL GAME FUNCTIONALITY--------------------#

	def updateBoard(self, startCoordinates, endCoordinates):
		pieceSelected = self.gameBoard[startCoordinates[0]][startCoordinates[1]]
		self.gameBoard[startCoordinates[0]][startCoordinates[1]] = 0
		self.gameBoard[endCoordinates[0]][endCoordinates[1]] = pieceSelected

	def gameNotDone(self):
		return True

	def getTurn(self):
		return self.turn

	def changeTurn(self):
		if (self.turn == self.MAX):
			self.turn = self.MIN
		else:
			self.turn = self.MAX





#Main Simulation
def main():

	game = Game()

	#while game.gameNotDone():
	for x in range (0, 2):
		if (game.getTurn() == game.MAX):
			game.makeHumanMove()
			#Update graphics game.graphicobject.updategraphics(game.board)
			game.changeTurn()
			


		else:
			game.makeAIMove()
			#Update graphics
			game.changeTurn()
			

	print game.gameBoard
	print game.getTurn()


main()





