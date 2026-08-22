# CSC500 Module 4 Portfolio Milestone

"""
Instructions from assignment: 
Create a class named ItemToPurchase with the following specifications:

Attributes:
 * item_name (string)
 * item_price (float)
 * item_quantity (int)

Default Constructor:
 * Initializes item_name = "none", item_price = 0.0, and item_quantity = 0.

Method:
 * print_item_cost(): Outputs the item name, quantity, and total cost in the following format:
     example: Bottled Water 10 @ $1.0 = $10.0
"""
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name # I hate using the word none in a string in Python but instructions said so
        self.item_price = item_price
        self.item_quantity = item_quantity

    # Calculate the cost
    def print_item_cost(self):
        item_total = self.item_price * self.item_quantity
        print(f"{self.item_quantity} x {self.item_name} @ ${self.item_price} = ${item_total}")

def get_user_input():
  # 


def main():
    # Create an empty shopping cart
    shopping_cart = []

    # Get items until the user enters quit
    while True:
        item_name = input("Enter the item name or quit to finish: ")

        if item_name.strip().lower() == "quit":
            break

        input_good = False
        while not input_good:
            try:
                item_price = float(input("Enter the item price: $"))
                item_quantity = int(input("Enter the item quantity: "))
                input_good = True
            except:
                # intro class, not worried about proper exceptions
                print("Invalid inputs. Do it over")

        # Create an ItemToPurchase object
        item = ItemToPurchase(item_name, item_price, item_quantity)

        # Add the item to the shopping cart
        shopping_cart.append(item)

    # Calculate the total cost
    total = 0.0

    for item in shopping_cart:
        total = total + (item.item_price * item.item_quantity)

    # Display the results
    print("\nTOTAL COST")
    print("******************")

    for item in shopping_cart:
        item.print_item_cost()

    print(f"Total: ${total}")


if __name__ == "__main__":
    main()
