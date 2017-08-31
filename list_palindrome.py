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
		while(current):
			successor, current.next, predecessor, current = current.next, predecessor, current, successor
		self.head = predecessor

		node = self.head
		while(node):
			print(node.val)
			node = node.next

		return


if __name__ == '__main__':
	linkedlist = LinkedList()
	linkedlist.insert(1)
	linkedlist.insert(2)
	linkedlist.insert(3)
	linkedlist.insert(4)
	linkedlist.print_all()
	linkedlist.reverse_list() 
