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
			self.mag = mag
		
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
		

# Simple point class for storing a coordinates as a tuple object
class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	# Returns a copy of itself to protect own content
	def get_position(self):
		return Point(self.x, self.y)
		
	def __str__(self):
		return "Point(" + str(self.x) + "," + str(self.y) + ")"
		
class MassPoint(Point):
	
	def __init__(self, x, y, m=1):
		super().__init__(x, y)
		self.m = m
		
	def __str__(self):
		return "MassPoint(" + str(self.x) + "," + str(self.y) + "), mass=" + str(self.m)
		

class Particle(Point):

	def __init__(self, p=Point(0,0), v=Vector(0,0)):
		self.p = p
		self.v = v
		
	def __str__(self):
		return "Particle( \n\t" + str(self.p) + ", \n\t" + str(self.v) + "\n)"
	
	
	