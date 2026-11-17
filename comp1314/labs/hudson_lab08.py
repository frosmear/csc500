#!/usr/bin/env python3
"""Lab 08 - Conditionals & Loops"""


def fizzbuzz(lower, upper):
    """Print integers, replacing multiples of 3 and 5 with fizzbuzz."""
    for number in range(lower, upper + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)


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


def main():
    """Get sequence bounds and run FizzBuzz."""
    lower = get_bound("Enter start (default 1): ", 1)
    upper = get_bound("Enter end (default 100): ", 100)

    if lower > upper:
        print("Start must be less than or equal to end. Try again.")
        return main()

    fizzbuzz(lower, upper)


if __name__ == "__main__":
    main()
