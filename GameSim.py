
class Game:

	MIN = 0
	MAX = 1
	turn = MAX

	def __init__(self):
		#instantiate ChessSimAI
		#instantiate BoardGraphics
		pass




	def makeAIMove(self):
		pass

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

	while game.gameNotDone():
		if (game.getTurn() == game.MAX):
			print "MAX"
			game.changeTurn()
		else:
			print "MIN"
			game.changeTurn()

	print "How about this?"


main()





