#!/usr/bin/env python3
"""Lab 07 - Comparators"""

# Declare variables
a = "hello"
b = 100.0
c = "python rocks!"
d = "January"
e = 10 ** 2
f = 2016
g = "100"

animals = ["dog", "cat", "horse", "bear", "python"]
languages = ["Farsi", "java", "python", "bash", "English", "perl"]

# Determine TRUE or FALSE

print("a.", a == a)                              # True
print("b.", a == c)                              # False
print("c.", type(a) == type(c))                  # True
print("d.", type(a) == type(b))                  # False
print("e.", b == e)                              # True
print("f.", b < f)                               # True
print("g.", str(b) < str(f))                     # True
print("h.", d < a)                               # True
print("i.", c < d)                               # False
print("j.", int(g) == b)                         # True
print("k.", " " in c)                            # True
print("l.", "rock" in c)                         # True
print("m.", "snakes" in c)                       # False
print("n.", "pythons" in c)                      # False
print("o.", "0" in str(e))                       # True
print("p.", "10" in g and 's' in d)              # False
print("q.", True and not False)                  # True

# Answer the following questions

# r. Is "python" in both animals and languages?
print("r.", "python" in animals and "python" in languages)  # True

# s. Is animals longer than languages?
print("s.", len(animals) > len(languages))  # False
