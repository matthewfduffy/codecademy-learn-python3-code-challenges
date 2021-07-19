# 4. Divisible by Ten
# Create a function called divisible_by_ten() that has one parameter named num.
# The function should return True if num is divisible by 10, and False otherwise. Consider using modulo operator % to check for divisibility.

# Option 1:
def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False


# Option 2 - with ternary operator:
def divisible_by_ten(num):
    return True if num % 10 == 0 else False

print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False