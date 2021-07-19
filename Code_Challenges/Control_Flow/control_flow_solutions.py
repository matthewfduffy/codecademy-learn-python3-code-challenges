# 1. Large Power
def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else:
    return False


# 2. Over Budget
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if (budget < food_bill + electricity_bill + internet_bill + rent):
    return True
  else:
    return False


# 3. Twice as Large
def twice_as_large(num1, num2):
  if num1 > 2 * num2:
    return True
  else:
    return False