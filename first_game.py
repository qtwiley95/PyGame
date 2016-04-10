#!/usr/bin/python

import sys, pygame
import time
pygame.init()


#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

size = width, height = 600, 600

screen = pygame.display.set_mode(size)

pygame.display.set_caption('slither')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))
font = pygame.font.Font(None, 36)



clock = pygame.time.Clock()

def play_game():
	gameExit = False
	lead_x = 300.0
	lead_y = 300.0
	lead_x_change = 0
	previous_x = [None] * 1000
	previous_y = [None] * 1000
	moveToggle = 0
	esc = False

	while not gameExit:


		for event in pygame.event.get():

			if(event.type == pygame.QUIT):
				esc = True

			if (esc == True):
				while(gameExit == False):
					message = font.render("You Lose! Press C to play again, Q to quit", 1, BLACK)
					screen.blit(message, (10, 180))
					pygame.display.update()
					for event in pygame.event.get():
						if event.type == pygame.KEYDOWN:
							if(event.key == pygame.K_c):
								play_game()
							elif(event.key == pygame.K_q):
								gameExit = True



		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				moveToggle = 1
			elif event.key == pygame.K_RIGHT:
				moveToggle = 2
			elif event.key == pygame.K_DOWN:
				moveToggle = 3
			elif event.key == pygame.K_UP:
				moveToggle = 4
			elif event.key == pygame.K_ESCAPE:
				esc = True

		if(moveToggle == 1):
			lead_x -= 4
		elif(moveToggle == 2):
			lead_x += 4
		elif(moveToggle == 3):
			lead_y +=4
		elif(moveToggle == 4):
			lead_y -=4

		if lead_x < 0:
			lead_x = 600
		elif lead_x > 600:
			lead_x = 0
		elif lead_y < 0:
			lead_y = 600
		elif lead_y > 600:
			lead_y = 0


		screen.fill((250, 250, 250))
		#print pygame.event
		pygame.draw.rect(screen, RED, [lead_x, lead_y, 10, 10])
		pygame.display.update()

		clock.tick(40)

play_game()

pygame.quit()
quit()
