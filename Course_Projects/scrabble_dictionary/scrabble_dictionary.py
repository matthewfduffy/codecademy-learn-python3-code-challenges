letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = dict(zip(letters, points))

letters_to_points[" "] = 0
# print(letters_to_points)

def score_word(word):
    point_total = 0
    for letter in word:
      point_total += letters_to_points.get(letter.upper(), 0)
    #   print(f"The current letter is: {letter}. The current total is: {point_total}.")
    return point_total


# brownie_points = score_word("BROWNIE")
# print(brownie_points)

player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"],
  "wordNerd": ["EARTH", "EYES", "MACHINE"],
  "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]
  }

player_to_points = {}
  
for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        x = score_word(word)
        player_points += x
        print(f"{player}, {player_points}")
    player_to_points[player] = player_points
    print("------")
    for each_key, each_value in player_to_points.items():
        print(f"{each_key}, {each_value}")



# If you want extended practice, try to implement some of these ideas with the Python you’ve learned:

#     play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played
#     update_point_totals() — turn your nested loops into a function that you can call any time a word is played
#     make your letter_to_points dictionary able to handle lowercase inputs as well

