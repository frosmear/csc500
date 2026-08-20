# CSC500 Module 2 Portfolio Milestone

# Project Initialization and Variable Setup
discount_percent = 10 

# Get and validate user inputs
input_good = False
while not input_good:
    try:
        item_name = input("Enter the item name: ")
        item_price = float(input("Enter the item price: $"))
        item_quantity = int(input("Enter the item quantity: "))
        input_good = True
    except:
        # intro class, not worried about proper exceptions
        print("Invalid inputs.  Do it over")

# Calculate the subtotal
subtotal = item_price * item_quantity

# Calculate the total quantity cost after a simple 10% discount
discount_amount = subtotal * (discount_percent/100)
total = subtotal - discount_amount

# Display the results
print("\nResults:\n******************")
print(f"Item: {item_name}")
print(f"Quantity: {item_quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: ${discount_amount:.2f}")
print(f"Total: ${total:.2f}")
