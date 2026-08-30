# CSC500 Module 6 Portfolio Milestone
#
# Online Shopping Cart - Part Deux
#
# This program creates an ItemToPurchase, ShoppingCart, and RetailStore
# class. The user can add, remove, modify, and display items
# through a menu-driven interface.

from datetime import datetime
from dateutil import parser
from dateutil.relativedelta import relativedelta

class ItemToPurchase:
    def init(self, item_name="none", item_price=0.0, item_quantity=0):
        # Note: Intro level class, assuming valid values passed
        # Production code would re-validate inputs
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        item_total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${item_total:.2f}")

class ShoppingCart:
    def __init__(
        self,
        customer_name="none",
        order_date=None,
        current_date="January 1, 2020"
    ):
        self.customer_name = customer_name

        if order_date is None:
            order_date = datetime.now()

        self.order_date = order_date
        self.cart_items = []

        # Required by assignment:
        # current_date must be a string and default to
        # "January 1, 2020".
        self.current_date = current_date

    # ============================================================
    # CORE SHOPPING CART METHODS - REQUIRED BY ASSIGNMENT
    # ============================================================

    # Add an ItemToPurchase object to the shopping cart
    def add_item(self, item: ItemToPurchase) -> bool:
        self.cart_items.append(item)
        return True

    # Remove item(s) from the shopping cart by name
    def remove_item(self, item_name: str) -> bool:
        # Remove all items matching item_name.
        # Comparison ignores case and surrounding whitespace.

        search_name = item_name.strip().lower()
        removed_items = []
        remaining_items = []

        for item in self.cart_items:
            if item.item_name.strip().lower() == search_name:
                removed_items.append(item)
            else:
                remaining_items.append(item)

        self.cart_items = remaining_items

        if not removed_items:
            print("Item not found in cart. Nothing removed.")
            return False

        if len(removed_items) > 1:
            print(
                f"Warning: Removed {len(removed_items)} "
                f"matching items: {removed_items}."
            )

        return True

    # Modify an existing ItemToPurchase object in the shopping cart
    def modify_item(self, moditem: ItemToPurchase) -> bool:
        if not self.is_incart(moditem):
            print("Item not found in cart. Nothing modified.")
            return False

        # Remove the existing item(s)
        if not self.remove_item(moditem.item_name):
            print("Error deleting item.")
            return False

        # Add the updated item
        self.cart_items.append(moditem)

        return True

    # Return the total quantity of all items
    def get_num_items_in_cart(self) -> int:
        total_quantity = 0

        for item in self.cart_items:
            total_quantity += item.item_quantity

        return total_quantity

    # Return the total cost of all items
    def get_cost_of_cart(self) -> float:
        total_cost = 0.0

        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity

        return total_cost

    # Print the contents and total cost of the cart
    def print_total(self):
        print(
            f"\n{self.customer_name}'s Shopping Cart - "
            f"{self.current_date}"
        )
        print("****************************************")

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return

        for item in self.cart_items:
            item.print_item_cost()

        print("----------------------------------------")
        print(f"Total Items: {self.get_num_items_in_cart()}")
        print(f"Total: ${self.get_cost_of_cart():.2f}")

    # Print descriptions of all items in the cart
    def print_descriptions(self):
        print(
            f"\n{self.customer_name}'s Shopping Cart - "
            f"{self.current_date}"
        )
        print("****************************************")
        print("Item Descriptions")

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return

        for item in self.cart_items:
            print(item.item_name)

    # ============================================================
    # UTILITY METHODS
    # ============================================================

    # Check if an item is in the cart
    def is_incart(self, item):
        # Input may be a string containing an item name
        # or an ItemToPurchase object.

        if isinstance(item, str):
            item_name = item

        elif isinstance(item, ItemToPurchase):
            item_name = item.item_name

        else:
            print(
                "Warning: is_incart() requires a string "
                "or ItemToPurchase object."
            )
            return False

        matches = []

        for cart_item in self.cart_items:
            if cart_item.item_name.lower() == item_name.lower():
                matches.append(cart_item.item_name)

        if len(matches) == 1:
            return True

        if len(matches) == 0:
            return False

        print(f"There were more than one match: {matches}")
        return True

    # Find an item by name
    def get_item_byname(self, item):
        # Input may be a string containing an item name
        # or an ItemToPurchase object.

        if isinstance(item, str):
            item_name = item

        elif isinstance(item, ItemToPurchase):
            item_name = item.item_name

        else:
            print(
                "Warning: get_item_byname() requires a string "
                "or ItemToPurchase object."
            )
            return False

        if not self.is_incart(item):
            return False

        for cart_item in self.cart_items:
            if (
                cart_item.item_name.strip().lower()
                == item_name.strip().lower()
            ):
                return cart_item

        # Should never reach here
        print("Error finding item by name")
        return False

    # ============================================================
    # USER INPUT / INTERFACE METHODS
    # ============================================================

    # Add an item to the shopping cart by querying user for info
    def get_info_to_add_item(self):
        print("\nAdding item to cart")

        while True:
            try:
                item_name = input("Enter item name: ")

                if item_name.strip() == "":
                    print("No item name entered, aborting entry")
                    return None

                # Check if item already in cart
                if self.is_incart(item_name):
                    print(
                        "You already have that item in the cart. "
                        "Use the modify function to change it."
                    )
                    return None

                item_price = float(input("Enter item price: $"))

                if item_price <= 0.0:
                    raise ValueError("Item price must be positive")

                item_quantity = int(input("Enter item quantity: "))

                if item_quantity <= 0:
                    raise ValueError("Item quantity must be positive")

                item = ItemToPurchase(
                    item_name,
                    item_price,
                    item_quantity
                )

                self.add_item(item)

                print(f"{item_name} added to cart.")
                return item

            except ValueError as error:
                print(f"Invalid input: {error}")
                print(
                    "Try again. Enter a blank item name to abort."
                )

    # Remove an item from the shopping cart by asking user for name
    def get_name_to_remove(self):
        print("\nRemove Item")

        item_name = input("Enter item name to remove: ")

        return self.remove_item(item_name)

    # Get a valid quantity from the user
    def get_valid_quantity(self, maxval=100):
        # Returns an int between 0 and maxval-1.
        # Returns -1 if the user wants to abort.

        while True:
            try:
                new_q = int(input("Enter new quantity: "))

                if new_q < 0:
                    return -1

                if new_q < maxval:
                    return new_q

                print(
                    f"The website cannot handle that amount. "
                    f"Enter less than {maxval}"
                )

            except ValueError:
                print(
                    "Please try again with a valid integer. "
                    "Enter -1 to abort."
                )

    # Get item information from the user and change its quantity
    def change_item_quantity(self):
        print("\nCHANGE ITEM QUANTITY")

        item_name = input("Enter item name: ").strip()
        quant_item = self.get_item_byname(item_name)

        if not quant_item:
            print(
                f"Item {item_name} not found in cart, "
                "nothing to change"
            )
            return False

        # Get the new quantity (-1 == abort)
        new_quantity = self.get_valid_quantity()

        if new_quantity < 0:
            print("Aborting quantity update")
            return False

        # Treat zero as a request to remove the item
        if new_quantity == 0:
            print("Quantity of zero requested, removing from cart")
            return self.remove_item(item_name)

        # Create a new item with the same attributes
        # except for the new quantity.
        modified_item = ItemToPurchase(
            quant_item.item_name,
            quant_item.item_price,
            new_quantity
        )

        return self.modify_item(modified_item)

# Main Retail Store class. 
# At this point just has one shopping cart for one customer
# But could be easily scaled.
class RetailStore:
    def init(self, store_name="Crazy DarF's Bargain Sprockets"):
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
    def get_purchase_date():
        # Prompt gives an example of a day a week in the future
        example_date = (datetime.now() + timedelta(days=7)).strftime("%m/%d/%Y") 
        while True:
            try:
                now = datetime.now()
                date_text = input(f"Enter order date (e.g., {example_date}) or ENTER for ASAP: ").strip()
            
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
                    raise ValueError("The date cannot be more than one year in the future.")
                # Passed test, return as datetime object
                return purchase_date

        except (ValueError, OverflowError) as error:
            print(f"Invalid date: {error}")
            print("Please enter a valid date between today and one year from today.")

    # Get customer information and update the shopping cart
    def get_customer_info(self):
        # Print friendly message and ask for info
        print(f"Welcome to {self.store_name}!")
        # Ask for their name
        self.cart.customer_name = self.validate_customer_name()       
        self.cart.order_date = self.get_purchase_date()
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
                self.cart.add_item()
    
            elif choice == "r":
                self.cart.remove_item()
    
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
    store.display_menu()

if name == "main":
main()
