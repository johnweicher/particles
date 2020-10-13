
# Simple vector class
class Vector(object):

	def __init__(self, x, y, mag=0):
		self.x = x
		self.y = y
		
		# If magnitude is passed, use it, otherwise derive from directional components
		if mag == 0:
			self.mag = math.sqrt((self.x*self.x)+(self.y*self.y))
		else:
			self.mag = mag
		
		# Always auto-normalize
		norm = math.sqrt((self.x*self.x)+(self.y*self.y))
		self.x = self.x / norm
		self.y = self.y / norm
		
	def normalize(self):
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
		
class MassPoint(Point):
	
	def __init__(self, x, y, m=1):
		super().__init__(x, y)
		self.m = m
		

# Universe needs an append and remove QUEUE list, so other entities like particles can request of the Universe to remove themselves and add newly joined particles.	