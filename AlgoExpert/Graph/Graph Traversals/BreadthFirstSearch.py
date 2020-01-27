class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.visited = False
    
    def bfs(self, array):
        queue = [self]
        while queue:
            current = queue.pop(0)
            current.visited = True
            array.append(current.name)
            for child in current.children:
                if not child.visited:
                    queue.append(child)
        return array


n1 = Node(5)
n2 = Node(6)
n3 = Node(7)
n4 = Node(8)
n2.children = [n1, n3]
n1.children = [n4]
array = []
n2.bfs(array)

print(n1.visited, n2.visited, n3.visited,n4.visited)
print(array)



