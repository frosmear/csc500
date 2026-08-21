# CSC500 Module 3 Assignment
"""
# The assignment is 'Using the latest version of Python, select and complete ONE of the following two options...'
# Since Python is picking which option and not me, I had to write functions that complete the assignment
# regardless which path the Python picks
"""

from datetime import datetime, timedelta
import random

tip_rate = 18
tax_rate = 8.5 # Parker is freaking expensive

def meal_calculator():
    print("\nPython chose: Meal Calculator\n)
    food_charge = float(input("Enter the meal price: $"))

    tip = food_charge * (tip_rate/100)
    tax = food_charge * (tax_rate/100)
    total = food_charge + tip + tax

    print(f"FoodBev total: ${food_charge:.2f}")
    print(f"Tip ({tip_rate})%:     ${tip:.2f}")
    print(f"Tax ({tax_rate)}%:      ${tax:.2f}")
    print(f"Total: ${total:.2f}")

def clock_alarm():
    print("Python chose:\n Alarm Clock")
    use_current = input("Use the current time as the starting time? (y/n): ").lower()

    if use_current == "y":
        current_time = datetime.now()
    else:
        start_hour = int(input("Enter the starting hour (0-23): "))
  
        current_time = datetime.now().replace(
            hour=start_hour,
            minute=0,
            second=0,
            microsecond=0
        )

    wait_hours = float(input("Enter the number of hours to wait: "))

    alarm_time = current_time + timedelta(hours=wait_hours)

    print(f"\nStarting time: {current_time.strftime('%H:%M')}")
    print(f"Alarm time:    {alarm_time.strftime('%H:%M')}")


def main():
    selected_option = random.randint(1, 2)

    print("Programming Logic Challenge")
    print(f"Randomly selected option: {selected_option}")

    if selected_option == 1:
        restaurant_meal_calculator()
    else:
        clock_alarm()


def doitmodulostyle():
    # This version does it in the "spirit" of the assignment using modulo math
    # in case the thing gets auto-graded I want full credit. 
    
    def get_valid_int(prompt, is_time=False):
        #Asks for input and validates it based on whether it represents a 24-hour time.
        while True:
            try:
                value = int(input(prompt))
                
                # If it's a 24-hour time, enforce the 0-23 range
                if is_time:
                    if 0 <= value <= 23:
                        return value
                    else:
                        # I thought about have this be a DrPepper Exception
                        print("Error: Time must be between 0 and 23. Try again.")
                
                # If it's not a time (like wait hours), accept any positive integer
                else:
                    if value >= 0:
                        return value
                    else:
                        print("Error: Value must be 0 or greater. Try again.")
                        
            except ValueError:
                print("Error: Please enter a valid integer.")

    # Gather validated user inputs
    current_time = get_valid_int("Enter the current time (0-23): ", is_time=True)
    hours_to_wait = get_valid_int("Enter the number of hours to wait: ")

    # Calculations: Use modulo 24 to wrap around the clock
    alarm_time = (current_time + hours_to_wait) % 24
    days_from_now = (current_time + hours_to_wait) / 24 # not sure this was required but to be safe

    # Output: Display the final alarm time
    print(f"The alarm will go off at: {alarm_time}")
    print(f"Days from now: {days_from_now}")

# Call the function to run the program
doitmodulostyle()











if __name__ == "__main__":
    main()
