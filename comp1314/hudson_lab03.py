#!/usr/bin/env python3
"""Lab 03 - Variables - Strings"""

# Declare variables
a = 'abra'
b = 'cad'
c = a + b + a
d = 'bird'
pi = 22 / 7   # the math nerds heads will explode with this
d_5 = d * 5

# a) What value is stored in variable c?
print("a)", c)                     # abracadabra

# b) Why does the following assignment not work?
# pi_str = "pi is " + pi
print("b) Python cannot concatenate a string and a float.")
print("   The float must first be converted to a string.")

# c) Convert pi to a string without typing out the number
pi_str = f"pi is {pi}"
print("c)", pi_str)                # pi is 3.142857142857143

# d) What is stored in variable d_5? Why?
print("d)", d_5)                   # birdbirdbirdbirdbird
print("   Multiplying a string by an integer repeats the string.")

# e) What character is at d_5[0]?
print("e)", d_5[0])                # b

# f) What character is at c[4]?
print("f)", c[4])                  # c

# g) What character is at d[-1]?
print("g)", d[-1])                 # d

# h) What word is at pi_str[3:5]?
print("h)", pi_str[3:5])           # is

# i) What animal makes the sound found at c[1:6:2]?
print("i)", c[1:6:2])              # baa (sheep)

# j) What word is c[4:1:-1]?
print("j)", c[4:1:-1])             # car
