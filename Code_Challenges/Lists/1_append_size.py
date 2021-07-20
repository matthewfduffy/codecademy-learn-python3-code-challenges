# 1. Append Size
# The function should append the size of lst (inclusive) to the end of lst. The function should then return this new list.

# For example, if lst was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of lst was originally 3.

# Option 1:
def append_size(lst):
    new_lst = [n for n in lst]
    new_lst.append(len(lst))
    return new_lst


# Option 2 - with copy() method:
def append_size(lst):
    new_lst = lst.copy()
    new_lst.append(len(lst))
    return new_lst



print(append_size([23, 42, 108]))