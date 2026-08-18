# CSC500 Module 2 Portfolio Milestone
# Project Initialization and Variable Setup

# Get user inputs
item_name = input("Enter the item name: ")
item_price = float(input("Enter the item price: $"))
item_quantity = int(input("Enter the item quantity: "))

# Calculate the subtotal
subtotal = item_price * item_quantity

# Calculate the total quantity cost after a simple 10% discount
discount_percent = 10
discount_amount = subtotal * discount_percent
total = subtotal - discount_amount

# Display the results
print("Item:", item_name)
print("Quantity:", item_quantity)
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: ${discount_amount:.2f}")
print(f"Total: ${total:.2f}")
