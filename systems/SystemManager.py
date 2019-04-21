import pygame 

import systems.Movement as Movement
import systems.Render as Render

class SystemManager():
	def __init__(self, entityManager, componentManager):
		# Holds the entityManager reference
		self.entityManager = entityManager 

		# Holds the componentManager reference
		self.componentManager = componentManager

		# Holds a list of all systems and the entities run for each 
		self.systemEntities = {}

		# All systems that can be used and their classes
		self.systems = {
			"Movement":Movement.Movement(),
			"Render":Render.Render()
		}

		# The order the systems are run in to prevent undefined behavior
		self.systemOrder = [
			"Movement",
			"Render"
		]

		# Initializes all systems with blank entity lists 
		for system in self.systemOrder:
			self.systemEntities[system] = []

		return

	def destroy(self, entityID):
		"""
		Runs the actions to completely remove this entity from everything

		param entityID - the entity to remove from the game
		"""

		# Removes all entityIDs from the systemEntities
		for system in self.systemOrder:
			self.systemEntities[system].remove(entityID)

		# Removes entity from component manager and entity manager both
		self.componentManager.destroy(entityID)
		self.entityManager.destroy(entityID)


	def load(self, entityID):
		"""
		Runs all logic to load an Entity to completion that cannot be done by 
		JSON alone

		param entityID - the specific entity to load
		"""

		# Loops through all systems
		for system in self.systemOrder:
			# Checks if this system can be run with the entity's components
			canRunSystem = self.systems[system].prep(entityID, self.componentManager)

			# If so, add to systemEntities for easy reference each tick
			if canRunSystem == True:
				self.systemEntities[system].append(entityID)
				self.systems[system].load(entityID, self.componentManager)

		return
	
	def update(self):
		"""
		The update action to be run once per tick
		"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		
		for system in self.systemOrder:
			self.systems[system].update(self.componentManager, self.systemEntities[system])
		return