import components.Components as Components

class ComponentManager():
	def __init__(self):
		
		# A list of ALL components and their contruction methods
		# Load in from JSON file?
		self.loadedComponents = {
			"Animation":Components.Animation,
			"Debug":Components.Debug,
			"Position":Components.Position,
			"Velocity":Components.Velocity,
			"Sprite":Components.Sprite,
		}

		# A struct to contain all entity keys and what components they have
		self.entities = {}

		# A struct containing all of the component data.
		self.components = {}

		return

	def alive(self, entityID):
		""" 
		Returns true if this entity is 'alive'. False otherwise
		
		param entityID - the entity to check for

		Returns a boolean
		"""
		return entityID in self.entities

	def create(self, entityID, component):
		"""
		Creates a new component for the given entity id

		param entityID - the id of the entity we're creating 
		param component - the component to add to the entity
		"""
		# componentString = component + "." + component + "()"
		if not self.alive(entityID):
			self.entities[entityID] = []

		# Catch case where this was already created
		if component in self.entities[entityID]:
			return

		# Adds the component to the entity's list of components
		self.entities[entityID].append(component)
		
		# Initializes a component struct if one doesn't exist already
		if component not in self.components:
			self.components[component] = {}
		
		# Initializes the entity's component data
		self.components[component][entityID] = self.loadedComponents[component]()
		return

	def destroy(self, entityID):
		"""
		Clears out all data for the given entity permanently

		param entityID - the id of the entity to remove
		"""
		# Removes the entity from the entities list
		entity = self.entities.pop(entityID)

		# Clears out entity data from all components the entity had 
		for component in entity['components']:
			self.components[component].pop(entityID)

	def get(self, component, entityID=None, field=None):
		"""
		Returns either the component, full value of the component for a given entity, 
		or a specific field's value

		param component - the component we're pulling fata for. 
		param entityID - the entity we're pulling data for
		param field - the specific field from the component we're pulling

		returns None if no values are found, or the struct or value found within 
		the component
		"""

		# Base case. Exit if the entity doesn't exist or component isn't used
		if component not in self.components:
			return {}

		elif entityID == None:
			return self.components[component]

		elif entityID not in self.components[component]:
			return None

		# Field isn't set, so return all component fields
		elif field == None:
			return self.components[component][entityID]

		# A field is set, so return it if it exists
		if field not in self.components[component][entityID]:
			return None
		return self.components[component][entityID][field]

	def set(self, component, entityID, field, value):
		"""
		Set the value of a field for an entity, component, and field

		param component - the component to set the value in
		param entityID - the id of the entity to set the value for
		param field - the field within the component to set
		param value - the value to insert into the component
		"""
		if (
			component not in self.components or 
			entityID not in self.components[component]
		):
			return
			
		self.components[component][entityID][field] = value
