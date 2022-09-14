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
                print(a.data, end=" ")
                a = a.prev

    def insert_start(self,data):
        print()
        ns = Node(data)
        a = self.head
        a.prev = ns
        ns.next = a
        self.head = ns

    def insert_end(self,data):
        print()
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne
        ne.prev = a

    def insert_between(self,position,data):
        print()
        nib = Node(data)
        a =self.head
        for i in range(1, position-1):
            a = a.next
        nib.prev = a
        nib.next = a.next
        a.next.prev = nib
        a.next = nib 

    def delete_start(self):
        print()
        a = self.head
        self.head = a.next
        a.next = None
        self.head.prev = None

    def delete_end(self):
        print()
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None
        a.prev = None

    def delete_between(self,position):
        print()
        a = self.head.next
        b = self.head
        for i in range(1 , position-1):
            a = a.next
            b = b.next
        b.next = a.next
        a.next.prev = b
        a.next = None
        a.prev = None

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
dll.insert_start(2)
dll.for_traverse()
dll.bac_traverse()
dll.insert_end(28)
dll.for_traverse()
dll.insert_between(3,17)
dll.for_traverse()
dll.delete_start()
dll.for_traverse()
dll.bac_traverse()
dll.delete_end()
dll.for_traverse()
dll.bac_traverse()
dll.delete_between(3)
dll.for_traverse()
dll.bac_traverse()