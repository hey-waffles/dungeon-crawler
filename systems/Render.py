
import pygame
import systems.System as System

class Render(System.System):
	def __init__(self):
		System.System.__init__(self)
		self.dependecies = ["Position","Sprite"]

		self.screen = pygame.display.set_mode((720, 480))


	def load(self, entityID, componentManager):
		"""
		Loads the object's sprite into a usable image
		"""
		spriteData = componentManager.get("Sprite", entityID)

		# TODO - Check that the image exists. If not, load in a placeholder

		sprite = pygame.image.load(spriteData["spriteFilePath"])
		componentManager.set(entityID, "Sprite", "sprite", sprite)
		print(spriteData)
		rect = pygame.Rect(spriteData["x"], spriteData["y"], spriteData["width"], spriteData["height"])
		componentManager.set(entityID, "Sprite", "spriteRect", rect)

		return

	def update(self, componentManager):
		self.screen.fill((0,0,0))
		
		for entity in componentManager.get("Sprite"):
			spriteData = componentManager.get("Sprite", entity)
			positionData = componentManager.get("Position", entity)
			# Extract image
			sprite = spriteData["sprite"].subsurface(spriteData["spriteRect"])
			self.screen.blit(sprite, (positionData["x"], positionData["y"]))
		
		pygame.display.flip()

