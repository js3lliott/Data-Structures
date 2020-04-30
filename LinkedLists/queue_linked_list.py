class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if not self.tail:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def dequeue(self):
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        return val

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

x = Queue() # Creates an object of the class Queue
x.enqueue(1)
x.enqueue(2)
x.display()
print(x.dequeue())
x.display()
print(x.dequeue())
print(x.dequeue())