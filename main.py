# import classes.Game as Game
import pygame

import entities.EntityManager as EntityManager
import components.ComponentManager as ComponentManager
import systems.SystemManager as SystemManager
# import components.DebugNameComponentManager as DebugNameComponentManager

def main():
	""" 
	The main method. Handles initial startup arguments and sets up the game 
	object

	"""

	entityManager = EntityManager.EntityManager()
	componentManager = ComponentManager.ComponentManager()
	systemManager = SystemManager.SystemManager(entityManager, componentManager)
	clock = pygame.time.Clock()

	# TODO - create a massive JSON file with data on all entities, including base components and default values
	createPlayer(entityManager, componentManager, systemManager)

	while(True):
		systemManager.update()
		clock.tick(30)

	input("Press the enter key to continue")

	# TODO - configuration file loading
	# game = Game.Game()
	# game.startGame()

# def createEntity(entityManager, componentManager, json):
	

def createPlayer(entityManager, componentManager, systemManager):
	playerID = entityManager.create()
	componentManager.create(playerID, "Debug")
	componentManager.create(playerID, "Position")
	componentManager.create(playerID, "Velocity")
	componentManager.create(playerID, "Sprite")
	componentManager.set("Debug", playerID, "name", "PLAYER")
	componentManager.set("Sprite", playerID, "spriteFilePath", "resources/waals_character.png")
	componentManager.set("Sprite", playerID, "width", 48)
	componentManager.set("Sprite", playerID, "height", 48)

	componentManager.set("Velocity", playerID, "x", 2)

	systemManager.load(playerID)
	# components['DebugNameComponentManager'].setDebugName(player, 'PLAYER')

main() 
