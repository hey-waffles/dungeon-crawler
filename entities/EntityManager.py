import entities.Entity as Entity

class EntityManager: 
	def __init__(self):
		self.entities = {} # A dict of all entities, with their ids as keys
		self.nextEntityID = 1 # Next entity id, to be incremented every entity created

		return

	def create(self):
		"""
		Creates a new entity and unique id and returns it
		"""
		entity = Entity.entity(self.nextEntityID)
		self.entities[self.nextEntityID] = entity
		self.nextEntityID = self.nextEntityID + 1

		return entity["entityID"]

	def alive(self, id):
		"""
		Returns true if the id exists and is alive. False otherwise
		"""
		return id in self.entities

	def erase(self, id):
		"""
		Removes a given id and entity from the entity manager
		"""
		if id not in self.entities:
			return

		self.entities.pop(id)
		


	
