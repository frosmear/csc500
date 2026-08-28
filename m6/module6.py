# CSC500 Module 6 Portfolio Milestone
#
# Online Shopping Cart - Part 2
#
# This program creates an ItemToPurchase class and a ShoppingCart
# class. The user can add, remove, modify, and display items
# through a menu-driven interface.

from datetime import datetime

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        item_total = self.item_price * self.item_quantity
        print(
            f"{self.item_name} {self.item_quantity} @ "
            f"${self.item_price:.2f} = ${item_total:.2f}"
        )


class ShoppingCart:
    def __init__(self,customer_name="none",current_date=None):
        self.customer_name = customer_name
        if current_date is None:
             current_date = datetime.now()
        self.current_date = current_date
        self.cart_items = []

    # Add an item to the shopping cart
    def add_item(self, item):
        self.cart_items.append(item)

    # Remove an item from the shopping cart by name
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return

        print("Item not found in cart. Nothing removed.")

    # Modify an existing item in the shopping cart
    def modify_item(self, item):
        for existing_item in self.cart_items:
            if existing_item.item_name == item.item_name:
                existing_item.item_price = item.item_price
                existing_item.item_quantity = item.item_quantity
                return

        print("Item not found in cart. Nothing modified.")

    # Return the total quantity of all items
    def get_num_items_in_cart(self):
        total_quantity = 0

        for item in self.cart_items:
            total_quantity += item.item_quantity

        return total_quantity

    # Return the total cost of all items
    def get_cost_of_cart(self):
        total_cost = 0.0

        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity

        return total_cost

    # Print the contents and total cost of the cart
    def print_total(self):
        print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
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
        print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("****************************************")
        print("Item Descriptions")

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return

        for item in self.cart_items:
            print(item.item_name)


def print_menu(cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output item descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        choice = input("Choose an option: ").strip().lower()

        if choice == "a":
            print("\nADD ITEM")
            item_name = input("Enter item name: ")

            try:
                item_price = float(input("Enter item price: $"))
                item_quantity = int(input("Enter item quantity: "))

                new_item = ItemToPurchase(
                    item_name,
                    item_price,
                    item_quantity
                )

                cart.add_item(new_item)
                print(f"{item_name} added to cart.")

            except ValueError:
                print("Invalid input. Item was not added.")

        elif choice == "r":
            print("\nREMOVE ITEM")
            item_name = input("Enter item name to remove: ")
            cart.remove_item(item_name)

        elif choice == "c":
            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter item name: ")

            try:
                new_quantity = int(input("Enter new quantity: "))

                modified_item = ItemToPurchase(
                    item_name,
                    0.0,
                    new_quantity
                )

                cart.modify_item(modified_item)

            except ValueError:
                print("Invalid quantity.")

        elif choice == "i":
            cart.print_descriptions()

        elif choice == "o":
            cart.print_total()

        elif choice == "q":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


def main():
    print("ONLINE SHOPPING CART")

    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")

    cart = ShoppingCart(customer_name, current_date)

    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    print_menu(cart)


if __name__ == "__main__":
    main()
