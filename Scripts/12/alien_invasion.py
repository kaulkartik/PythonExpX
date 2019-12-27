import sys

import pygame 
from settings import settings 


def run_game():
	# initiate the pygame object
	pygame.init()

	# initalise the settings object 
	ai_settings = Settings ()


	screen = pygame.display.set_mode(ai_settings.screen_width, ai_settings.screen_height)
	pygame.display.set_caption('games-1')

	# declaring the bg_color variable
	bg_color = (230 , 230, 230)

	#declaring your battle ship
	ship = ship (ai_settings, screen)

	# start the while loop to initialise the game execution
	while True:

		# setting the background color 
		screen.fill(ai_settings.bg_color)
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings, screen, ship)

run_game()	


def check_events(ship)	
	# watch for the keyboard and the mouse events 
	for event in  pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.type == pygame.K_RIGHT:
				ship.moving_right = True
			elif event.type == pygame.K_LEFT
				ship.moving_left = True	
				
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False
			elif event.key == pygame.K_LEFT
				ship.moving_left = False	
				

def update_screen(ai_settings, screen, ship)
	# update the images on the screen according to the game 	
	# initiating your ship in the game 
	ship.blitme()
	# make most recently drawn screen visible 
	pygame.display.flip()






