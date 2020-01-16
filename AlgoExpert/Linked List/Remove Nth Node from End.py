""" 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9, 4 
4th position is 6, solution is 
 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9 """

" Two pointers are used as the single linked list can't be traversed from the end"

def removeKthNodeFromEnd(head, k):
    # Write your code here.
	# Initialize the counter with 1
	counter = 1 
	# Initialize first and second with head
	first = head
	second = head
	# loop until k nodes from the head 
	while counter <= k:
		second = second.next
		counter += 1
	# if the second node is null then the head had to be removed
	if second is None: 
		head.value = head.next.value
		head.next = head.next.next
		return 
	# Until the second.next is not None traverse 
	while second.next is not None: 
		first  = first.next 
		second = second.next 
	first.next = first.next.next



 

