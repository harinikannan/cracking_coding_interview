class Node:

	nextNode = None #of type Node
	data = 0 #data for Node

	def __init__(self,nn, d):
		self.nextNode = nn
		self.data = d

	def appendNodeToTail(self, n):
		curr = self
		while(curr.nextNode != None):
			curr = curr.nextNode

		curr.nextNode = n
		#must guarantee that the last one is null
		n.nextNode = None


	def delNode(self, n):
		curr = self
		while(curr.nextNode !=n and curr.nextNode != None):
			curr = curr.nextNode
		if(curr.nextNode == n):
			nn = curr.nextNode.nextNode
			curr.nextNode = nn

	def printList(self):
		count = 0
		curr = self
		while(curr.nextNode!=None):
			print ("\n Node " +str(count) + " in linked list contains data: " + str(curr.data))
			count += 1
			curr = curr.nextNode;
		#for final node	
		print("\n Node " +str(count) + " in linked list contains data: " +str(curr.data))

	def insertAfter(self, n, toInsert):
		curr = self
		while(curr.nextNode!=n  and curr.nextNode!=None):
			curr = curr.nextNode

		curr = curr.nextNode #get current node to equal n
		if(curr == n):
			temp_Node = curr.nextNode
			curr.nextNode = toInsert
			toInsert.nextNode = temp_Node
 
		if(curr.nextNode == None):
			curr.nextNode = toInsert

if __name__ == "__main__":
	head = Node(None, 0)
	n1 = Node(None, 1)
	n2 = Node(None, 2)
	n3 = Node(None, 3)
	n4 = Node(None, 4)

	head.nextNode = n1
	head.appendNodeToTail(n2)
	head.appendNodeToTail(n4)
	#head.printList()
	head.insertAfter(n2, n3)

	head.printList()



