from singly_linkedlist import *

def removeDups(self):
	temp_buf = []

	curr = self
	while(curr.nextNode != None):

		if(temp_buf.count(curr.data) >= 1):
			self.delNode(curr)
		else:
			temp_buf.append(curr.data)

		curr = curr.nextNode

	if(temp_buf.count(curr.data) >= 1):
			self.delNode(curr)

def kthtolast(self,k):
	count = 0
	curr = self

	while(curr.nextNode != None):
		count+=1
		curr = curr.nextNode

	if(k == 0):
		print ("Node at "+str(k)+"th to last element has data: "+ str(curr.data))

	else:
		count+=1
		ktolast = count -k

		count = 0
		curr = self
		while(curr.nextNode !=None):
			if(count == ktolast):
				print ("Node at "+str(k)+"th to last element has data: "+ str(curr.data))
			count+=1
			curr = curr.nextNode

def delMid(n):
	#we are not given the head of the linked list, just the node itself
	#therefore, we can not "delete" the node by changing the prev node's pointers
	#we can only COPY the next node's stuff into this node

	nextN = n.nextNode
	n.data = nextN.data
	n.nextNode = nextN.nextNode

def partition(self,x):
	lessX_head = Node(None, None)
	greatX_head = Node(None, None)
	lessXlast = lessX_head
	greatXlast = greatX_head

	curr = self
	while(curr!=None):
		temp_next = curr.nextNode

		if(lessX_head.data != None and curr.data < x):
			lessX_head.appendNodeToTail(curr)
			lessXlast = curr

		if (lessX_head.data == None and curr.data < x):
			lessX_head.data = curr.data

		if(greatX_head.data != None and curr.data >= x):
			greatX_head.appendNodeToTail(curr)
			greatXlast = curr

		if(greatX_head.data == None and curr.data >= x):
			greatX_head.data = curr.data

		
		curr = temp_next

	lessX_head.printList()
	greatX_head.printList()
	#lessXlast.nextNode = greatX_head

	#return lessX_head

def reverseString(s):
	newStr = ""
	for i in range(len(s)-1, -1, -1):
		newStr += s[i]
	return newStr

def stringToLL(s):
	l = []
	for i in range(len(s)):
		n = Node(None, int(s[i]))
		l.append(n)

	for i in range(len(l)):
		if (i==len(l)-1):
			l[i].nextNode = None
		else:
			l[i].nextNode = l[i+1]

	return l[0]

def addNums(l1, l2):
	curr1 = l1
	str1 = ""
	while(curr1 != None):
		str1 += str(curr1.data)
		curr1 = curr1.nextNode

	curr2 = l2
	str2 = ""
	while(curr2 != None):
		str2 +=str(curr2.data)
		curr2 = curr2.nextNode

	str1 = reverseString(str1)
	str2 = reverseString(str2)

	summation = int(str1) + int(str2)
	str_sum = reverseString(str(summation))

	ll = stringToLL(str_sum)
	return ll

def circular(self):
	track = []
	curr = self
	while(track.count(curr) < 1):
		track.append(curr)
		curr = curr.nextNode

	return curr

def ispalindrome(self):
	org_str = ""
	reverse = ""
	curr = self

	while(curr!=None):
		org_str+= str(curr.data)
		curr = curr.nextNode

	reverse = reverseString(org_str)

	return org_str == reverse

if __name__ == "__main__":
	head = Node(None, 0)
	n2 = Node(None, 2)
	n3 = Node(None, 3)
	n4 = Node(None, 4)
	n1 = Node(None, 1)

	#print("n1 next node: "+str(n1.nextNode.data))

	head.appendNodeToTail(n1)
	head.appendNodeToTail(n2)
	head.appendNodeToTail(n3)
	head.appendNodeToTail(n4)
	
	#head.nextNode = n1
	#n1.nextNode = n2
	#n2.nextNode = n3
	#n3.nextNode = n4
	#n4.nextNode = n2


	#new_ll = partition(head, 2)

	#removeDups(head)
	#kthtolast(head, 0)

	#new_ll.printList()
	a4 = Node(None, 0)
	a3 = Node(a4, 2)
	a2 = Node(a3, 3)
	a1 = Node(a2, 0)

	ll = addNums(a1, a3)
	#ll.printList()

	#n = circular(head)
	#print("n's data: "+str(n.data))

	print ispalindrome(a1)
