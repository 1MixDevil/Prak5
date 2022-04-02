from files.Stack import Stack

class Postfix:
    def __init__(self):
        self.stack = Stack()
        self.string = []
        self.Priority = {
            "(": 0,
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "^": 3,
            "~": 4,
            "cos": 4,
            "sin": 4,
            "tg": 4,
            "exp": 4,
        }

    def record(self, lexems):
        for i in lexems:
            try:
                float(i)
                self.string.append(i)
            except:
                if i == "(":
                    self.stack.push(i)
                elif i == ")":
                    while True:
                        a = self.stack.pop()
                        if a == "(":
                            break
                        self.string.append(a)
                elif i in self.Priority:
                    prioritet = self.Priority[i]
                    while True:
                        try:
                            a = self.stack.pop()
                            if self.Priority[a] > prioritet:
                                self.string.append(a)
                            else:
                                self.stack.push(a)
                                break
                        except:
                            break
                    self.stack.push(i)

        for i in self.stack.array[::-1]:
            self.string.append(i)
        return self.string
