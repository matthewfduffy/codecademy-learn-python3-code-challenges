# 2. Append Sum
# Write a function named append_sum that has one parameter — a list named named lst.

# The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.

# For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8]. 

# Option 1 - using a counter with while loop:
# def append_sum(lst):
#     counter = 0
#     while counter < 3:
#         lst.append((lst[-1] + lst[-2]))
#         counter += 1
#     return lst

# Option 2 - modified while loop with flag:
def append_sum(lst):
    new_lst = lst.copy()

    flag = True
    while flag:
        new_lst.append((new_lst[-1] + new_lst[-2]))
        if (len(new_lst) - len(lst) == len(lst)):
            flag = False
    return new_lst


print(append_sum([1, 1, 2]))