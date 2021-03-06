class ListNode():
	def __init__(self, x):
		self.val = x
		self.next = None

class LinkedList():
	def __init__(self):
		self.head = None

	def insert(self, a):
		node = ListNode(a)
		if self.head == None:
			self.head = node
		else:
			node.next = self.head
			self.head = node

	def print_all(self):
		if self.head == None:
			print('No elements in the list')
		else:
			node = self.head
			while(node):
				print(node.val)
				node = node.next
		return

	def reverse_list(self):
		predecessor, current, successor = None, self.head, self.head
		# https://stackoverflow.com/a/8725769/6613065 
		# The right side operators are evaluated first,
		# so not good for variables that are both on rhs 
		# and lhs in a loop - Unless one is very careful. 
		# May be, I will get with practice
		while(current):
			successor = current.next
			current.next = predecessor
			predecessor = current
			current = successor
		self.head = predecessor

		node = self.head
		while(node):
			print(node.val)
			node = node.next

		return

	def reverse_recursion(self, node):
		if node.next == None:
			self.head = node
			return
		self.reverse_recursion(node.next)
		temp = node.next
		temp.next = node
		node.next = None


	def remove_dups(self):
		current = self.head
		while(current.next):
			if current.next.val == current.val:
				current.next = current.next.next
			else:
				current = current.next

if __name__ == '__main__':
	linkedlist = LinkedList()
	linkedlist.insert(1)
	linkedlist.insert(2)
	linkedlist.insert(3)
	linkedlist.insert(4)
	linkedlist.insert(4)
	linkedlist.insert(4)
	linkedlist.insert(4)
	linkedlist.insert(4)
	linkedlist.print_all()
	linkedlist.reverse_list() 
	linkedlist.reverse_recursion(linkedlist.head)
	linkedlist.print_all()
	linkedlist.remove_dups()
	linkedlist.print_all()
