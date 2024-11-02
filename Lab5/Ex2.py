class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop(0)

    def peek(self):
        if not self.items:
            return None
        return self.items[0]
    
    def print(self):
        print(self.items)


queue = Queue()
queue.push("Start")
queue.push(2)
queue.push(3)
queue.pop()
print(queue.peek())
queue.push("Sfarsit")
queue.print()
