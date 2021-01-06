#ListNode.py

class ListNode:

	def __init__(self, initValue, initNext):
	
	# post: constructs a new element with object initValue,
	# followed by next element
		self.value = initValue
		self.next_node = initNext
	

	#def ListNode (Object initValue):
	# post: constructs a new element with object initValue,
	# followed by a reference to null
	#	__init__(initValue, null);
	

	def get_value(self):
	# post: returns value associated with this element
		return self.value
	

	def get_next(self):
	# post: returns reference to next value in list
		return self.next_node
	

	def set_value(self, theNewValue):
		self.value = theNewValue
	

	def set_next(self, theNewNext):
	# post: sets reference to new next value
		self.next_node = theNewNext
	
