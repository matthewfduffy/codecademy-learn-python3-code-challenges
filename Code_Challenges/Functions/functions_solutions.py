# 1. Tenth Power (1_tenth_power.py)
def tenth_power(num):
  return num ** 10


# 2. Square Root (2_square_root.py)
def square_root(num):
  return num ** 0.5
#one half power of the input value is mathmatically equivalent to returning the square root


# 3. Win Percentage (3_win_percentage.py)
def win_percentage(wins, losses):
  total_games = wins + losses
  ratio_won = wins / total_games
  return ratio_won * 100


# 4. Average (4_average.py)
def average(num1, num2):
  return (num1 + num2) / 2


# 5. Remainder (5_remainder.py) 
def remainder(num1, num2):
  return (2 * num1) % (num2 / 2)