# 1. Check Name
def check_for_name(sentence, name):
  return name.lower() in sentence.lower()

  
# 2. Every Other Letter
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other


# 3. Reverse
def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse


# 4. Make Spoonerism
def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+" "+word1[0]+word2[1:]


# 5. Add Exclamation
def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word