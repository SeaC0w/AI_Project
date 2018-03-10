from graphics import *

windowHeight = 800
windowWidth = 650
imgDict = {"Q":"wqueen.png", "K":"wking.png", "k":"bking.png", "q":"bqueen.png"}

class BoardGraphics():
	def __init__(self):
		self.window = GraphWin("Chess Board", windowWidth, windowHeight)
		self.boxes = []
		self.texts = []

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

	# given a dictionary of positions for all the pieces in a game
	# draw a pretty chess board with the pieces at those locations
	def updateBoard(self, positions):
		for t in self.texts:
			t.undraw()
		self.texts = []
		for pieceName in list(positions.keys()):
			p = positions[pieceName]
			c = self.boxes[p[0]][p[1]].getCenter()
			# t = Text(c, pieceName)
			# t.draw(self.window)
			# self.texts.append(t)
			i = Image(c, imgDict[pieceName])
			i.draw(self.window)
			self.texts.append(i)

	# draws the chessboard (background, not the pieces)
	def drawGrid(self):
		for row in self.boxes:
			for item in row:
				item.draw(self.window)


# def main():
# 	b = BoardGraphics()
# 	b.drawGrid()
#
# if __name__ == "__main__":
# 	main()
