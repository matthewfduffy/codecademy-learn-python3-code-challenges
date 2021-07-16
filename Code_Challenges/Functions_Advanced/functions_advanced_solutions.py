# 1. First Three Multiples (1_first_three_multiples.py)
def first_three_multiples(num):
  print(num)
  print(num * 2)
  print(num * 3)
  return num * 3
  

# 2. Tip (2_tip.py)
def tip(total, percentage):
  tip_amount = (total * percentage) / 100
  return tip_amount


# 3. Bond, James Bond (3_james_bond.py)
def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name


# 4. Dog Years (4_dog_years.py)
def dog_years(name, age):
  return name+", you are "+str(age * 7)+" years old in dog years"