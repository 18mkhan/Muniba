class node:
	def __init__(self,value):
		self.__value = value
		self.__left = None
		self.__right= None
		
	def get_value(self,value):
		return self.__value
	def get_left(value):
		return self.__left
	def get_right(self):
		return self.__right
	def set_left(self):
		return self.__left = left
	def set_right(self):
		return self.__right = right

root = node(16)
A = node(5)
root.set_left(A)
B = node(2)
A.set_left(B)


class BST:
	def __init__(self,rootValue):
		self.__root = node(rootValue)


	def breadthFirst(self):
		q = []
		q.append(self.__root) # add the root
		while len(q) != 0: # while the queue is not empty
			current = q.pop(0) # remove from the queue
			if current.get_left() != None: # repeat until the queue is empty and print the value
				q.append(current.get_left())
			if current.get_right() != None:
				q.append(current.get_right())
			print(current.get_value())

	def postOrderTraversal(self):
		self.postOrderTraversalRecursive(self.__root)
		
	def postOrderTraversalRecursive(self,current):
		if current != None:
			self.postOrderTraversalRecursive(current.get_right())
			self.postOrderTraversalRecursive(current.get_left())
			print(current.get_value())
		
	def postInorderTraversal(self):
		self.postInorderTraversalRecursive(self.__root)
		
	def postInorderTraversalRecurisve(self,current):
		if current != None:
			self.postInorderTraversalRecurisve(current.get_left())
			print(current.get_value)
			self.postInorderTraversalRecurisve(current.get_right())
			
	def preOrderTraversal(self):
		self.preOrderTraversalRecursive(self.__root)
		
	def preOrderTraversalRecurisve(self,current):
		if current != None:
			print(current.get_value)
			self.preOrderTraversalRecurisve(current.get_left())
			self.preOorderTraversalRecurisve(current.get_right())
			
	def add(self,ValueToAdd):
		temp = node(ValueToAdd)
		current = self.__root
		previous = None
		while current != None:
			previous = current
# Transverse until current equals to none
		if ValueToAdd < current.get_value():
			current = current.get_left()
		if ValueToAdd >= current.get_value():
			current = current.get_Right()
#adds the value to either left if its less than previous value otherwise adds to right
		if valueToAdd < previous.get_value():
			previous.set_left(temp)
		else:
			previous.set_right(temp)

tree = BST(16)
tree.add(5)
tree.add(25)
tree.add(2)
tree.add(20)
tree.add(29)
tree.add(17)
tree.add(23)
tree.add(27)
tree.postOrderTraversal()
tree.postInorderTraversal()
tree.preOrderTraversal()D



