class Stack():
    def __init__(self, size):
        self.size = size
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        if len(self.items) < self.size:
            self.items.append(item)
        else:
            raise Exception('Stak is full')
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception('Stack is empty')

    def peak(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items
