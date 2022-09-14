class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def for_traverse(self):
        if self.head is None:
            print("Doubly Linked List is empty")
        else:
            a = self.head
            while a is not None:
                print(a.data)
                a = a.next
    
    
    def bac_traverse(self):
        if self.head is None:
            print("Doubly Linked List is empty")
        else:
            a = self.head
            while a.next is not None:
                a  = a.next
            while a is not None:
                print(a.data, end="")
                a = a.prev

dll = DLL()
node1 = Node(5)
dll.head = node1
node2 = Node(10)
node1.next = node2
node3 = Node(15)
node2.next = node3
node4 = Node(20)
node3.next = node4
dll.for_traverse()
dll.bac_traverse()