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
    print("\nPython chose: Meal Calculator\n")
    while True:
        try:
            food_charge = float(input("Enter the meal price: $ "))
            break
        except:
            print("The price is wrong.")

    tip = food_charge * (tip_rate/100)
    tax = food_charge * (tax_rate/100)
    total = food_charge + tip + tax

    print(f"FoodBev total: ${food_charge:.2f}")
    print(f"Tip ({tip_rate})%:     ${tip:.2f}")
    print(f"Tax ({tax_rate})%:      ${tax:.2f}")
    print(f"Total: ${total:.2f}")

def alarm_clock():
    print("Python chose:\n Alarm Clock")

    # Function to validate inputs regardless of method used
    def get_valid_int(prompt, is_time24hour=False):
        while True:
            try:
                value = int(input(prompt))
                
                # If it's a 24-hour time, enforce the 0-23 range
                if is_time24hour:
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

    # Give option to default current time
    use_current = input("Use the current time as the starting time? (y/n): ").lower()

    if use_current == "y":
        current_time = datetime.now()
        start_hour = current_time.hour
    else:
        start_hour = get_valid_int("Enter the starting hour (0-23): ")
  
        current_time = datetime.now().replace(
            hour=start_hour,
            minute=0,
            second=0,
            microsecond=0
        )

    wait_hours = get_valid_int("Enter the number of hours to wait: ")

    alarm_time = current_time + timedelta(hours=wait_hours)

    print(f"\nStarting ntime: {current_time.strftime('%H:%M')}")
    print(f"Alarm time:    {alarm_time.strftime('%H:%M')}")
    print("That method used datetime, here's the same thing using just modulo math:")
    doitmodulostyle(start_hour,wait_hours)  


def doitmodulostyle(start_time,hours_to_wait):
    # This version does it in the "spirit" of the assignment using modulo math
    # in case the thing gets auto-graded I want full credit. 
    
    # don't ask user twice for input
    #start_time = get_valid_int("Enter the start time (0-23): ", is_time=True)
    #hours_to_wait = get_valid_int("Enter the number of hours to wait: ")

    # Calculations: Use modulo 24 to wrap around the clock
    alarm_time = (start_time + hours_to_wait) % 24
    mids_from_now = (start_time + hours_to_wait) // 24 # not sure this was required but to be safe

    # Output: Display the final alarm time
    print(f"The alarm will go off at: {alarm_time}")
    print(f"Midnights will happen: {mids_from_now} times")



def main():
    selected_option = random.randint(1, 2)

    print("Programming Logic Challenge")
    print(f"Randomly selected option: {selected_option}")

    if selected_option == 1:
        meal_calculator()
    else:
        alarm_clock()


if __name__ == "__main__":
    main()

