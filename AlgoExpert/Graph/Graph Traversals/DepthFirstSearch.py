# Node class for graph 
class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.visited = False

# O(v + e) time | O(v) space
#Method for DFS
    def dfs(self, array):
        '''
        Make the node visted and append the name to the array, 
        Traverse through each child if it is not visited.  
        '''
        self.visited = True
        array.append(self.name)
        for child in self.children:
            if not child.visited:
                child.dfs(array)
        return array

if __name__ == '__main__':
    n1 = Node(5)
    n2 = Node(6)
    n3 = Node(7)
    n2.children = [n1, n3]
    print(n2.dfs([]))


         

