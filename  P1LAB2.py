# Ricardo Chatelain
# September 8, 2026
# P1LAB2 - Product Sales
# A program that demonstrates Input, Processing, and Output by calculating product sales.

# Input
product_name = input("Enter the product name: ")
count = int(input("Enter the quantity: "))
unit_price = float(input("Enter the unit price in USD: "))

# Processing
total = count * unit_price

# Output
print("\nWelcome to the Sales Receipt Program")
print(f"Product: {product_name}")
print(f"Quantity: {count}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Total Price: ${total:.2f}")
