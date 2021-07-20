# 5. Combine Sort
# Write a function named combine_sort that has two parameters named lst1 and lst2.

# The function should combine these two lists into one new list and sort the result. Return the new sorted list.

# Option 1:
def combine_sort(lst1, lst2):
    new_lst = []

    for i in lst1:
        new_lst.append(i)
    for j in lst2:
        new_lst.append(j)
    
    new_lst.sort()
    return new_lst


print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
# should return [-10, 2, 2, 4, 5, 5, 10, 10]