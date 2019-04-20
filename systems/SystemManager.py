import systems.Render as Render

class SystemManager():
	def __init__(self, entityManager, componentManager):
		self.entityManager = entityManager
		self.componentManager = componentManager
		self.systems = {
			"Render":Render.Render()
		}
		self.systemOrder = [
			"Render"
		]
		return

	def load(self, entityID):
		"""
		Runs all logic to load an Entity to completion that cannot be done by JSON alone
		"""
		for system in self.systemOrder:
			self.systems[system].load(entityID, self.componentManager)
		return
	
	def update(self):
		"""
		The update action to be run once per tick
		"""
		for system in self.systemOrder:
			self.systems[system].update(self.componentManager)
		return