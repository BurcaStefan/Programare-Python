class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]
    
    def print(self):
        print(self.items)
    

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
print(stack.peek())
stack.push(4)
stack.push(5)
stack.print()