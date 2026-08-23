# CSC500 Module 4 Assignment
"""
# The assignment is 'Using the latest version of Python, select and complete ONE of the following two options...'
# Since Python is picking which option and not me, I wrote two classes that complete the assignment
# regardless which path Python picks.
#
# Option 1 also includes a calculation using a Pythonic list comprehension.
"""

import random

class RainfallChallenge:
    def __init__(self):
        self.months = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        ]
        self.years = 0
        self.rainfall_data = []

    def get_rainfall_data(self):
        while True:
            try:
                self.years = int(input("Enter the number of years: "))

                if self.years > 0:
                    break
                else:
                    print("The number of years must be greater than 0.")
            except:
                print("Please enter a valid number of years.")

        # Outer loop handles each year
        for year in range(1, self.years + 1):

            # Inner loop handles each month
            for month in range(12):
                while True:
                    try:
                        rainfall = float(input(
                            f"Enter the rainfall for {self.months[month]} of year {year}: "
                        ))

                        if rainfall >= 0:
                            break
                        else:
                            print("Rainfall cannot be negative.")
                    except:
                        print("Please enter a valid number.")

                self.rainfall_data.append(rainfall)

    def calculate_rainfall(self):
        total_months = len(self.rainfall_data)

        # Calculate the total using a Pythonic list comprehension
        total_rainfall = sum([rainfall for rainfall in self.rainfall_data])

        average = total_rainfall / total_months

        print(f"\nTotal months: {total_months}")
        print(f"Total rainfall: {total_rainfall:.2f} inches")
        print(f"Average rainfall per month: {average:.2f} inches")

    def average_rainfall(self):
        print("\nPython chose: Average Rainfall\n")

        self.get_rainfall_data()
        self.calculate_rainfall()







class BookstoreChallenge:

    def bookstore_points(self):
        print("\nPython chose: Bookstore Points\n")

        while True:
            try:
                books = int(input("Enter the number of books purchased this month: "))

                if books >= 0:
                    break
                else:
                    print("The number of books cannot be negative.")
            except:
                print("Please enter a valid number of books.")

        # Award points based on the number of books purchased
        if books >= 8:
            points = 60
        elif books >= 6:
            points = 30
        elif books >= 4:
            points = 15
        elif books >= 2:
            points = 5
        else:
            points = 0

        print(f"Books purchased: {books}")
        print(f"Bookstore points awarded: {points}")


def main():
    options = ['Average Rainfall (Nested Loops)','Bookstore Points (Conditional Logic)']
    selected_option = random.randint(0, 1)

    print("Programming Logic Challenge")
    print(f"Randomly selected option: {options[selected_option]}")

    if selected_option == 0:
        challenge = RainfallChallenge()
        challenge.average_rainfall()
    else:
        challenge = BookstoreChallenge()
        challenge.bookstore_points()

if __name__ == "__main__":
    main()
