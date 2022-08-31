class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("Singly Linked List is empty")
        else:
            a = self.head
            while a is not None:
                print(a.data)
                a = a.next

sll = SLL()
node1 = Node(5)
sll.head = node1
node2 = Node(10)
node1.next = node2
node3 = Node(15)
node2.next = node3
node4 = Node(20)
node3.next = node4
sll.traverse()