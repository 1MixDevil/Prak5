import math
from files.Postfix import Postfix
from files.Lexem import Lexem
from files.Stack import Stack
from files.Computing import Computing

class inequality:
    def __init__(self, a, b, stroka):
        self.a = a
        self.b = b
        self.E = 0.00001
        self.stroka = stroka

    def f(self, chisl):
        parse = []
        for i in self.stroka:
            if i == 'x':
                if chisl > 0:
                    parse.append(str(chisl))
                else:
                    parse.append(str(abs(chisl)))
                    parse.append('~')
            else:
                parse.append(i)
        a = Computing()
        return a.complete(parse)[0]

    def find(self):
        if float(self.f(self.a)) == float(self.f(self.b)):
            self.b -= 1
        x = self.b - (float(self.f(self.b)) / (float(self.f(self.b)) - float(self.f(self.a)))) * (self.b - self.a)
        while abs(float(self.f(x))) > self.E:
            x = self.b - (float(self.f(self.b)) / float((self.f(self.b)) - float(self.f(self.a)))) * (self.b - self.a)
            if abs(self.a - x) < abs(self.b - x):
                self.a = x
            else:
                self.b = x
        return x if self.a <= x <= self.b else None

    def find_integral(self):
        a_new = self.a + self.E
        square = 0
        while self.a <= self.b:
            square += ((a_new - self.a) / 6) * (float(self.f(self.a)) + 4 * float(self.f((self.a + a_new) / 2)) + float(self.f(a_new)))
            self.a = a_new
            a_new += self.E
        return square