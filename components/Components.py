# Contains all component struct contstructors
def Controllable():
	return {"Controllable":True}

def Debug():
	return {"DebugName":"%NO NAME%"}

def Loaded():
	return {"loaded":True}

def Position():
	return {"x":0, "y":0}

def Sprite():
	return {
		"sprite":None,  # The sprite image object, created by system load
		"spriteFilePath":"",  # Path to the image file
		"spriteRect":None, # The sprite rect for rendering the sprite
		"x":0, # The default x position of the rect on the sprite image
		"y":0, # The default y position of the rect on the sprite image
		"width":0, # The default width of the sprite image
		"height":0 # The default height of the sprite image
	}
