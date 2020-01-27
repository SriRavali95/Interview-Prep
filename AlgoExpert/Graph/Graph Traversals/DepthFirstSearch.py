class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.visited = False

    def dfs(self, array):
        self.visited = True
        array.append(self.name)
        for child in self.children:
            if not child.visited:
                child.dfs(array)
        return array

n1 = Node(5)
n2 = Node(6)
n3 = Node(7)
n2.children = [n1, n3]
print(n2.dfs([]))


         

