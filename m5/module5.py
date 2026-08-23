# CSC500 Module 5 Assignment
"""
# The assignment is 'Using the latest version of Python, select and complete ONE of the following two options...'
# Since Python is picking which option and not me, I wrote two classes that complete the assignment
# regardless which path Python picks.
#
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
    
    def set_years(self):
        while True:
            try:
                self.years = int(input("Enter the number of years: "))
                if self.years > 0:
                    return True
                print("The number of years must be greater than 0.")
            except:
                print("Please enter a valid number of years.")

    def get_rainfall_float(self,year,month):  
        # Moves the value checking outside of loop to make easier to debug
        while True:
            try:
                rainfall = float(input(f"Enter the rainfall for {self.months[month]} of year {year}: "))
                if rainfall >= 0:
                    return rainfall
                print("Rainfall cannot be negative.")
            except:
                print("Please enter a valid number.")

    def collect_user_data(self):
        # Determine how many years user wants to enter
        self.set_years()

        # Outer loop handles each year
        for year in range(1, self.years + 1):

            # Inner loop handles each month
            for month in range(12):
                rainfall = self.get_rainfall_float(year,month)
                self.rainfall_data.append(rainfall)

    def calculate_rainfall(self):
        total_months = len(self.rainfall_data)
        total_rainfall = sum(self.rainfall_data)
        average = total_rainfall / total_months

        print(f"\nTotal months: {total_months}")
        print(f"Total rainfall: {total_rainfall:.2f} inches")
        print(f"Average rainfall per month: {average:.2f} inches")

    def average_rainfall(self):
        print("\nPython chose: Average Rainfall\n")

        self.collect_user_data()
        self.calculate_rainfall()


class BookstoreChallenge:
    def __init__(self):
        self.books = 0
        self.points = 0
        # This is hard-coded from most to least point threshold values.
        # I'm assuming these are NOT cummulative (reading 6 books does not get the points for 2/4)
        # ie they would not get 50 points, just 30. 
        #
        # Note: This would not work pre-Python 3.7 as it does depend on dictionary order
        self.point_table = {
            8: 60,
            6: 30,
            4: 15,
            2: 5,
            0: 0
        }

    def get_book_count(self):
        while True:
            try:
                self.books = int(input("Enter the number of books purchased this month: "))
                if self.books >= 0:
                   return True
                else:
                    print("The number of books cannot be negative.")
            except:
                print("Please enter a valid number of books.")

    def calculate_points(self):
        for threshold, points in self.point_table.items():
            if self.books >= threshold:
                self.points = points
                return True

    def bookstore_points(self):
        print("\nPython chose: Bookstore Points\n")

        self.get_book_count()
        self.calculate_points()

        print(f"Books purchased: {self.books}")
        print(f"Bookstore points awarded: {self.points}")


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
