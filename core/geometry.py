import pygame
import pygame.gfxdraw
import math

# Simple vector class
class Vector(object):

	def __init__(self, x, y, m=0):
		self.x = x
		self.y = y
		
		# If magnitude is passed, use it, otherwise try to derive a magnitude
		#  derive from directional components.  Override resulting 0 with 1.
		if m == 0:
			m = math.sqrt((self.x*self.x)+(self.y*self.y))
			if m == 0:
				m = 1
			self.mag = m
		else:
			self.mag = m
		
		# Always auto-normalize directional components to a unit vector
		norm = math.sqrt((self.x*self.x)+(self.y*self.y))
		if norm == 0:
			norm = 1
		self.x = self.x / norm
		self.y = self.y / norm
		
	def __str__(self):
		return "Vector(" + str(self.x) + "," + str(self.y) + ", mag=" + str(self.mag) + ")"
	
	# Function for re-applying normalization to unit vector.
	#  Checks that we don't have a zero-mag vector to avoid div by zero
	def normalize(self):
		if self.x != 0 or self.y != 0:
			self.mag = math.sqrt((self.x*self.x)+(self.y*self.y))
			self.x = self.x / self.mag
			self.y = self.y / self.mag
	
	def duplicate(self):
		return Vector(self.x, self.y, self.mag)
		

# Simple RGB Color container
class Color(object):
	def __init__(self, r=255, g=255, b=255):
		self.r = r
		self.g = g
		self.b = b

# Simple point class for storing a coordinates as a tuple object
class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __str__(self):
		return "Point(" + str(self.x) + "," + str(self.y) + ")"

	# Returns a copy of itself to protect own content
	def get_position(self):
		return Point(self.x, self.y)
	
	# Adds/moves a point by a vector (assumes unit vector)
	def add_vector(self, v):
		self.x += (v.x * v.m)
		self.y += (v.y * v.m)
		
	def draw(self, win):
		pygame.gfxdraw.filled_circle(win, self.x, self.y, 3, (255,0,0))
		

		
class MassPoint(Point):
	
	def __init__(self, x, y, m=1):
		super().__init__(x, y)
		self.m = m
		
	def __str__(self):
		return "MassPoint(" + str(self.x) + "," + str(self.y) + "), mass=" + str(self.m)
		

class Particle(Point):

	def __init__(self, p=Point(0,0), mass=0, radius=1, v=Vector(0,0)):
		self.p = p
		self.v = v
		self.m = mass
		self.rad = radius
		
	def __str__(self):
		return "Particle( \n\t" + str(self.p) + ", \n\t" + "mass = " + str(self.m) + ", \n\t" + "radius = " + str(self.r) + ", \n\t" + str(self.v) + "\n)"
	
	
