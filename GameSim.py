
class Game:

	MIN = 0
	MAX = 1
	turn = MAX
	gameBoard = []
	WHITEKING = "wking"
	WHITEQUEEN = "wqueen"
	BLACKKING = "bking"

	def __init__(self):
		#instantiate ChessSimAI
		#instantiate BoardGraphics
		self.gameBoard = self.setUpBoard()
		


	def setUpBoard(self):
		gameBoard = [[0 for i in range(8)] for j in range(8)]
		gameBoard[0][3] = self.WHITEQUEEN
		gameBoard[1][5] = self.WHITEKING
		gameBoard[6][7] = self.BLACKKING
		return gameBoard
		

	#The human move clicks on a piece, and then clicks on where to move it. Then
	def makeHumanMove(self):
		coor1 = None
		coor2 = None
		pieceSelected = None
		while not self.isValidMove(coor1, coor2, pieceSelected):
			pass
			#acquire coordinates of first click
			#pieceSelected = self.getPieceType(coor1)
			#acquire coordinates of second click
		self.updateBoard(coor1, coor2, pieceSelected)

	def getPieceType(self, coordinates):
		return self.gameBoard[coordinates[0]][coordinates[1]]

	def isValidMove(self, coor1, coor2, pieceType):
		# if(coor1, coor2, pieceType == None, None, None):
		# 	return False
		# else:
		# 	#Check here if move is valid

		return True


	def makeAIMove(self):
		pass

	def updateBoard(self, startCoordinates, endCoordinates, pieceSelected):
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
	#for x in range (0, 30):
		if (game.getTurn() == game.MAX):
			#game.makeHumanMove()
			#Update graphics game.graphicobject.updategraphics(game.board)
			game.changeTurn()
			


		else:
			game.makeAIMove()
			#Update graphics
			game.changeTurn()
			

	print game.gameBoard


main()





