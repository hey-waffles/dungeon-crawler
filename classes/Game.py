# Pip Installed Packages
import pygame

# Project Packages
import classes.constant as constant
import classes.enums as enum
import classes.IEntity as IEntity
import classes.Player as Player

class Game:
	"""
	The core game class for running and handling all game functions
	"""
	def __init__(self):
		"""
		Initializes the game class
		"""
		pygame.init()
		self.clock = pygame.time.Clock()
		return

	def run(self):
		"""
		Loops constantly until an exit case is reached
		"""
		while 1:
			self.tick()

	def startGame(self):
		"""
		A function called by main after all arguments have been processed and the 
		game is ready to initalize
		"""

		# TODO - actions that prepare everything for 
		self.size = self.width, self.height = 320, 240
		self.speed = [2, 2]
		self.black = 255, 255, 255

		self.screen = pygame.display.set_mode(self.size)

		self.player = Player.Player()

		self.run()

	def tick(self):
		"""
		Runs on every update of the game. 
		"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit() # TODO - find system-specific exits

			if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
				self.player.inputControl(event)


		self.player.update()

		self.screen.fill(self.black)
		self.screen.blit(self.player.image, self.player.rect)
		pygame.display.update()

		self.clock.tick(30)

		return
