class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
    
    def pop(self):
        if not self.head:
            return None
        popped = self.head.data
        self.head = self.head.next
        return popped

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

# Test program
x = Stack() # Creating an object of the Stack class
x.push(1) # pushing 1 to the stack
x.push(2) # pushing 2 to the stack
x.display() # displays 2 1
print(x.pop()) # prints the deleted element from the stack (which is the last element)
x.display() # 1
print(x.pop()) # prints the value 1
print(x.pop()) # returns None because the stack is empty