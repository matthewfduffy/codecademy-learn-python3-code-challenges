# 1. In Range
# Create a function named in_range() that has three parameters named num, lower, and upper.

# The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.

# Option 1:
def in_range(num, lower, upper):
    if num >= lower and num <= upper:
        return True
    else:
        return False


print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False