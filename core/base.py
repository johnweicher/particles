
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
		
	def delete_obj(self, obj):
	
		# LL is empty, invalid delete request
		if self.head == None:
			return
		else
			# start at head of list, loop until we're at the end
			crnt = head
			while crnt != None:
				
				# check if object the one requested for delete
				if crnt.obj is obj:
				
					# only one object in the LL
					if head is tail
						head = None
						tail = None
						crnt = None
					# deleting head, LL has multiple object already
					elif head is crnt:
						head.next.prev = None
						head = head.next
						crnt = None
					# deleting anywhere else in the LL
					else
						crnt.prev.next = crnt.next
						# if deleting node is not already the tail
						if crnt.next != None
							crnt.next.prev = crnt.prev
						else
							tail = crnt.prev
						crnt = None
				# advance to next object in LL
				else
					crnt = crnt.next
			
			
	def delete_node(self, node):
	
		# LL is empty, invalid delete request
		if self.head == None:
			return
		else
			# start at head of list, loop until we're at the end
			crnt = head
			while crnt != None:
				
				# check if object the one requested for delete
				if crnt is node:
				
					# only one object in the LL
					if head is tail
						head = None
						tail = None
						crnt = None
					# deleting head, LL has multiple object already
					elif head is crnt:
						head.next.prev = None
						head = head.next
						crnt = None
					# deleting anywhere else in the LL
					else
						crnt.prev.next = crnt.next
						# if deleting node is not already the tail
						if crnt.next != None
							crnt.next.prev = crnt.prev
						else
							tail = crnt.prev
						crnt = None
				# advance to next object in LL
				else
					crnt = crnt.next
					
	def draw(self, win):
		crnt = head
		while crnt != None:
			crnt.obj.draw(win)
			crnt = crnt.next
			
	def update(self):
		crnt = head
		while crnt != None:
			crnt.obj.update()
			crnt = crnt.next
		
		