class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        # Always push into the last position
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            # Alwasy pop from last position
            return self.items.pop()
        else:
            print("The stack is empty. Can't pop")
            return None

    def size(self):
        return len(self.items)
    
    def printStack(self):
        for item in self.items:
            print(item, end=" ")
        print("<TOP")

if __name__ == "__main__":
    # Execute only if it's run as a script, example test program
    stack = Stack()
    while True:
        print("What do you want to do?")
        print("\t1 - Push")
        print("\t2 - Pop")
        print("\t3 - Check empty")
        print("\t4 - Check size")
        print("\t5 - Print stack")
        print("\t6 - Exit")
        option = input()
        print()
        if option == '1':
            item = input("Type your item ")
            stack.push(item)
            print("Item added to the stack successfully\n")
        elif option == '2':
            item = stack.pop()
            print("Popped item" , item, "\n")
        elif option == '3':
            if stack.isEmpty():
                print("Stack is empty\n")
            else:
                print("Stack is not empty\n")
        elif option == '4':
            print("The stack size is", stack.size(), "\n")
        elif option =='5':
            stack.printStack()
            print()
        elif option =='6':
            print("Bye!")
            break
        else:
            print("Please, choose an option between 1 and 6\n")