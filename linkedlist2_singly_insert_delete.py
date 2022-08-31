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

    def insert_start(self, data):
        print()
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_end(self, data):
        print()
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne

    def insert_between(self, position, data):
        print()
        nib = Node(data)
        a = self.head
        for i in range(position-1):
            a = a.next
        nib.next = a.next
        a.next = nib

    def delete_start(self):
        print()
        a = self.head
        self.head = a.next
        a.next = None

    def delete_end(self):
        print()
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None

    def delete_between(self, position):
        print()
        prev = self.head
        a = self.head.next
        for i in range(1, position-1):
            a = a.next
            prev = prev.next
        prev.next = a.next
        a.next = None

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
sll.insert_start(2)
sll.traverse()
sll.insert_end(25)
sll.traverse()
sll.insert_between(3,17)
sll.traverse()
sll.delete_start()
sll.traverse()
sll.delete_end()
sll.traverse()
sll.delete_between(3)
sll.traverse()