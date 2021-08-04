class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0

    def push(self, obj):
        self.data.append(obj)

    def pop(self):
        self.data.pop()

    def top(self):
        return self.data[-1]

    def bottom(self):
        return self.data[0]

    def tampil(self, index):
        return self.data[index]