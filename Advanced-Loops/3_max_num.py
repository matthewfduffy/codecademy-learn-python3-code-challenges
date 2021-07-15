"""
    3. Max Num
    Create a function named `max_num()` that takes a list of numbers named `nums` as a parameter.
    The function should return the largest number in `nums`

"""
# Option 1 - step-by-step:
def max_num(nums):
    greatest_num = 0
    for num in nums:
        if num > greatest_num:
            greatest_num = num
    return greatest_num


# Option 2 - with built-ins:
def max_num(nums):
    return max(nums)


# Option 3 - via new list sorted:
def max_num(nums):
    new_lst = sorted(nums)
    return new_lst[-1]


#Uncomment the line below when your function is done
output = max_num([50, -10, 0, 75, 20])
print(output)