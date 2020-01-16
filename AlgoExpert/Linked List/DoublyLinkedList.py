# Node class for linked list
class Node: 
    def __init__(self, value):
        self.value = value 
        self.prev = None 
        self.next = None 
        
# DoublyLinkedlist Class
class DoublyLinkedList():
    # Instantaneous constructor to set the head and tail 
    def __init__(self):
        self.head = None 
        self.tail = None 

    # Method to set the head of the dll 
    def setHead(self, node):
        # if the head is none then update the head and tail of the dll 
        if self.head is None: 
            self.head = None 
            self.tail = None 
            return
        # If the head is not None then insert the node before the head 
        self.insertBefore(self.head, node)

    # Method to set the tail of the dll 
    def setTail(self, node): 
        # if the tail is none then set the head and tail of the dll with the node
        if self.tail is None: 
            self.setHead(node)
            return
        # If the node is not empty then insert the node after the tail 
        self.insertAfter(self.tail, node)

    # Method for insertBefore
    def insertBefore(self, node, nodeToInsert):
        # if the nodeToInsert is head and tail then do nothing 
        if nodeToInsert == self.head and nodeToInsert == self.tail: 
            return         
        # if the node is already in the dll then remove it 
        self.remove(nodeToInsert)     
        # update the nodeToInsert.prev to the node.prev
        nodeToInsert.prev = node.prev
        #update the nodeToInsert.next to the node
        nodeToInsert.next = node
        
        # if the node.prev is None i.e., the node is head 
        if node.prev is None: 
            self.head = nodeToInsert
        else: 
            node.prev.next = nodeToInsert
        # update the node.prev to the nodeToInsert
        node.prev = nodeToInsert
    
    #Method for insertAfter
    def insertAfter(self, node, nodeToInsert):
        # if the nodeToInsert is head and tail then do nothing 
        if nodeToInsert == self.head and nodeToInsert == self.tail: 
            return         
        # if the node is already in the dll then remove it 
        self.remove(nodeToInsert)     
        # update the nodeToInsert.prev to the node
        nodeToInsert.prev = node
        #update the nodeToInsert.next to the node.next
        nodeToInsert.next = node.next
        
        # if the node.prev is None i.e., the node is tail 
        if node.next is None: 
            self.tail = nodeToInsert
        else: 
            node.next.prev = nodeToInsert
        # update the node.prev to the nodeToInsert
        node.next = nodeToInsert
    
    #Method for insertAt a given position
    def insertAtPosition(self, position, nodeToInsert):
        # if the position is 1 then insert at the head 
        if position == 1:
            self.setHead(nodeToInsert)
        # loop through until the end or getting the position
        currentPosition = 1
        node = self.head
        while node is not None and currentPosition != position: 
            node = node.next 
            currentPosition += 1
        """while loop breaks then if we are not at the end of the list then it is to be inserted 
           before the node"""
        if node is not None: 
            self.insertBefore(node, nodeToInsert)
        #Else we reached the end of the node so set the tail
        else:
            self.setTail(nodeToInsert)
    
    # Method to check whether the node is in the dll
    def containsNodeWithValue(self, value):
        # Take the instance of the head for traversal 
        node = self.head
        # Loop through until the node is empty and the value not equal to the value required
        while node is not None and node.value != value: 
            node = node.next
            
        """while loop breaks if the node is None or the value is found. 
        Returning not None will clearly check whether the node is available or not"""             
        return node is not None 
    
    # Method to remove all the nodes with bindings
    def removeNodesWithValue(self, value):
        # Instance of the head
        node = self.head
        # Loop until the last of the list
        while node is not None: 
            # Copy the instance so that it is not lost in the traversal
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value: 
                self.remove(nodeToRemove)
                
    # Method to remove the node 
    def remove(self, node):
        # If the node is head then update the head of the dll 
        if node == self.head: 
            self.head = self.head.next
        # If the node is tail then update the tail of the dll 
        if node == self.tail: 
            self.tail = self.tail.prev
        # Remove the bindings of the node 
        self.removeBindings(node)
    
    # method to remove the bindings of the node
    def removeBindings(self, node):
        # If the node.previous is not empty then update it with the next node 
        if node.prev is not None: 
            node.prev.next = node.next
        # If the node.next is not empty then update it with the previous node 
        if node.next is not None: 
            node.next.prev = node.prev
        # Update the previous and next of the node to None 
        node.prev = None 
        node.next = None 
    
    
            
        
        