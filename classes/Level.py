import class.Chunk as chunk

class Level:
	def __init__(self, levelName):
		""" 
		Initializes the level and all associated chunks

		arg - the name of the level to load
		"""

		self.load(levelName)

	def load(self, levelName):
		"""
		Loads the given level into chunks.

		arg levelName - the name of the level to load
		"""

		self.levelName = levelName
		# Load and open the file

		# For testing purposes, we're just loading in test data
		self.areaSize = (15, 15)

		self.chunks = []
		for y in range(0, self.areaSize[1]):
			for x in range(0, self.areaSize[0]):
				self.chunks[x][y] = Chunk("", x, y)
