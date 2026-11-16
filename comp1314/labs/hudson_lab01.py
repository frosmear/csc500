#!/usr/bin/env python3

"""Lab 01 - Python as a Calculator

"""

# a) 10 + 15
print("a)", 10 + 15)       # 25

# b) 20 + 2
print("b)", 20 + 2)        # 22

# c) 50 - 5 * 6
print("c)", 50 - 5 * 6)    # 20

# d) 100 / 8
print("d)", 100 / 8)       # 12.5

# e) 75 / 3
print("e)", 75 / 3)        # 25.0

# f) 75 // 3
print("f)", 75 // 3)      # 25

# g) 100 // 8
print("g)", 100 // 8)     # 12

# h) 100 % 8
print("h)", 100 % 8)      # 4

# i) 2.0 ** 4
print("i)", 2.0 ** 4)     # 16.0

# j) 10 ** 3
print("j)", 10 ** 3)      # 1000

# k) Why are there decimal points in d) and e)?
print("k) The / operator performs true division in Python.")
print("   It always returns a floating-point number (float),")
print("   even when the result is a whole number.")

# l) Why are there NO decimal points in f) and g)?
print("l) The // operator performs floor division.")
print("   It rounds the result down to the nearest whole number")
print("   and returns an integer (int) when both operands are integers.")
