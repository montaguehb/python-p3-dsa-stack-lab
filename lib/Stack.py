class Stack:

    def __init__(self, items = None, limit = 100):
        self.limit = limit
        self.items = []
        if items:
            for item in items:
                self.push(item)

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        return None if self.isEmpty() else self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        try:
            return len(self.items) - self.items.index(target) - 1
        except ValueError:
            return -1 