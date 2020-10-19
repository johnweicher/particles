import pygame
import math
from core.base import *
from core.geometry import *

pygame.init()

winWidth = 1500
winHeight = 1000

univ = Universe(3000, 2000, 0, winWidth, winHeight)
print("Created Universe....")
print(univ)

# Set up a sample scene
p = ForceParticle(Point(-550, 550), 1, 5, Vector(1,-2), 10, 2500, Color(255,0,0))
p2 = ForceParticle(Point(550, -550), 1, 16, Vector(-1,2), 10, 2500, Color(0, 255, 0))
p3 = ForceParticle(Point(-350, 650), 1, 5, Vector(1,-6), 6, 2500, Color(0, 0, 255))
p4 = ForceParticle(Point(50, -950), 1, 6, Vector(-1,8), 6, 2500, Color(255, 255, 0))
p5= ForceParticle(Point(-750, 0), 1, 5, Vector(1,-6), 6, 2500, Color(255, 0, 255))
p6 = ForceParticle(Point(500, -650), 1, 6, Vector(-1,8), 6, 2500, Color(0, 255, 255))
univ.append(p)
univ.append(p2)
univ.append(p3)
univ.append(p4)
univ.append(p5)
univ.append(p6)
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




