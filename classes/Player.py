import math
import pygame
import classes.constant as constant
import classes.enums as enum
import classes.ICharacter as ICharacter

class Player(ICharacter.ICharacter):
	def __init__(self):
		ICharacter.ICharacter.__init__(self)
		self.health = 100 # An entity's health. It will be destroyed if health < 0

		self.name = "Waals" # This object's name
		self.interactText = "Hey, this is you!"

		self._setSpriteSheet()
		self._setRect()

		return

	def setDirection(self, direction):
		# TODO - check if the direction is in the enum
		self.state["update"] = True
		self.state["direction"] = direction

	def setWalking(self, isWalking):
		# TODO - check if the direction is in the enum
		self.state["update"] = True
		self.state["walking"] = isWalking

	def inputControl(self, event):
		"""
		Handles key input to handle player control
		"""
		# Start moving
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				self.setMoving("x", -1)

			if event.key == pygame.K_DOWN:
				self.setMoving("y", 1)

			if event.key == pygame.K_RIGHT:
				self.setMoving("x", 1)

			if event.key == pygame.K_UP:
				self.setMoving("y", -1)

		# End moving
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				self.setMoving("x", 1)

			if event.key == pygame.K_DOWN:
				self.setMoving("y", -1)

			if event.key == pygame.K_RIGHT:
				self.setMoving("x", -1)

			if event.key == pygame.K_UP:
				self.setMoving("y", 1)
	
	def setMoving(self, direction, speed):
		self.moving[direction] += speed

	def update(self):
		self.move()

		self.updateImage() # Update Animation		


	def updateImage(self):
		"""
		Sets the individual image to load
		"""
		# TODO - base state of of delta time (time between frames) to prevent slowdown from FPS dropping
		if self.moving["x"] != 0 or self.moving["y"] != 0:
			self.animationState["walk"] = (self.animationState["walk"] + 0.2) % 4

			# Determine which way we're moving
			if self.moving["x"] > 0:
				self.animationState["direction"] = enum.Direction.RIGHT

			elif self.moving["x"] < 0:
				self.animationState["direction"] = enum.Direction.LEFT

			elif self.moving["y"] > 0:
				self.animationState["direction"] = enum.Direction.DOWN

			elif self.moving["y"] < 0:
				self.animationState["direction"] = enum.Direction.UP
		
		else:
			self.animationState["walk"] = 0

		# TODO - reuse the same Rect, just move it around 
		self.image = self.spriteSheet.subsurface(
			self.spriteSheetMap['walk'][math.floor(self.animationState["walk"])] * constant.tileSize, 
			self.spriteSheetMap['direction'][self.animationState["direction"]] * constant.tileSize, 
			constant.tileSize, 
			constant.tileSize
		)

	def _setSpriteSheet(self):
		"""
		Loads the spriteSheet resource in from the resources directory
		"""

		self.spriteSheet = pygame.image.load("resources/waals_character.png")

	def _setRect(self):
		self.rect = pygame.Rect(
			0  ,
			0,
			self.tileSize[0] * constant.tileSize,
			self.tileSize[1] * constant.tileSize
		)
		# self.rect.x = 0  
		# self.rect.y = 0
		# self.rect.width =  self.tileSize[0] * constant.tileSize
		# self.rect.height = self.tileSize[1] * constant.tileSize