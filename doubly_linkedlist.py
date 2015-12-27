#A doubly linked list is sequential in which Head's prev points to null and tail's next node points to null

class Node:

	nextNode = None #of type Node
	prevNode = None
	data = 0 #data for Node

	def __init__(self,nn, pn, d):
		self.nextNode = nn
		self.prevNode = pn
		self.data = d

	def appendToTail(self, n):
		curr = self
		while(curr.nextNode != None):
			curr = curr.nextNode

		curr.nextNode = n
		curr.nextNode.prevNode = curr

	def delNode(self, n):
		curr = self
		while(curr.nextNode !=n and curr.nextNode != None):
			curr = curr.nextNode
		print("print list so far: \n")
		self.printListForward()
		print("curr Node's data is "+ str(curr.data))
		print("next Node's data is "+ str(curr.nextNode.data))
		if(curr.nextNode == n):
			nn = curr.nextNode.nextNode
			if(nn == None):
				curr.nextNode = None
			else:
				print("next NEXT Node's data is "+ str(curr.nextNode.nextNode.data))
				curr.nextNode = nn
				nn.prevNode = curr

	def printListForward(self):
		count = 0
		curr = self
		while(curr.nextNode!=None):
			print ("\n Node " +str(count) + " in linked list contains data: " + str(curr.data))
			count += 1
			curr = curr.nextNode;
		#for final node	
		print("\n Node " +str(count) + " in linked list contains data: " +str(curr.data))

	def printListBackward(self):
		count = 0
		curr = self
		while (curr.prevNode != None):
			print ("\n Node " +str(count) + " in linked list contains data: " + str(curr.data))
			count +=1
			curr = curr.prevNode
		#for final node	
		print("\n Node " +str(count) + " in linked list contains data: " +str(curr.data))

	def insertAfter(self, n, toInsert):
		curr = self
		while(curr.nextNode!= n and curr.nextNode!=None):
			curr = curr.nextNode

		curr = curr.nextNode #get current node to equal n
		if(curr == n):
			temp_Node = curr.nextNode
			curr.nextNode = toInsert
			toInsert.nextNode = temp_Node

			toInsert.prevNode = curr
			temp_Node.prevNode = toInsert
 
		if(curr.nextNode == None):
			curr.nextNode = toInsert
			toInsert.prevNode = curr

if __name__ == "__main__":
	head = Node(None, None, 0)
	n1 = Node(None, None, 1)
	n2 = Node(None, None, 2)
	n3 = Node(None, None, 3)
	n4 = Node(None, None, 4)

	head.appendToTail(n1)
	head.appendToTail(n2)
	head.appendToTail(n4)

	#head.printListForward()
	
	head.insertAfter(n2,n3)
	head.delNode(n4)
	
	head.printListForward()
	n3.printListBackward()

