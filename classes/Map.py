import enums as Enum
import entity

class Map:
	"""
	The object for rendering the playable area
	"""
	def __init__(self, level="default.lvl"):
		"""
		Initializes the Map

		arg level - the first level to initialize on runtime

		"""
		self.changeLevel(level)

		return

	def changeLevel(newLevel):
		"""
		Saves the current level state and changes to the given level

		arg newLevel - the name of the level to change to
		"""

		self.level._saveLevelState()
		self.level.load(newLevel)


	def _buildMap(self):
		_initializeMap()

	def _initializeMap(self):
		self.map = []

		for y in range(0, self.mapSize[Enum.Pos.Y]):
			for x in range(0, self.mapSize[Enum.Pos.X]):
				self.map[y][x] = Tile()

class Tile extends entity.Entity:
	def __init__(self):
		self.damagable = True
		self.health = 100
		
		return

	def makeFloor(self):

