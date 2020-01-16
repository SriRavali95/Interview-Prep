# reverse linked list 

""" As the linked list doesn't have the pointer it should be done in the following way"""


def reverseLinkedList(head):
	# pointer for the previous node
	p1 = None 
	# pointer for the current node 
	p2 = head 
	# loop till the next node exists 
	while p2.next != None: 
		"""copy the instance of the next node to the p3
		   so that the refrence to next node is not lost while reversing"""
		p3 = p2.next 
		# Now the next node is present in p3, change the p2.next to previous node
		p2.next = p1 
		#Move the pointers accordingly 
		p1 = p2 
		p2 = p3
	# p1 will have the last node 
	return p1



 

