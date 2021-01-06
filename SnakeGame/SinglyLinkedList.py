# SinglyLinkedList.py

from ListNode import ListNode
class SinglyLinkedList:

	def __init__(self):
		self.first = None
		self.last = None

	def get_first(self):
		if self.first == null:
			return None
		else:
			return self.first.get_value()

	def add_first(self, value):
		if self.first != None:
			self.first = ListNode(value, self.first)
		else:
			self.first = self.last = ListNode(value, None)

	def add_last(self, value):
		if self.first == None:
			self.first = self.last = ListNode(value, None)
		else:
			temp = ListNode(value, None)
			self.last.set_next(temp)
			self.last = temp

	def get_last(self):
		if self.last == None:
			return None
		else:
			return self.last.get_value()

	def size(self):
		count = 0

		temp = self.first
		while temp != None:
			count += 1
			temp = temp.get_next()

		return count

	def delete_last(self):
		list_size = self.size() 
		if list_size > 1:
			count = 0
			temp = self.first
			while count != list_size - 2:
				temp = temp.get_next()
				count += 1
			temp.set_next(None)
			self.last = temp

	def print_list(self):
		temp = self.first # starts at first node
		while temp != None:
			print(temp.get_value() + " ")
			temp = temp.get_next() # flush to next node
		print("\n\nNumber of elements: " + str(self.size()))