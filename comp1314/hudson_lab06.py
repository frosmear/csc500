#!/usr/bin/env python3
"""Lab 06 - Assignment Operations"""

# Initialize a
a = int()
step1 = a
step2 = format(a, "b")
print("1)", step1, "  2)", step2)

# Add 2
# Same as: a = a + 2
a += 2
step3 = a
step4 = format(a, "b")
print("3)", step3, "  4)", step4)

# Shift bits left by 1
# Same as: a = a << 1
a <<= 1
step6 = a
step5 = format(a, "b")
print("6)", step6, "  5)", step5)

# Bitwise OR
# Same as: a = a | 1
a |= 1
step8 = a
step7 = format(a, "b")
print("8)", step8, "  7)", step7)

# Bitwise XOR
# Same as: a = a ^ 0xf
# Same as: a = a ^ 15
a ^= 0xf
step10 = a
step9 = format(a, "b")
print("10)", step10, "  9)", step9)

# Shift bits right by 3
# Same as: a = a >> 3
a >>= 3
step12 = a
step11 = format(a, "b")
print("12)", step12, "  11)", step11)

# Convert to string
a = str(a)
step13 = a
print("13)", step13)

# Repeat string 5 times
# Same as: a = a * 5
a *= 5
step14 = a
print("14)", step14)

# Convert binary string to integer
a = int(a, 2)
step16 = a
step15 = format(a, "b")
print("16)", step16, "  15)", step15)

# Convert to float
a = float(a)
step17 = a
print("17)", step17)

# Count characters in string representation
a = len(str(a))
step18 = a
print("18)", step18)


# Print completed worksheet

print()
print("LAB 06 - COMPLETED WORKSHEET")
print("-" * 78)
print(f"{'Code':<25} {'Base 10':<12} {'Base 2':<12} SAME AS")
print("-" * 78)

print(f"{'a = int()':<25} {step1:<12} {step2:<12}")
print(f"{'a += 2':<25} {step3:<12} {step4:<12} a = a + 2")
print(f"{'a <<= 1':<25} {step6:<12} {step5:<12} a = a << 1")
print(f"{'a |= 1':<25} {step8:<12} {step7:<12} a = a | 1")
print(f"{'a ^= 0xf':<25} {step10:<12} {step9:<12} a = a ^ 0xf")
print(f"{'a >>= 3':<25} {step12:<12} {step11:<12} a = a >> 3")
print(f"{'a = str(a)':<25} {step13:<12}")
print(f"{'a *= 5':<25} {step14:<12} {'':<12} a = a * 5")
print(f"{'a = int(a, 2)':<25} {step16:<12} {step15}")
print(f"{'a = float(a)':<25} {step17}")
print(f"{'a = len(str(a))':<25} {step18}")

print("-" * 78)
print()

