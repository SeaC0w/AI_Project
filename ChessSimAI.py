class ChessSimAI:


	def __init__(self):
		pass



	'''
	We are calculating optimal moves for the AI based on the theory that minimization
	of space for the enemy will lead to a swift checkmate. Here, we calculate the 
	space the king could move around in regardless of the amount of turns without
	moving into check.
	@params: board state, position ([coor1, coor2, piecetype])
	@return: the move (coordinates) that minimizes the enemies available space
	'''
	def calculateEnemySpace(self, move, board):
		#Recalculate the AIThreatRepresentation for the move
		#threat = self.AIThreatRepresentation(move, board)
		#count = self.BFSCalcTotalNodes(threat)
		#return count
		return 5 #temp

	#Method that conducts a breadth first search given a position to see the amount
	#of space given to the enemy king
	def BFSCalcTotalNodes(self, tempBoard):
		pass


	#Creates a fake board that fills all possible positions that are under threat
	#from the AI with values, so that the BFS can run and stop at these values
	#An example would be if a queen was on a diagonal, that diagonal would be filled
	#with q's
	#Returns a board with altered values
	def AIThreatRepresentation(self, move, board):
		tempBoard = board
		tempBoard[2][4] = "k"
		wqueenPosition = None
		wkingPosition = None
		rowNum = 0
		colNum = 0
		for row in tempBoard:
			for col in row:
				if (col == "wqueen"):
					wqueenPosition = [rowNum, colNum]
				elif(col == "wking"):
					wkingPosition = [rowNum, colNum]

				colNum += 1
			rowNum += 1

		print (wqueenPosition)
		print (wkingPosition)



		return tempBoard

	#Builds a temporary board for the purpose of the AITHreatRepresentation
	def testBoard(self, position, board):
		pass

	def getPieceType(self, string):
		piece = "wking" if string == 'k' else "wqueen"
		return piece

	def getCurrentPiecePosition(self, pieceType, board):
		pos = None
		for i in range (0, 8):
			for j in range (0,8):
				if (board[i][j] == pieceType):
					pos = [i,j] 

		return pos

	#This is our 'main' function that calculates the AI move
	def makeAIMove(self, board):

		bestSpace = 0
		move = [[0,0], [0,0]]
		AIThreatRepresentation = self.AIThreatRepresentation(None, board)

		for i in range (0, 8):
			for j in range (0,8):
				if (AIThreatRepresentation[i][j] == 'q' or AIThreatRepresentation[i][j] == 'k' or AIThreatRepresentation[i][j] == "qk"):
					pieceType = self.getPieceType(AIThreatRepresentation[i][j])
					print (pieceType)
					potentialMove = [i, j, pieceType]
					print ("Potenial Move is :", str(potentialMove))
					space = self.calculateEnemySpace(potentialMove, AIThreatRepresentation)

					#If our discovered move gets better space gain, we construct the new move as our move
					if (space > bestSpace): #MIGHT NEED TO CHANGE THIS WILL GET STUCK IN LOOP PROBS
						curPiecePos = self.getCurrentPiecePosition(potentialMove[2], board) 
						move = [curPiecePos ,[potentialMove[0], potentialMove[1]]]
						bestSpace = space


		#move = [[0,3], [0,4]] #Temp
		return move


	





	