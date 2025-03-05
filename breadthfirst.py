def breadthFirst(root):
	myQueue = []
	myQueue.append(root):
		while len(myQueue) != 0:
			headOfQueue = myQueue.pop(0)
			children = headOfQueue.getChildren()
			if len(children) != 0:
				for i in range(0,len(children)-1):
					myQueue.append(children[i])
					next i
			print(headOfQueue.getValue())
			
