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
		threat = self.AIThreatRepresentation(move, board)
		count = self.BFSCalcTotalNodes(threat)
		return count

	#Method that conducts a breadth first search given a position to see the amount
	#of space given to the enemy king
	def BFSCalcTotalNodes(self, tempBoard):
		return 5


	#Creates a fake board that fills all possible positions that are under threat
	#from the AI with values, so that the BFS can run and stop at these values
	#An example would be if a queen was on a diagonal, that diagonal would be filled
	#with q's
	#Returns a board with altered values
	def AIThreatRepresentation(self, move, board):
		tempBoard = board
		if (move != None):
			tempBoard[move[1][0]][move[1][1]] = tempBoard[move[0][0]][move[0][1]]
			tempBoard[move[0][0]][move[0][1]] = 0
		wqueenPosition = None
		wkingPosition = None
		rowNum = 0
		for row in tempBoard:
			colNum = 0
			for col in row:
				if (col == "wqueen"):
					wqueenPosition = [rowNum, colNum]
				elif(col == "wking"):
					wkingPosition = [rowNum, colNum]

				colNum += 1
			rowNum += 1


		if (wkingPosition != None):
			tempBoard = self.AIThreatAdderKing(wkingPosition, tempBoard)

		if (wqueenPosition != None):
			tempBoard = self.AIThreatAdderQueen(wqueenPosition, tempBoard)



		return tempBoard

	#Helper method for the AIThreatRepresentation, actually added the values in for the king
	def AIThreatAdderKing(self, pos, board):
		row = pos[0]
		col = pos[1]
		addThreatToBoardFirstIteration = [[row-1, col-1], [row-1, col], [row-1, col +1], [row, col-1], [row, col+1], [row+1, col-1], [row+1, col], [row+1, col+1]]
		addThreatToBoard = []
		for element in addThreatToBoardFirstIteration:
			if (element[0] < 0 or element[1] < 0 or element[0] > 7 or element[1] > 7 or board[element[0]][element[1]] == "wqueen"):
				pass
			else:
				addThreatToBoard.append(element)

		for element in addThreatToBoard:
			if (board[element[0]][element[1]] == 0):
				board[element[0]][element[1]] = "k"
			else:
				board[element[0]][element[1]] = board[element[0]][element[1]] + "k"

		return board

	#Helper method for the AIThreatRepresentation, actually added the values in for the king
	def AIThreatAdderQueen(self, pos, board):
		row = pos[0]
		col = pos[1]
		addThreatToBoardFirstIteration = []
		addThreatToBoard = []
		#Vert
		for i in range(1,8):
			if((row + i) > 7 or board[row + i][col] == "wking"):
				break
			else:
				addThreatToBoardFirstIteration.append([row + i, col])
		for i in range(1,8):
			if((row - i) <0 or board[row - i][col] == "wking"):
				break
			else:
				addThreatToBoardFirstIteration.append([row - i, col])

		#horizontal
		for i in range(1,8):
			if((col + i) > 7 or board[row][col + i] == "wking"):
				break
			else:
				addThreatToBoardFirstIteration.append([row, col+ i])
		for i in range(1,8):
			if((col -1) <0 or board[row][col - i] == "wking"):
				break
			else:
				addThreatToBoardFirstIteration.append([row, col -i])

		#Left to right diagonal
		for i in range(1,8):
			if((row + i) > 7 or (col + i) > 7 or board[row + i][col + i] == "wking"):
				break
			else:
				addThreatToBoardFirstIteration.append([row + i, col + i])
		for i in range(1,8):
			if((row - i) <0 or (col -i) <0 or board[row - i][col - i] == "wking"):
				break
			else:
				addThreatToBoardFirstIteration.append([row - i, col - i])

		#Right to left diagonal
		for i in range(1,8):
			if((row + i) > 7 or (col- i) <0 or board[row + i][col - i] == "wking"):
				break
			else:
				addThreatToBoardFirstIteration.append([row + i, col -i])
		for i in range(1,8):
			if((row -i) <0 or (col + i) > 7 or board[row - i][col + i] == "wking"):
				break
			else:
				addThreatToBoardFirstIteration.append([row - i, col + i])

		#remove impossibilities
		for element in addThreatToBoardFirstIteration:
			if (element[0] < 0 or element[1] < 0 or element[0] > 7 or element[1] > 7 or board[element[0]][element[1]] == "wking" or board[element[0]][element[1]] == "bking"):
				pass
			else:
				addThreatToBoard.append(element)

		for element in addThreatToBoard:
			if (board[element[0]][element[1]] == 0):
				board[element[0]][element[1]] = "q"
			else:
				board[element[0]][element[1]] = board[element[0]][element[1]] + "q"

		return board


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
		# move = [[0,0],[0,0]]
		move = None
		AIThreatRepresentation = self.AIThreatRepresentation(move, board)
		print (AIThreatRepresentation)

		# for i in range (0, 8):
		# 	for j in range (0,8):
		# 		if (AIThreatRepresentation[i][j] == 'q' or AIThreatRepresentation[i][j] == 'k' or AIThreatRepresentation[i][j] == "qk"):
		# 			pieceType = self.getPieceType(AIThreatRepresentation[i][j])
		# 			#print (pieceType)
		# 			potentialMove = [i, j, pieceType]
		# 			#print ("Potenial Move is :", str(potentialMove))
		# 			space = self.calculateEnemySpace(potentialMove, AIThreatRepresentation)

		# 			#If our discovered move gets better space gain, we construct the new move as our move
		# 			if (space > bestSpace): #MIGHT NEED TO CHANGE THIS WILL GET STUCK IN LOOP PROBS
		# 				curPiecePos = self.getCurrentPiecePosition(potentialMove[2], board) 
		# 				move = [curPiecePos ,[potentialMove[0], potentialMove[1]]]
		# 				bestSpace = space


		# print (move)
		return move


	





	