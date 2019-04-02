import classes.IEntity as IEntity
import classes.enums as enum


class ICharacter(IEntity.IEntity):
	def __init__(self):
		IEntity.IEntity.__init__(self)

		self.isAlive = True # Should this be updated on each turn?
		self.isAnimated = True # Should this be checked for animations?
		self.isDamagable = True # This entity can be damaged by attacking

		self.isCollidable = True # Can a user, monster, or item go in this spot?
		self.isInteractable = True # Can a user interact with this item?
		self.isKillable = True # Will this object be destroyed when health drops below 0?

		self.health = 1 # An entity's health. It will be destroyed if health < 0

		self.interactText = "Some strange being. You can't seem to tell what it is."

		self.moveSpeed = 3

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

	

	def act(self):
		"""
		Instructs the Character to act in some way. Move to NPCs?
		"""
		return

