"""
    1. First Three Multiples
    Write a function named first_three_multiples() that has one parameter named num.

    This function should print the first three multiples of num. Then, it should return the third multiple.

    For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21.
"""
# Option 1:
# def first_three_multiples(num):
#     print(num)
#     print(num * 2)
#     print(num * 3)
    # return num * 3

# Option 2:
def first_three_multiples(num):
    multiplier = num
    for i in range(2):
        print(multiplier)
        multiplier += num
    print(multiplier)
    return multiplier

print(first_three_multiples(7))
