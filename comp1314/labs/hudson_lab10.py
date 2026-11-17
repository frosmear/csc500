#!/usr/bin/env python3
"""Lab 10 - Functions"""


def double(input):
    return input * 2


def myFunc(a, b, c):
    return a / b * c


def add(first, second):
    return first + second


a = double(2)
b = double(2.5)
c = myFunc(a, b, a)
d = add(add(a, b), c)

python_goodness = double("python")

# Display results
print("a =", a)                              # a = 4
print("b =", b)                              # b = 5.0
print("c =", c)                              # c = 3.2
print("d =", d)                              # d = 12.2
print("python_goodness =", python_goodness)  # python_goodness = pythonpython