class ForceParticle(Particle):
	
	def __init__(self, p=Point(0,0), mass=0, radius=1, v=Vector(0,0), force=0, range=0, color=Color(255,255,255)):
		super().__init__(p, mass, radius, v)
		self.f = force
		self.r = range
		self.c = color
		
	def __str__(self):
		return "ForceParticle( \n\t" + str(self.p) + ", \n\t" + str(self.v) + ", \n\t force=" + str(self.f) + "\n)"
	

	def update(self, univ):
	

		
		
		# Check edge cases if necessary to handle a wall bounce
		if (self.v.x > 0) and (self.p.x + (self.v.x*self.v.mag)) >= (univ.x/2):
			self.v.x *= -1
			self.v.mag *= .75
		if (self.v.x < 0) and (self.p.x + (self.v.x*self.v.mag)) <= -(univ.x/2):
			self.v.x *= -1
			self.v.mag *= .75
		if (self.v.y > 0) and (self.p.y + (self.v.y*self.v.mag)) >= (univ.y/2): 	
			self.v.y *= -1
			self.v.mag *= .75
		if (self.v.y < 0) and (self.p.y + (self.v.y*self.v.mag)) <= -(univ.y/2):			
			self.v.y *= -1
			self.v.mag *= .75
		
		
		
		# general approach:
		#	1. iterate through all other objects in the universe
		#	2. check if they are closer than the range of any affects
		#	3. compute the affect on own vector
		crnt = univ.head
		amDeleted = False
		while crnt != None:
			if crnt.obj is not self:
			
				if isinstance(crnt.obj, ForceParticle) == True:
				
					# For now, only for ForceParticles, but need better class hierarchy
					# Make more organized/universal in when this is applied
					
					# If position of sibling is within my own radius,
					# Create new merge particle, add to Universe, delete self and sibling
		
					p = crnt.obj.p
					f = crnt.obj.f
					r = crnt.obj.r
					dist = math.sqrt( math.pow((self.p.x - p.x),2) + math.pow((self.p.y - p.y),2) )
					
					# If close enough to merge
					if dist <= self.rad:
						newX = (self.p.x + p.x)/2
						newY = (self.p.y + p.y)/2
						newMass = (self.m + crnt.obj.m)
						
						area_self = math.pi * (self.rad * self.rad)
						area_othr = math.pi * (crnt.obj.rad * crnt.obj.rad)
						newRadius = math.sqrt( (area_self + area_othr)/math.pi )
						
						newV = Vector((self.v.x * self.v.mag) + (crnt.obj.v.x * crnt.obj.v.mag), (self.v.y * self.v.mag) + (crnt.obj.v.y * crnt.obj.v.mag))
						newForce = (self.f + f)
						newRange = (self.r + r)/2
						newColor = Color( round((self.c.r + crnt.obj.c.r)/2), round((self.c.g + crnt.obj.c.g)/2), round((self.c.b + crnt.obj.c.b)/2))
					
						univ.append( ForceParticle( Point(newX, newY), newMass, newRadius, newV, newForce, newRange, newColor) )
						
						univ.delete_obj(crnt.obj)
						univ.delete_obj(self)
						return

					# If close enough to affect
					elif dist <= r:
						Vf = Vector((p.x - self.p.x), (p.y - self.p.y ), f * (1 - (dist/r)) )
						Vf.normalize()
						self.v.x = (self.v.x * self.v.mag) + (Vf.x * Vf.mag)
						self.v.y = (self.v.y * self.v.mag) + (Vf.y * Vf.mag)
						self.v.mag = math.sqrt((self.v.x*self.v.x)+(self.v.y*self.v.y))
						self.v.normalize()
						
			# Update own position by current vector
			if amDeleted == False:
				self.p.x = round(self.p.x + (self.v.x*self.v.mag)) 
				self.p.y = round(self.p.y + (self.v.y*self.v.mag))
				# Dampen Velocity over time
				#self.v.mag *= .9
				
			
			
			
			crnt = crnt.next
		
		
	def draw(self, win, univ):
		#pygame.gfxdraw.filled_circle(win, self.p.x, self.p.y, 3, (255,0,0))
		#pygame.gfxdraw.circle(win,self.p.x, self.p.y, self.r, (255,0,0))
		#pygame.draw.line(win, (255,0,0), (self.p.x, self.p.y), (round(self.p.x + (self.v.x*20)), round(self.p.y + (self.v.y*20))) )
		dX = univ.get_draw_coord_x(self.p.x)
		dY = univ.get_draw_coord_y(self.p.y)
		
		scaleX = (univ.x / univ.w)
		scaleY = (univ.y / univ.h)
		scale = min(scaleX, scaleY)
		
		pygame.gfxdraw.filled_circle(win, dX, dY, round(self.rad / scale), (self.c.r,self.c.g,self.c.b))
		pygame.gfxdraw.circle(win,dX, dY, round(self.r / scale), (self.c.r,self.c.g,self.c.b))
		pygame.draw.line(win, (self.c.r,self.c.g,self.c.b), (dX, dY), (round(dX + (self.v.x*20)), round(dY + (self.v.y*20))) )
		
		
		