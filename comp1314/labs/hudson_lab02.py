#!/usr/bin/env python3
"""Lab 02 - Variables - Numbers
"""

# Declare variables
a = 10
b = 15

# Arithmetic expressions

# a) a + b
print("a)", a + b)                         # 25

# b) a * b
print("b)", a * b)                         # 150

# c) a - b
print("c)", a - b)                         # -5

# d) (b + a) / (b - a)
print("d)", (b + a) / (b - a))             # 5.0

# Store the result in x
x = ((b + a) / (b - a))**2

# e) print(x)
print("e)", x)                             # 25.0


# Integer division and remainder

dividend = 100
divisor = 8
quotient = dividend // divisor
remainder = dividend % divisor

# f) Print the division equation
print("f)", dividend, "=", divisor, "*", quotient, "+", remainder)


