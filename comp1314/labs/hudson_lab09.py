#!/usr/bin/env python3
"""Lab 09 - List Comprehension"""


def get_bound(prompt, default):
    """Prompt for a non-negative integer, using default if blank."""
    while True:
        value = input(prompt).strip()

        if not value:
            return default

        try:
            number = int(value)
            if number >= 0:
                return number
        except ValueError:
            pass

        print("Please enter a non-negative integer.")


def divisible_by_3(lower, upper):
    """Return integers evenly divisible by 3."""
    return [
        number for number in range(lower, upper + 1)
        if number % 3 == 0
    ]


def divisible_by_3_and_5(lower, upper):
    """Return integers evenly divisible by both 3 and 5."""
    return [
        number for number in range(lower, upper + 1)
        if number % 3 == 0 and number % 5 == 0
    ]


def even_fizzy(lower, upper):
    """Return even integers, replacing multiples of 3 with 'fizzy'."""
    return [
        'fizzy' if number % 3 == 0 else number
        for number in range(lower + (lower % 2), upper + 1, 2)
    ]


def fizzybuzzy(lower, upper):
    """Return integers, replacing multiples of 3 and 5 with strings."""
    return [
        'fizzybuzzy' if number % 15 == 0
        else 'fizzy' if number % 3 == 0
        else number
        for number in range(lower, upper + 1)
    ]


def fizzbuzz(lower, upper):
    """Return the complete FizzBuzz sequence."""
    return [
        'fizzybuzzy' if number % 15 == 0
        else 'fizzy' if number % 3 == 0
        else 'buzzy' if number % 5 == 0
        else number
        for number in range(lower, upper + 1)
    ]


def main():
    """Get sequence bounds and display the five lists."""
    lower = get_bound("Enter start (default 0): ", 0)
    upper = get_bound("Enter end (default 100): ", 100)

    if lower > upper:
        print("Start must be less than or equal to end. Try again.")
        return main()

    print("\n1. Integers divisible by 3:")
    print(divisible_by_3(lower, upper))

    print("\n2. Integers divisible by 3 and 5:")
    print(divisible_by_3_and_5(lower, upper))

    print("\n3. Even integers with fizzy:")
    print(even_fizzy(lower, upper))

    print("\n4. Integers with fizzy and fizzybuzzy:")
    print(fizzybuzzy(lower, upper))

    print("\nChallenge: Complete FizzBuzz:")
    print(fizzbuzz(lower, upper))


if __name__ == "__main__":
    main()
