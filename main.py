# import classes.Game as Game
import entities.EntityManager as EntityManager
import components.ComponentManager as ComponentManager
# import components.DebugNameComponentManager as DebugNameComponentManager

def main():
	""" 
	The main method. Handles initial startup arguments and sets up the game 
	object

	"""

	entityManager = EntityManager.EntityManager()
	componentManager = ComponentManager.ComponentManager()
	# TODO - create a massive JSON file with data on all entities, including base components and default values
	createPlayer(entityManager, componentManager)



	# TODO - configuration file loading
	# game = Game.Game()
	# game.startGame()

def createEntity(entityManager, componentManager, json):
	

def createPlayer(entityManager, componentManager):
	playerID = entityManager.create()
	componentManager.create(playerID, "Debug")
	componentManager.create(playerID, "Position")
	componentManager.set(playerID, "Debug", "DebugName", "PLAYER")
	print(componentManager.get(playerID, "Debug", "DebugName"))
	print(componentManager.get(playerID, "Position", ))
	# components['DebugNameComponentManager'].setDebugName(player, 'PLAYER')

def loadComponents():
	"""Loads all component managers into a single struct for ease of passing"""

	# TODO - put this in a ComponentManager straight up


	components = {}
	components["DebugNameComponentManager"] = DebugNameComponentManager.DebugNameComponentManager()
	return components
main() 
