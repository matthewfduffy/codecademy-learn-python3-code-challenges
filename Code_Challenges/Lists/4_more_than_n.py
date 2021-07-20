# 4. More Than N
# Create a function named more_than_n that has three parameters named lst, item, and n.

# The function should return True if item appears in the list more than n times. The function should return False otherwise.

# Option 1 - basic with for loop and counter:
def more_than_n(lst, item, n):
    counter = 0
    for num in lst:
        if num == item:
            counter += 1
    print("Counter is : ", counter)
    if counter > n:
        return True
    else:
        return False


# Option 2 - using count() and ternary operator:
def more_than_n(lst, item, n):
    x = lst.count(item)
    return True if x > n else False


print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))