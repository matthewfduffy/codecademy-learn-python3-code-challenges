# 5 Max Number

# Option 3 - Using reduce():
# see file '5a_max_number_alternate.py'
from functools import reduce

# does not account if a list has two numbers of the same value
def max_num(num1, num2, num3):
    num_list = [num1, num2, num3]
    highest_num = reduce(lambda x,y: x if x > y else y, num_list )
    return highest_num


print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"