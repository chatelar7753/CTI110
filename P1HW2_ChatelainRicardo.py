# Ricardo Chatelain
# September 14, 2026
# P1HW2 - Travel Expense Calculator
# This program asks the user for their budget and travel expenses (gas,
# accommodation, and food), then adds up the expenses, subtracts them
# from the budget, and displays the remaining balance.

# Pseudocode:
# 1. Print a short description of the program
# 2. Ask the user for their budget
# 3. Ask the user for their travel destination
# 4. Ask the user how much they will spend on gas
# 5. Ask the user how much they will spend on accommodation
# 6. Ask the user how much they will spend on food
# 7. Add up gas, accommodation, and food to get total expenses
# 8. Subtract total expenses from the budget to get the remaining balance
# 9. Display the destination, budget, each expense, and the remaining balance

print("This program calculates and displays travel expenses")
print()

budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
accommodation = int(input("Approximately, how much will you need for accomodation/hotel? "))
food = int(input("Last, how much do you need for food? "))

total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

print()
print("-------------Travel Expenses-------------")
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accomodation:", accommodation)
print("Food:", food)
print()
print("Remaining Balance:", remaining_balance)