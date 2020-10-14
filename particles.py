import pygame
import pygame.gfxdraw
import math
from core.base import *
from core.geometry import *

pygame.init()

univ = Universe(1500, 1000)
print("Created Universe....")
print(univ)

p = Particle( Point(50, 50), Vector(2, 4) )

print(p)




