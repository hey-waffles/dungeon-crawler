import math 

def scalarToVector(magnitude, angle):
	""" 
	Converts a speed and vector into a vector array [x, y, z] 
	X is horizontal magnitude, Y is vertical magnitude, and Z is magnitude in/out of screen

	arg magnitude - the magnitude of the vector
	arg angle - the direction in radians of the vector

	Returns an array with the x, y, z vector 
	"""
	# We leave z blank for now, since we don't use it
	# In the future, add functionality for two angles
	return [math.cos(angle) * magnitude, math.sin(angle) * magnitude, 0]

def subtractVectors(v1, v2):
	"""
	Subtracts a vector (v2) from another vector (v1) such that v3 = v1 - v2

	arg v1 - the vector to subtract from
	arg v2 - the vector to subtract 

	Returns a resultant vector
	"""

	v3 = [
		v1[0] - v2[0],
		v1[1] - v[1]
	]

	return v3