# finding loop and the element where it is 

""" Terminology: 
	L = Distance from head till the loop starts
	C = Distance from the loop starting to the coincidence of the first and second 
	R = Remaining from the coincidence to the start of the loop """

# Distance covered by first = L + C 

# Distance covered by second pointer is 2L + 2C

# Total Distance = (2L + 2C) - (C) = 2L + C

# Remaining = Total - distance covered by first = (2L + C) - (L + C) = L

def findLoop(head):
	# initialize first and second pointers	
	first = head.next
	second = head.next.next
	
	# Loop until the pointers coincide 
	while first != second: 
		first = first.next 
		second = second.next.next
	
	# Bring back the first pointer to head
	first = head 
	
	# loop until the pointers coincide
	while first != second: 
		first = first.next
		second = second.next 
	return first  






 

