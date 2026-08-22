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

class ShoppingCart:
     def __init__(self, store_name="Crazy DarFs"):
          self.store_name=store_name
          self.cart_items = []

     def add_itmes(self):
          # Add items to cart until the user enters quit
          # Returns a count of items added
          item_count = 0
          while True:
               newitem = self.get_shopping_cart_item()
               if newitem is None:
                    return item_count
               # Add the item to the shopping cart
               self.cart_item.append(newitem)
               item_count += 1
         
     def get_shopping_cart_item(self):
          # Function that prompts user for input of an item
          # Returns either an ItemToPurchase object
          # or None if the user declines
          #    
          # Note: The instructions explicitly say the string quit but thats a poor idea in practice
          # What if a user wants to buy 5 quilts and just typos
          # I'd just make it a blank string - less typing - so this implementation quits on either
          while True:
               try:
                    if item_name.strip().lower() in ("quit", ""):
                         return None
                    item_price = float(input("Enter the item price ($): "))
                    item_quantity = int(input("Enter the item quantity: "))
                    # Return ItemToPurchase object
                         return ItemToPurchase(item_name, item_price, item_quantity)
               except:
                    print("Invalid inputs. Do it over")
     
     def print_cart_contents(self)
          # Calculate the total cost
          self.cart_total = 0.0
     
          for item in self.cart_items:
               self.cart_total = self.cart_total + (item.item_price * item.item_quantity)
     
          # Display the results
          print("\n{self.store_name}")
          print("******************")
     
          for item in self.cart_items:
               item.print_item_cost()
     
          print(f"Total: ${self.cart_total}")

def main():
     # Create an empty shopping cart
     cart = ShoppingCart()

     # Add items to it
     cart.add_itmes()

     # Print the receipt view
     cart.print_cart_contents()

if __name__ == "__main__":
    main()
