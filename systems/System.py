class System():
	def __init__(self):
		self.dependencies = [""]

	def prep(self, entityID, componentManager):
		"""
		Determines if an entity has the requisite components to run this system 
		based on its dependencies. 

		# TODO - move to SystemManager? We don't need to redefine this each time. 
		# If needed, we can have a base function that by default returns true but 
		# can be defined on a system by system basis to check other prerequisites. 
		
		param entityID - the entity to check
		param componentManager - componentManager holding all entity-component 
		references
		
		Returns true if dependencies are met, false otherwise.
		"""

		entityComponents = componentManager.entities[entityID]
		for dependency in self.dependencies:
			if dependency not in entityComponents:
				return False

		return True

	def load(self, entityID, componentManager):
		"""
		The base 'load' function. Overloaded by subclasses to perform actions. 
		Otherwise does nothing.
		"""
		
		return

	def update(self):
		"""
		The base 'update' function. Overloaded by subclasses to perform actions.
		Otherwise does nothing.
		"""
		return