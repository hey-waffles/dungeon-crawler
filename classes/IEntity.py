import math 
import pygame 

import classes.constant	 as constant
import classes.physics	 as physics

class IEntity(pygame.sprite.Sprite): 
	"""
	The base Interface for all entities in the game to give base flags, values, 
	and functions
	"""
	def __init__(
		self,
		x = 0,
		y = 0
	):
		pygame.sprite.Sprite.__init__(self)

		self.isAlive = False # Should this be updated on each turn?
		self.isAnimated = False # Should this be checked for animations?
		self.isDamagable = False # This entity can be damaged by attacking
		self.isCollidable = False # Can a user, monster, or item go in this spot?
		self.isInteractable = False # Can a user interact with this item?
		self.isKillable = False # Will this object be destroyed when health drops below 0?

		self.health = 1 # An entity's health. It will be destroyed if health < 0

		self.name = "NO NAME" # This object's name
		# The text you get when you interact with this
		self.interactText = "Some strange object. You can't seem to tell what it is."


		self.currentVelocity = [0, 0] # The current velocity of an entity
		self.targetVelocity = [0, 0] # The target velocity of an entity (we acclerate to)

		self.maxAcceleration = 1	# The change in velocity that can be done in a single frame

		self.tileSize = (1,1) # Size in tiles

		self._setImage()
		# self.setPosition(x, y)
		return

	def move(self):
		""" 
		Overloads the Sprite's move method to handle movement on its own
		"""
		self.rect = self.rect.move(self.currentVelocity)

	def update(self):
		"""
		Runs all update actions on the entity
		"""
		self._updateVelocity()
		self.move()
		if self.rect.left < 0:
			self.targetVelocity[0] = abs(self.targetVelocity[0])

		if self.rect.right > 320:
			self.targetVelocity[0] = abs(self.targetVelocity[0]) * -1

		if self.rect.top < 0: 
			self.targetVelocity[1] = abs(self.targetVelocity[1])
			
		if self.rect.bottom > 240:
			self.targetVelocity[1] = abs(self.targetVelocity[1]) * -1

		return

	def _updateVelocity(self):
		""" 
		Updates velocity by determining the difference between two vectors and applying the appropriate amount of acceleration
		"""
		# Find difference between two vectors
		differenceVector = [0, 0]
		differenceVector[0] = self.targetVelocity[0] - self.currentVelocity[0]
		differenceVector[1] = self.targetVelocity[1] - self.currentVelocity[1]

		# Exit if there's nothing to update to avoid extra calculations
		if(differenceVector[0] == 0 and differenceVector[1] == 0):
			return

		# Find the hypotenuse of the difference vector
		differenceMagnitude = math.sqrt((differenceVector[0] ** 2) + (differenceVector[1] ** 2))

		# If hypotenuse <= maxAcceleration, set currentVelocity = targetVelocity
		if(differenceMagnitude <= self.maxAcceleration):
			self.currentVelocity[0] = self.targetVelocity[0]
			self.currentVelocity[1] = self.targetVelocity[1]
			return

		# Else, divide the distance vector by the hypotenuse (to make unit vector), multiply by maxAcceleration, and add to currentVelocity
		differenceVector[0] = self.maxAcceleration * (differenceVector[0] / differenceMagnitude)
		differenceVector[1] = self.maxAcceleration * (differenceVector[1] / differenceMagnitude)

		self.currentVelocity[0] += differenceVector[0]
		self.currentVelocity[1] += differenceVector[1]

		return
	
	def setPosition(self, x, y):
		"""
		Sets the position of the rect

		arg x - the x position to move to
		arg y - the y position to move to
		"""

		self.rect.left = x
		self.rect.top = y
	
	def _setImage(self):
		"""
		This should be overridden by the extending methods. This on it's own will 
		display a non-texture
		"""

		self.image = pygame.image.load("resources/intro_ball.gif")
		self.rect = self.image.get_rect()


