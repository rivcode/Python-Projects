# In this project, the user's monthly savings is calculated by calculating their monthly income and total monthly expenses.

# Prompt to enter monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt to enter total monthly rent
monthly_rent = float(input("Enter your monthly rent: "))

# Prompt to enter total monthly grocery expense
monthly_groceryexpenses = float(input("Enter your grocery expenses: "))

# Prompt to enter total internet bill
monthly_internetbill = float(input("Enter your internet bill: "))

# Prompt to enter personal cell phone bill 
monthly_cellphonebill = float(input("Enter your cell phone bill: "))

# Prompt to enter the cost for personal subscriptions such as Netflix, Amazon, 
monthly_subscriptions = float(input("Enter your miscellaneous expenses: "))

# Calculate total expenses
total_expenses = monthly_rent + monthly_groceryexpenses + monthly_internetbill + monthly_cellphonebill + monthly_subscriptions

# Calculate monthly saving and print it 2 decimal places.
savings = monthly_income - total_expenses

# Print Statement
print("Your monthly saving is " + str(round(savings, 2)))