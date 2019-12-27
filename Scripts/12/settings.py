# this class will store all the settings required for the alien
# invasion game . any new settings or the chnage in the settings
# will be handled in this class 

class Settings():
	""Initialise the game settings for aliens invasion game "

	 self.ship_speed_factor = 1.5

	def __init__(self):
		self.screen_width=1000
		self.screen_height=800
		self.bg_color=(0, 255, 0)
