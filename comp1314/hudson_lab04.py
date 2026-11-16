#!/usr/bin/env python3
"""Lab 04 - Variables - Lists"""

# Declare variables
animals = ["dog", "cat", "horse", "bear", "python"]
languages = ["Farsi", "java", "python", "bash", "English", "perl"]
python_sentence = "With python, we can fly!"
mixed_numbers = [1, "two", "3", 2**2, 1.25+3.75]

# a) Save the last element of languages
worst_language_ever = languages[-1]
print("a)", worst_language_ever)          # perl
# Don't need a computer to figure that one out!

# b) Determine the number of elements in animals
print("b)", len(animals))                 # 5

# c) Determine the number of words in python_sentence
print("c)", len(python_sentence.split())) # 5

# d) Determine the total number of characters in animals
print("d)", sum(len(animal) for animal in animals))  # 21

# Determine the types of elements in mixed_numbers

# e) type(mixed_numbers[0])
print("e)", type(mixed_numbers[0]))       # <class 'int'>

# f) type(mixed_numbers[1])
print("f)", type(mixed_numbers[1]))       # <class 'str'>

# g) type(mixed_numbers[2])
print("g)", type(mixed_numbers[2]))       # <class 'str'>

# h) type(mixed_numbers[3])
print("h)", type(mixed_numbers[3]))       # <class 'int'>

# i) type(mixed_numbers[4])
print("i)", type(mixed_numbers[4]))       # <class 'float'>


