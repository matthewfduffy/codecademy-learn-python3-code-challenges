"""
    4. Same Values

    Write a function named `same_values()` that takes two lists of numbers of equal size as parameters.

    The function should return a list of the indices where the values were equal in `lst1` and `lst2`.

    For example, the following code should return [0, 2, 3]

    same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])
"""
# Option 1:
def same_values(lst1, lst2):
    new_lst = []
    index = 0
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if i == j:
                new_lst.append(i[index])
        index += 1
    return new_lst


#Uncomment the line below when your function is done
output = same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])
print(output)