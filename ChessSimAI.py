from copy import *

def moveToString(move):
	translate = ["a", "b", "c", "d", "e", "f", "g", "h"]
	return translate[move[0][1]] + str(8 - move[0][0]) + translate[move[1][1]] + str(8 - move[1][0])


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
		potentialEnemyMoves = self.findPotentialEnemyMoves(threat)
		bKingPos = self.findPiecePos('bking', threat)
		wQueenPosition = self.findPiecePos("wqueen", threat)
		wKingPosition = self.findPiecePos("wking", threat)
		mostSpace = 0
		space = 0
		for move in potentialEnemyMoves:
			tempBoard = [[0 for i in range(8)] for j in range(8)]
			tempBoard[move[0]][move[1]] = 'bking'
			tempBoard[wQueenPosition[0]][wQueenPosition[1]] = 'wqueen'
			tempBoard[wKingPosition[0]][wKingPosition[1]] = 'wking' 
			tempBoard = self.AIThreatRepresentation(None, tempBoard)
			space = 0
			space = self.calcTotalAvailableSpace(move, tempBoard)
			if (space > mostSpace):
				mostSpace = space
		return space

	#Method that conducts a breadth first search given a position to see the amount
	#of space given to the enemy king
	def calcTotalAvailableSpace(self, move, tempBoard):
		posSeen = []
		posUnseen = [move]
		space = self.calcSpaceHelper(posSeen, posUnseen, tempBoard)
		if (space == None):
			space = 0
		return space

	def calcSpaceHelper(self, posSeen, posUnseen, tempBoard):

		if(len(posUnseen) == 0):
			return len(posSeen)

		#for pos in posUnseen:
		pos = posUnseen.pop()
		posSeen.append(pos)
		row = pos[0]
		col = pos[1]
		potentialUnseenFirstIteration = [[row-1, col-1], [row-1, col], [row-1, col +1], [row, col-1], [row, col+1], [row+1, col-1], [row+1, col], [row+1, col+1]]
		for element in potentialUnseenFirstIteration:
			if (element[0] < 0 or element[1] < 0 or element[0] > 7 or element[1] > 7 or 
				tempBoard[element[0]][element[1]] == "wqueen" or tempBoard[element[0]][element[1]] == "q" or tempBoard[element[0]][element[1]] == "k"
				or element in posSeen or element in posUnseen):
				pass
			else:
				posUnseen.append(element)

		return self.calcSpaceHelper(posSeen, posUnseen, tempBoard)





	#Returns a list of allowed moves by the enemy king after recieving a threat representation for a board
	def findPotentialEnemyMoves(self, threatRep):

		tempBoard = []

		for element in threatRep:
			tempBoard.append(copy(element))

		kingPos = self.findPiecePos("bking", tempBoard)
		row = kingPos[0]
		col = kingPos[1]
		potentialMovesFirstIteration = [[row-1, col-1], [row-1, col], [row-1, col +1], [row, col-1], [row, col+1], [row+1, col-1], [row+1, col], [row+1, col+1]]
		potentialMoves = []

		for element in potentialMovesFirstIteration:
			if (element[0] < 0 or element[1] < 0 or element[0] > 7 or element[1] > 7 or 
				tempBoard[element[0]][element[1]] == "wqueen" or tempBoard[element[0]][element[1]] == "q"):
				pass
			else:
				potentialMoves.append(element)

		return potentialMoves





	def findPiecePos(self, piece, board):
		Pos = None
		rowNum = 0
		for row in board:
			colNum = 0
			for col in row:
				if (col == piece):
					Pos = [rowNum, colNum]

				colNum += 1
			rowNum +=1
		return Pos




	#Creates a fake board that fills all possible positions that are under threat
	#from the AI with values, so that the BFS can run and stop at these values
	#An example would be if a queen was on a diagonal, that diagonal would be filled
	#with q's
	#Returns a board with altered values
	def AIThreatRepresentation(self, move, board):
		tempBoard = []

		for element in board:
			tempBoard.append(copy(element))


		if (move != None):
			tempBoard[move[1][0]][move[1][1]] = tempBoard[move[0][0]][move[0][1]]
			tempBoard[move[0][0]][move[0][1]] = 0
		wqueenPosition = self.findPiecePos("wqueen", tempBoard)
		wkingPosition = self.findPiecePos("wking", tempBoard)
		if (wkingPosition != None):
			tempBoard = self.AIThreatAdderKing(wkingPosition, tempBoard)

		if (wqueenPosition != None):
			tempBoard = self.AIThreatAdderQueen(wqueenPosition, tempBoard)

		#print tempBoard
		return tempBoard

	#Helper method for the AIThreatRepresentation, actually added the values in for the king
	def AIThreatAdderKing(self, pos, board):
		row = pos[0]
		col = pos[1]
		addThreatToBoardFirstIteration = [[row-1, col-1], [row-1, col], [row-1, col +1], [row, col-1], [row, col+1], [row+1, col-1], [row+1, col], [row+1, col+1]]
		addThreatToBoard = []
		for element in addThreatToBoardFirstIteration:
			if (element[0] < 0 or element[1] < 0 or element[0] > 7 or element[1] > 7 or board[element[0]][element[1]] == "wqueen" or board[element[0]][element[1]] == "bking"):
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


	def cleanBoard(self, board):
		for i in range (0, 8):
			for j in range (0,8):
				if (board[i][j] != 'wking' and board[i][j] != 'wqueen' and board[i][j] != 'bking'):
					board[i][j] = 0

		return board

	# def policy1(self, board):
	# 	return True

	# def policy2(self, board):
	# 	return False

	# def policy3(self, board):
	# 	return False

	#This is our 'main' function that calculates the AI move
	def makeAIMove(self, board):

		bestSpace = 10000000
		move = None
		
		AIThreatRepresentation = self.AIThreatRepresentation(move, board)
		
		# if (self.policy1(board)):
		for i in range (0, 8):
			for j in range (0,8):
				if (AIThreatRepresentation[i][j] == 'q' or AIThreatRepresentation[i][j] == 'k' or AIThreatRepresentation[i][j] == "qk"):
					pieceType = self.getPieceType(AIThreatRepresentation[i][j])
					
					
					startPos = self.getCurrentPiecePosition(pieceType, board)
					potentialMove = [startPos, [i, j]]
					
					space = self.calculateEnemySpace(potentialMove, board)
					print space
					#If our discovered move gets better space gain, we construct the new move as our move
					if (space < bestSpace and space > 1): 
						move = potentialMove
						bestSpace = space

		# elif (policy2()):

		move = moveToString(move)
		print "------------------------"
		print "\n"
		print "AI Move: " + move
		print "\n"
		print "------------------------"
		return move
