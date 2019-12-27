# ship class 

class Ship():

	def __init__(self, ai_settings, screen):
		self.screen = screen

		# Load the image for the ship
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#import the settings from the settings module
		self.ai_settings = ai_settings

		# start the. ship at the bottom centre of the screen
		self.rect.center = self.screen.center
		self.rect.bottom = self.screem.bottom

		#Movement Flag for right side movement 
		self.moving_right = False	

		#Movement flag for the. left side movement 
		self.moving_left = False

		#store the decimal value for the ships center 
		self.center = float (self.rect.centerx)

	def blitme(self)
		""Draw the ship at the center location""
		self.screen.blit(self.image, self_rect)

	def update(self)
		""update the ships position based on the movement Flag""
		if self.moving_right and self_rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor 
		if self.moving_left and self.rect.left > 0 :
			self.center -= self.ai_settings.ship_speed_factor 
		self.rect.centerx = self.center
				

			
