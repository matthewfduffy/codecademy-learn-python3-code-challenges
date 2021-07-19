# 5. Max Number
# Create a function called max_num() that has three parameters named num1, num2, and num3.

# The function should return the largest of these three numbers. If any of two numbers tie as the largest, you should return "It's a tie!".

# Option 1:
def max_num(num1, num2, num3):
    current_max = num1
    if num1 == num2 or num1 == num3 or num2 == num3:
        return "It's a tie!"
    else:               
        if num2 > current_max:
            current_max = num2
        if num3 > current_max:
            return num3
# TODO 
Revisit and clean solution

# Option 2:
# def max_num(num1, num2, num3):
#     num_list = []
#     num_list.append(num1)
#     num_list.append(num2)
#     num_list.append(num3)
#     num_list.sort()
#     return num_list[-1]




print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"