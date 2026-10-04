from datetime import datetime, timedelta
from dateutil import parser

from shopping_cart import ShoppingCart


class RetailStore:
    def __init__(self, store_name="Crazy DarF's Bargain Sprockets"):
        self.store_name = store_name
        self.cart = ShoppingCart()

    # Define a name validation method
    # This simply makes sure its not empty but in production code would check for repeats
    # and that is not fake like a Moe's Tavern customer
    def validate_customer_name(self):
        while True:
            customer_name = input("Enter customer's name: ").strip()

            if customer_name:
                return customer_name

            print("Customer name cannot be empty.")

    # Define a method to select a purchase date
    # Defaults to now if enter is pressed
    # Enforces it between now and a year from now
    def get_purchase_date(self):
        # Prompt gives an example of a day a week in the future
        example_date = (
            datetime.now() + timedelta(days=7)
        ).strftime("%m/%d/%Y")

        while True:
            try:
                now = datetime.now()

                date_text = input(
                    f"Enter order date (e.g., {example_date}) "
                    "or ENTER for ASAP: "
                ).strip()

                # Blank input defaults to the current date/time
                if date_text == "":
                    return now

                # Parse the input
                purchase_date = parser.parse(date_text)

                # If the user entered today in any reasonable format,
                # use the current date/time rather than midnight.
                if purchase_date.date() == now.date():
                    return now

                # Compare to make sure not in the past
                if purchase_date < now:
                    raise ValueError("The date cannot be in the past.")

                # Make sure its not too far in the future
                one_year_from_now = now + timedelta(days=365)

                if purchase_date > one_year_from_now:
                    raise ValueError(
                        "The date cannot be more than one year in the future."
                    )

                # Passed test, return as datetime object
                return purchase_date

            except (ValueError, OverflowError) as error:
                print(f"Invalid date: {error}")
                print(
                    "Please enter a valid date between today "
                    "and one year from today."
                )

    # Get customer information and update the shopping cart
    def get_customer_info(self):
        # Print friendly message and ask for info
        print(f"Welcome to {self.store_name}!")

        # Ask for their name
        self.cart.customer_name = self.validate_customer_name()

        purchase_date = self.get_purchase_date()
        self.cart.current_date = purchase_date.strftime("%B %d, %Y")

        return True

    def print_customer(self):
        print(f"\nCustomer name: {self.cart.customer_name}")
        print(f"Order date: {self.cart.current_date}")

    def generate_menu_text(self):
        # Separates print statements from logic loop
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output item descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        return True

    # Display the shopping cart menu and process user selections
    def print_menu(self):
        while True:
            self.generate_menu_text()
            choice = input("Choose an option: ").strip().lower()

            if choice == "q":
                print("Goodbye!")
                return True

            elif choice == "a":
                self.cart.get_info_to_add_item()

            elif choice == "r":
                self.cart.get_name_to_remove()

            elif choice == "c":
                self.cart.change_item_quantity()

            elif choice == "i":
                self.cart.print_descriptions()

            elif choice == "o":
                self.cart.print_total()

            else:
                print("Invalid option. Please try again.")


# Main Program loop
def main():
    store = RetailStore()
    store.get_customer_info()
    store.print_menu()


if __name__ == "__main__":
    main()
