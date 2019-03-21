def getVelocity(speed, vector):
	""" 
	Converts a speed and vector into a velocity array [x, y, z] 
	X is horizontal movement, Y is vertical movement, and Z is movement in/out of screen

	arg speed - the speed scalar
	arg vector - the direction in radians that the object is moving in

	Returns an array with the x, y, z velocity 
	"""
	# We leave z blank for now, since we don't use it
	# In the future, add functionality for two angles
	return [math.cos(vector) * speed, math.sin(vector) * speed, 0]