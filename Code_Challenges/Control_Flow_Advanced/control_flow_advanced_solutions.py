# 1. In Range
def in_range(num, lower, upper):
  if(num >= lower and num <= upper):
    return True
  return False


# 2. Same Name
def same_name(your_name, my_name):
  if (your_name == my_name):
    return True
  else:
    return False


# 3. Always False
def always_false(num):
  if (num > 0 and num < 0):
    return True
  else:
    return False


# 4. Movie Review
def movie_review(rating):
  if(rating <= 5):
    return "Avoid at all costs!"
  if(rating < 9):
    return "This one was fun."
  return "Outstanding!"


# 5. Max Number
def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"