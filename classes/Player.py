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

		self.spriteSheetMap = {
			"direction":{
				enum.Direction.UP:3,
				enum.Direction.LEFT:1,
				enum.Direction.RIGHT:2,
				enum.Direction.DOWN:0
			},
			"walk":{
				0:1,
				1:0,
				2:1,
				3:2
			}
		}
		self.animationState = {
			"direction":enum.Direction.DOWN,
			"walk":0
		}

		return

	def update(self):
		self.updateImage()		


	def updateImage(self):
		"""
		Sets the individual image to load
		"""
		# TODO - base state of of delta time (time between frames) to prevent slowdown from FPS dropping
		self.animationState["walk"] = (self.animationState["walk"] + 0.2) % 4
		
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