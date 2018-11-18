# Represents a single space within the board.
class Tile():
	# Initializes the tile. 
	# By default, each tile is a wall until a board is built
	def __init__(self):
		self.isWall = True

	# Renders the object character in this tile
	def render(self):
		if self.isWall == True:
			return '0';

# Represents the game board for the PC to explore
class Board():
	# Initializes the board with a rectangle of Tiles
	#
	# @width - the number of tiles wide the board is
	# @height - the number of tiles tall the board is
	def __init__(self, width, height):
		self.width = width # width of the max play area
		self.height = height # height of the max play area

		self.board = []; # collection of all tiles that make up the board

		# Loop through each row & column to initialize the tile
		for y in range(0, self.height):
			row = [];
			for x in range(0, self.width):
				tile = Tile();
				row.append(tile);

			self.board.append(row);

	# Renders each tile in the board
	def render(self):
		for y in range(0, self.height):
			row = '';

			for x in range(0, self.width):
				row += self.board[y][x].render();

			print(row)
