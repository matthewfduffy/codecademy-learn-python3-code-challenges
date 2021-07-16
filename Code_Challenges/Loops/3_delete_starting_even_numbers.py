"""
    3. Delete Starting Even Numbers

    Write a function called delete_starting_evens() that has a parameter named lst.

    The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.

    For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].

    Make sure your function works even if every element in the list is even!
"""
# Option 1:
def delete_starting_evens(lst):
    index = 0

    for num in lst:
        if num % 2 == 0:
            del lst[index]
        index += 1
    
    return lst



print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))