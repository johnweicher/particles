from	core.geometry import Point

# Node object for implementing a linked list
class Node(object):

	def __init__(self, obj, next=None, prev=None):
		self.obj = obj
		self.next = next
		self.prev = prev
		
	def set_object(self, obj):
		self.obj = obj
		
	def get_object(self, obj):
		return self.obj
		
	def __str__(self):
		return str(self.obj)
		
		

class Universe(object):

	def __init__(self, x, y, z, w, h):
		self.x = x
		self.y = y
		self.z = z
		self.w = w
		self.h = h
		self.head = None
		self.tail = None
		self.cnt = 0
		
	def __str__(self):
		return "Universe (" + str(id(self)) + ") has " + str(self.cnt) + " objects, " + "head=" + str(id(self.head)) + ", tail=" + str(id(self.tail)) 

	
	def get_draw_coords(self, p=Point(0,0)):
		# quick check for div by zero potential and just return point if so
		if self.x == 0 or self.y == 0:
			return p
		else:
			dX = self.w * ( (p.x - ((self.x/2)*-1)) / self.x )
			dY = self.h * ( (p.y - ((self.y/2)*-1)) / self.y )
			return Point(round(dX), round(dY))
			
	def get_draw_coord_x(self, x):
		# quick check for div by zero potential and just return coord if so
		if self.x == 0: 
			return x
		else:
			return round(self.w * ( (x - ((self.x/2)*-1)) / self.x ))

	def get_draw_coord_y(self, y):
		# quick check for div by zero potential and just return coord if so
		if self.y == 0:
			return y
		else:
			return round(self.h * ( (y - ((self.y/2)*-1)) / self.y ))
	
		
	def list_objects(self):
		s = ""
		crnt = self.head
		while crnt != None:
			s = s + str(crnt) + "\n"
			crnt = crnt.next
		return s
		
		
		
	# methods for maintaining a linked-list of Nodes to track all entities in the universe
	def append(self, obj):
		
		# first Node in the LL
		if self.head == None:
			n = Node(obj)
			self.head = n
		elif self.cnt == 1:
			n = Node(obj, None, self.head)
			self.head.next = n
			self.tail = n
		# not first node, add to the end of the list
		else:
			n = Node(obj, None, self.tail)
			self.tail.next = n
			self.tail = n
			
		self.cnt += 1
		
	def delete_obj(self, obj):
	
		# LL is empty, invalid delete request
		if self.head == None:
			return
		else:
			# start at head of list, loop until we're at the end
			crnt = self.head
			while crnt != None:
				
				# check if object the one requested for delete
				if crnt.obj is obj:
				
					# only one object in the LL
					if self.head is self.tail:
						self.head = None
						self.tail = None
						crnt = None
					# deleting head, LL has multiple object already
					elif self.head is crnt:
						self.head.next.prev = None
						self.head = self.head.next
						crnt = None
					# deleting anywhere else in the LL
					else:
						crnt.prev.next = crnt.next
						# if deleting node is not already the tail
						if crnt.next != None:
							crnt.next.prev = crnt.prev
						else:
							self.tail = crnt.prev
						crnt = None
				# advance to next object in LL
				else:
					crnt = crnt.next
			self.cnt -= 1
			
			
	def delete_node(self, node):
	
		# LL is empty, invalid delete request
		if self.head == None:
			return
		else:
			# start at head of list, loop until we're at the end
			crnt = self.head
			while crnt != None:
				
				# check if object the one requested for delete
				if crnt is node:
				
					# only one object in the LL
					if self.head is self.tail:
						self.head = None
						self.tail = None
						crnt = None
					# deleting head, LL has multiple object already
					elif self.head is crnt:
						self.head.next.prev = None
						self.head = self.head.next
						crnt = None
					# deleting anywhere else in the LL
					else:
						crnt.prev.next = crnt.next
						# if deleting node is not already the tail
						if crnt.next != None:
							crnt.next.prev = crnt.prev
						else:
							self.tail = crnt.prev
						crnt = None
				# advance to next object in LL
				else:
					crnt = crnt.next
			self.cnt -= 1
			
	def draw(self, win):
		crnt = self.head
		while crnt != None:
			crnt.obj.draw(win, self)
			crnt = crnt.next
			
	def update(self):
		crnt = self.head
		while crnt != None:
			crnt.obj.update(self)
			crnt = crnt.next
		




		