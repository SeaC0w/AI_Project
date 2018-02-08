from graphics import *

windowHeight = 650
windowWidth = 650

class BoardGraphics():
	def __init__(self):
		self.window = GraphWin("Chess Board", windowWidth, windowHeight)
		# self.window.setCoords(25, 25, windowWidth-25, windowHeight-25)
		self.boxes = []
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

	def setupOne(self):
		bking = PieceGraphics("bking.png", 0, 8)
		bqueen = PieceGraphics("bqueen.png", 4, 8)
		wking = PieceGraphics("wking.png", 0, 0)
		bking.drawPiece(self.window)
		bqueen.drawPiece(self.window)
		wking.drawPiece(self.window)

	def drawGrid(self):
		for row in self.boxes:
			for item in row:
				item.draw(self.window)


	def endRun(self):
		self.window.close()

class PieceGraphics():
	def __init__(self, image, row, col):
		self.posX = 75 * col + 25
		self.posY = 75 * row + 25
		self.object = Image(Point(self.posX, self.posY), image)

	def drawPiece(self, window):
		self.object.draw(window)

	def undrawPiece(self):
		self.object.undraw()

	def setBoardPosition(self, row, col):
		self.posX = 75 * col + 25
		self.posY = 75 * row + 25

def main():
	b = BoardGraphics()
	b.drawGrid()
	b.setupOne()
	time.sleep(15)
	b.endRun()

if __name__ == "__main__":
	main()
