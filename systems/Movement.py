
import pygame
import systems.System as System

class Movement(System.System):
	def __init__(self):
		System.System.__init__(self)
		self.dependencies = ["Position","Velocity"]

	def update(self, componentManager, entities):
		"""
		Grabs the velocity data, adds it to the position data, and saves 
		to move the position every tick

		param componentManager - the componentManager containing all component data
		"""
		for entityID in entities:
			positionData = componentManager.get("Position", entityID)
			velocityData = componentManager.get("Velocity", entityID)

			componentManager.set("Position", entityID, "x", positionData["x"] + velocityData["x"])
			componentManager.set("Position", entityID, "y", positionData["y"] + velocityData["y"])
		
