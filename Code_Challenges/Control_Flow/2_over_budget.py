# 2. Over Budget
# Create a function called over_budget that has five parameters named budget, food_bill, electricity_bill, internet_bill, and rent.

# The function should return True if budget is less than the sum of the other four parameters — you’ve gone over budget! Return False otherwise.

# Option 1:
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    expenses = food_bill + electricity_bill + internet_bill + rent
    if budget < expenses:
        return True
    else:
        return False


# Option 2 - with ternary operator:
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    expenses = food_bill + electricity_bill + internet_bill + rent
    return True if budget < expenses else False

    
# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True