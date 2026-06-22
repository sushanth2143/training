class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new

    def add_beg(self,data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        new.next = self.head
        self.head = new

    def display(self):
        itr = self.head
        while itr:
            print(itr.data, end="->")
            itr = itr.next
l1 = LinkedList()
l1.add_end(50)
l1.add_end(150)
l1.add_end(798)
l1.add_end(78)
l1.add_end(98)
l1.add_end(4)
l1.add_beg(68)
l1.add_end(999)
l1.display()