

class Lexem():
    def __init__(self):
        self.buffer = []
        self.current_state = ""
        self.signs = ["+", "-", "=", "/", "*", "^"]
        self.text = {
            "sin": 1,
            "cos": 1,
            "tg": 1,
            "ln": 1,
            "exp": 1,
        }

    def parse(self, s):
        s += " "
        symbol = ""
        i = 0
        while True:
            try:
                self.text[symbol]
                self.buffer.append(symbol)
                symbol = ""
            except:
                pass
            if i >= len(s):
                self.buffer.append(symbol)
                break
            j = s[i]
            try:
                int(j)
                symbol += j
            except:
                if j == ".":
                    symbol += j
                elif j in self.signs:
                    self.buffer.append(symbol)
                    symbol = ""
                    self.buffer.append(j)
                elif j in ["(", ")"]:
                    self.buffer.append(symbol)
                    symbol = ""
                    self.buffer.append(j)
                else:
                    symbol += j

            i += 1
        self.buffer = list(filter(None, self.buffer))
        return self.buffer
