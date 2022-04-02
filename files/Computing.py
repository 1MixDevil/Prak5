from files.Stack import Stack
import math


class Computing():
    def __init__(self):
        self.options = {
            "+": self.plus,
            "-": self.minus,
            "/": self.division,
            "^": self.degree,
            "*": self.multiply,
            "exp": self.exp,
            "cos": self.cos,
            "sin": self.sin,
            "ln": self.ln,
            "~": self.minus_I,
        }
        self.minus = 0
        self.stack = Stack()

    def complete(self, c):
        for i in c:
            if i not in self.options:
                self.stack.push(i)
            elif i in self.options:
                self.options[i]()
        return self.stack.array

    def plus(self):
        a = float(self.stack.pop())
        b = float(self.stack.pop())
        self.stack.push(a + b)

    def minus(self):
        a = float(self.stack.pop())
        b = float(self.stack.pop())
        self.stack.push(b - a)

    def division(self):
        a = float(self.stack.pop())
        b = float(self.stack.pop())
        self.stack.push(str(b / a))

    def ln(self):
        a = float(self.stack.pop())
        self.stack.push(math.log(a))

    def degree(self):
        a = float(self.stack.pop())
        b = float(self.stack.pop())
        self.stack.push(str(b ** a))

    def multiply(self):
        a = float(self.stack.pop())
        b = float(self.stack.pop())
        self.stack.push(str(a * b))

    def exp(self):
        a = float(self.stack.pop())
        self.stack.push(str(math.exp(a)))

    def sin(self):
        a = float(self.stack.pop())
        self.stack.push(str(math.sin(a)))

    def cos(self):
        a = float(self.stack.pop())
        self.stack.push(str(math.cos(a)))

    def minus_I(self):
        self.stack.push(str(-1 * float(self.stack.pop())))

