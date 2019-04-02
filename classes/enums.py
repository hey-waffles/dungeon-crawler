from enum import Enum

# An enum for making states easy to read when coding 
class State(Enum):
	PREP = 0 # A state for starting up the game. Used to limit certain functions
	GAME = 1
	START = 2

# An enum for making directions easy to read while coding
class Direction(Enum):
	UP = 0
	DOWN = 1
	LEFT = 2
	RIGHT = 3

# An enum for keeping track of which position the x and y values are in
class Pos(Enum):
	X = 0
	Y = 1
