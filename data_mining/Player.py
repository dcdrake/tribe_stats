class Player(object):

	def __init__(self, firstname_in, lastname_in, number_in):
		self.firstname  = firstname_in
		self.lastname   = lastname_in
		self.number     = number_in
		self.games      = []

	def addGame(self, new_game):
		self.games.append(new_game)

	def getGame(self, index):
		return self.games.pop(index)

	def __str__(self):
		rep = self.firstname + ' ' + self.lastname + ', ' + self.number
		return rep
