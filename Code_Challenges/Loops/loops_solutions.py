# 1. Divisible by 10 (1_divisible_by_ten.py)
def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count


# 2. Greetings (2_greetings.py)
def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name)
  return new_list


# 3. Delete Starting Even Numbers (3_delete_starting_even_numbers.py)
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst


# 4. Odd Indices (4_odd_indices.py)
def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst


# 5. Exponents (5_exponents.py)
def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst