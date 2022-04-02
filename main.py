import math
from files.Postfix import Postfix
from files.Lexem import Lexem
from files.Stack import Stack
from files.Computing import Computing


a = Lexem()
c = a.parse("3+2*2")
a = Postfix()
c = a.record(c)
a = Computing()
print(a.complete(c))
