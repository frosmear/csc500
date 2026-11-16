#!/usr/bin/env python3
"""Lab 05 - Methods"""

# STRINGS

# a) Create the words string
words = "comp1314 - python foundations class"
print("a)", words)

# b) Convert all characters to uppercase
upper = words.upper()
print("b)", upper)

# c) Capitalize each word
title = upper.title()
print("c)", title)

# d) Replace " - " with a single space
temp = title.replace(" - ", " ")
print("d)", temp)

# e) Split temp into a list of words
title_list = temp.split()
print("e)", title_list)

# f) Remove all spaces from temp
packed = "".join(title_list)
print("f)", packed)

# g) Print the length of packed
print("g)", len(packed))                 # 30

# BONUS) Capitalize comp and title-case the remaining words
course = words.replace("comp", "COMP").title()
print("Bonus)", course)                  # COMP1314 - Python Foundations Class


# LISTS

# h) Create a_list
a_list = [6, 1, 7, 0, 9]
print("h)", a_list)

# i) Add 5 to the end of a_list
a_list.append(5)
print("i)", a_list)

# j) Add 8 to the beginning of a_list
a_list.insert(0, 8)
print("j)", a_list)

# k) Add [3, 2, 4] to the end of a_list
a_list.extend([3, 2, 4])
print("k)", a_list)

# l) Sort a_list from largest to smallest
a_list.sort(reverse=True)
print("l)", a_list)

# m) Create a copy of a_list
b_list = a_list.copy()
print("m)", b_list)

# n) Sort b_list from smallest to largest
b_list.sort()
print("n)", b_list)

# o) Print both lists
print("o) a_list:", a_list)
print("   b_list:", b_list)


# DICTIONARIES

# p) Create the balance dictionary
balance = {
    "Sam": 1000,
    "Kim": 1000,
    "Joe": 2000,
    "Sue": 0,
    "Tim": 500
}
print("p)", balance)

# q) Add Tom to the dictionary
balance["Tom"] = 500
print("q)", balance)

# r) Remove Sue and save her balance
sue_value = balance.pop("Sue")
print("r)", sue_value)

# s) Save Joe's balance
joe_value = balance["Joe"]
print("s)", joe_value)

# t) Create a list of dictionary values
total = list(balance.values())
print("t)", total)

# u) Print Sue's balance, Joe's balance, and the total
print("u) Sue:", sue_value)
print("   Joe:", joe_value)
print("   Total:", sum(total))


