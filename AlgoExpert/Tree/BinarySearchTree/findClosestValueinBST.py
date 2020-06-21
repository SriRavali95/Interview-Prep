#Class for BST 
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Avg: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
#Static method for finding closest value 
    @staticmethod
    def findClosestValueInBsthelper(tree, target, closest): 
        '''
        Using Node value assignments the time complexity reduces to O(log(n))
        '''
        currentNode = tree 
        while currentNode is not None: 
            if abs(target - closest) > abs(target-currentNode.value):
                closest = currentNode.value
            if target < currentNode.value:  
                currentNode = currentNode.left
            elif target > currentNode.value: 
                currentNode = currentNode.right
            else: 
                break
        return closest

if __name__ == '__main__': 
        # Construct tree   
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        print(BST.findClosestValueInBsthelper(root,12,root.value))

