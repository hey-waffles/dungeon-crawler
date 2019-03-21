class Chunk:
	def __init__(self, mapFile, x, y):
		"""
		Initializes the chunk for rendering

		arg mapFile - the map file to read from
		arg x - the position in the map file to read from
		arg y - the position in the map to read from
		"""

		self.chunkSize = (32, 32)
		self.tileSize = (32, 32)

		self.tiles = []
		for y in range(0, self.chunkSize[1]):
			for x in range(0, self.chunkSize[0]):
				self.tiles[x][y] = pygame.rect(self.tileSize[0], self.tileSize[1])

	