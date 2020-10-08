
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
		
		

class Universe(object):

	def __init__(self, w, h, d=0):
		self.w = w
		self.h = h
		self.d = d
		self.head = None
		self.tail = None		
		
	# methods for maintaining a linked-list of Nodes to track all entities in the universe
	def append(self, obj):
		
		# first Node in the LL
		if head = None:
			self.head = Node(obj)
			self.tail = self.head

		# not first node, add to the end of the list
		else
			newNode = Node(obj, None, self.tail)
			self.tail.next = newNode
		
	def delete(self, obj):
	
			