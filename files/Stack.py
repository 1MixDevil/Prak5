class Stack:
    def __init__(self):
        self.array = []

    def push(self, new_value):
        self.array.append(new_value)
        return self.array

    def pop(self):
        return self.array.pop(len(self.array) - 1)
