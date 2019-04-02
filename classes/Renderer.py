import pygame # Required for rendering the screen

class Renderer:
	"""
	Handles the rendering actions of the game the free up Game for logic
	"""
	def __init__(self, screenSize):
		""" 
		Initializes the render class
		"""
		self.backgroundColor = 0, 0, 0

		self.setScreen(screenSize)

	def render(self, map, entities):
		"""
		Renders the screen and everything in it

		arg map - the map or section of map to render
		arg entities - an array of the entities to render
		"""

		self.screen.fill(self.backgroundColor)
		for i in range(0, len(entities)):
			self.screen.blit(entities[i].getImage(), entities[i].get_rect())
			
		pygame.display.flip()

	def setScreen(self, screenSize):
		"""
		Sets the screen size and resets the pygame size
		"""
		# Catches invalid screen sizes
		if(screenSize[0] <= 0 or screenSize[1] <= 0):
			raise ValueError

		# Catches max screensize
		# TODO - do we want to error out or set the max values?

		self.screenSize = screenSize

		self.screen = pygame.display.set_mode(self.screenSize)





		



	


