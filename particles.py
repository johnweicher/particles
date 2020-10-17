import pygame
import math
from core.base import *
from core.geometry import *

pygame.init()

winWidth = 1500
winHeight = 1000

univ = Universe(15000, 10000, 0, winWidth, winHeight)
print("Created Universe....")
print(univ)

# Set up a sample scene
p = ForceParticle(Point(50, 50), Vector(1,5), 6, 1000)
p2 = ForceParticle(Point(950, 950), Vector(-1,-2), 6, 1000)
univ.append(p)
univ.append(p2)
print(univ.list_objects())



def redrawWindow():
	win.fill((0,0,0))
	univ.draw(win)
	pygame.display.update()


# Main loop
win = pygame.display.set_mode((winWidth,winHeight));
clock = pygame.time.Clock()

run = True
while run:
	clock.tick(30)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	# Ask the universe to update all objects
	univ.update()

	# Redraw the scene
	redrawWindow()
	


# Broke main loop, cleanup			
pygame.quit()




