"""
    1. Larger Sum

    Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

    The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

"""
# Option 1:
# def larger_sum(lst1, lst2):
#     sum_of_lst1 = 0
#     sum_of_lst2 = 0
#     for num1 in lst1:
#         sum_of_lst1 += num1
        
#     for num2 in lst2:
#         sum_of_lst2 += num2
    
#     if sum_of_lst1 > sum_of_lst2:
#         return sum_of_lst1
#     else:
#         return sum_of_lst2


# Option 2 - Without Loops:
# def larger_sum(lst1, lst2):
#     if sum(lst1) > sum(lst2):
#         return sum(lst1)
#     else:
#         return (lst2)


# Option 3 - Using Terinary Operator:
def larger_sum(lst1, lst2):
    return sum(lst1) if sum(lst1) > sum(lst2) else sum(lst2)


#Uncomment the line below when your function is done
output = larger_sum([1, 9, 5], [2, 3, 7])
print(output)