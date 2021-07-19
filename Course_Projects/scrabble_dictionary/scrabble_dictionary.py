"""
    # Scrabble Dictionary

    In this project, you will process some data from a group of friends playing scrabble. 
    You will use dictionaries to organize players, words, and points.

    Two lists are provided, letters and points. 
    Combine these two into a dictionary that would map a letter to its point value.
"""
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
            "U", "V", "W", "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# using zip and list comprehension to create a mapping between letters and points
letters_to_points = dict(zip(letters, points))

# adding an option for blank tiles
letters_to_points[' '] = 0

# create a function that will take in a word and return how many points that word is worth
def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letters_to_points.get(letter.upper())
    return point_total

# Scoring a Game - Creating a dictionary that maps players to a list of words they have played
player_to_words = {
                    "player1": ["BLUE", "TENNIS", "EXIT"],
                    "wordNerd": ["EARTH", "EYES", "MACHINE"],
                    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
                    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

player_to_points = {}

for player in player_to_words:
    player_points = 0
    for word in player_to_words:
        player_points += score_word(word)
        print(player_points)

# For Testing
# print(letters_to_points)
# print(score_word("brownie"))