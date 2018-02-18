from graphics import *

windowHeight = 800
windowWidth = 650

class BoardGraphics():
	def __init__(self):
		self.window = GraphWin("Chess Board", windowWidth, windowHeight)
		# self.window.setCoords(25, 25, windowWidth-25, windowHeight-25)
		self.validPieces = ["king", "queen"]
		self.message = Text(Point(325, 725), 650)
		self.message.setText('Game start')
		self.message.draw(self.window)
		self.boxes = []
		self.whitePieces = []
		self.blackPieces = []

		self.rect = Rectangle(Point(5,5), Point(10,10))
		self.rect.setFill("red")
		self.rect.draw(self.window)

		for row in range(8):
			gridRow = []
			p1y = (75 * row) + 25
			p2y = p1y + 75
			for col in range(8):
				p1x = (75 * col) + 25
				p2x = p1x + 75
				curr = Rectangle(Point(p1x, p1y), Point(p2x, p2y))
				if (row % 2) != (col % 2):
					curr.setFill("green")
				gridRow.append(curr)
			self.boxes.append(gridRow)

	def setMessage(self, s):
		# self.message.undraw()
		self.message.setText(s)
		# self.message.draw(self.window)

	#pieceData = [row, column, player, image, pieceType]
	def initPiece(self, data):
		player = data[2]
		piece = PieceGraphics(data[3], data[0], data[1], data[4])
		if player == 0:
			self.whitePieces.append(piece)
		elif player == 1:
			self.blackPieces.append(piece)
		else:
			self.setMessage("Invalid player assignment for piece")
			return
		return piece

	def checkforPieceAt(self, player, row, col):
		if player == 0:
			for p in self.whitePieces:
				print(p.row, p.column)
				if p.row == row and p.column == col:
					return p
			return False
		elif player == 1:
			print(p.row, p.column)
			for p in self.blackPieces:
				if p.row == row and p.col == col:
					return p
			return False
		else:
			self.setMessage("Invalid player argument")
			return False

	def setupOne(self):
		wking = self.initPiece([7, 0, 0, "wking.png", "king"])
		wqueen = self.initPiece([7, 4, 0, "wqueen.png", "queen"])
		bking = self.initPiece([0, 0, 1, "bking.png", "king"])
		if not wking or not wqueen or not bking:
			self.setMessage("Pieces couldnt be placed")
		wking.drawPiece(self.window)
		wqueen.drawPiece(self.window)
		bking.drawPiece(self.window)

	def drawGrid(self):
		for row in self.boxes:
			for item in row:
				item.draw(self.window)

	def playTurn(self, player):
		playName = ""
		if player == 0:
			playName = "White"
		else:
			playName = "Black"
		self.setMessage(playName + " player's turn:")
		clickValid = False
		while not clickValid:
			self.setMessage("Click a piece to move")
			click = self.window.getMouse()
			clickX = int((click.getX() - 25)//75)
			clickY = int((click.getY() - 25)//75)
			print(clickX, clickY)
			piece = self.checkforPieceAt(player, clickX, clickY)
			if (piece):
				click2Valid = False
				while not click2Valid:
					self.setMessage("Click a space to move to")
					click2 = self.window.getMouse()
					click2x = int((click.getX() - 25)//75)
					click2y = int((click.getY() - 25)//75)
					if (click2x, click2y) in piece.validMoves():
						self.setMessage(playName + " " + piece.type + " to" "(" + str(click2x) + "," + str(click2y) + ")")
						piece.setDrawPosition(click2x, click2y)
						piece.drawPiece(self.window)
						click2Valid = True
					else:
						self.setMessage("That location is not a valid move, choose again!")
				clickValid = True
			else:
				self.setMessage("No piece belonging to you at (" + str(clickX) + "," + str(clickY) + "),")
				print("No piece belonging to you at (" + str(clickX) + "," + str(clickY) + "),")

	def endRun(self):
		self.window.close()

class PieceGraphics():
	def __init__(self, image, row, col, pType):
		if (row < 0 or row > 7):
			return False
		if (col < 0 or col > 7):
			return False
		self.type = pType
		self.row = row
		self.column = col
		self.posX = 75 * row + 25
		self.posY = 75 * col + 25
		self.image = image
		self.im = Image(Point(self.posX + 37.5, self.posY + 37.5), image)

	def drawPiece(self, window):
		self.im.draw(window)

	def undrawPiece(self):
		self.im.undraw()

	def setDrawPosition(self, row, col):
		self.posX = 75 * row + 25
		self.posY = 75 * col + 25
		self.undrawPiece()
		self.im = Image(Point(self.posX + 37.5, self.posY + 37.5), self.image)


def main():
	b = BoardGraphics()
	b.drawGrid()
	print("hi")
	b.setupOne()
	# b.setMessage("yoyoyo")
	# time.sleep(5)
	for i in range(10):
		b.playTurn(i % 2)
	b.endRun()

if __name__ == "__main__":
	main()
