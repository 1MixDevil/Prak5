import math
from files.Inequality import inequality
from files.Postfix import Postfix
from files.Lexem import Lexem
from files.Stack import Stack
from files.Computing import Computing

equation = input("Привет! Введи какое-то уравнение: \n")
try:
    a = Lexem()
    c = a.parse(equation)
    if "x" not in c:
        a = Postfix()
        c = a.record(c)
        a = Computing()
        print(a.complete(c)[0])
    else:
        print("В каком диапазоне мне искать x?")
        a = Postfix()
        c = a.record(c)
        a = inequality(float(input("Введите первую точку: \n")), float(input("Введите вторую точку: \n")), c)
        if input("Введите IN, если хотите вычислить интеграл, если просто хотите решить уравнение, напишите что-то другое \n") == "IN":
            print(a.find_integral())
        else:
            print(a.find())

except:
    print("Что-то пошло не так :(")
