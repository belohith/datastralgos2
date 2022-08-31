class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
node1 = Node(7)
print(node1.data)
print(node1.ref)

class SLL:
    def __init__(self):
        self.head = None
        

sll = SLL()