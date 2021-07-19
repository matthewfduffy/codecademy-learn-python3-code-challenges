# 2. Same Name
# Create a function named same_name() that has two parameters named your_name and my_name.

# If our names are identical, return True. Otherwise, return False.

# Option 1:
def same_name(your_name, my_name):
    if your_name == my_name:
        return True
    return False

# Option 2 - Sanitizing Input:
def same_name(your_name, my_name):
    if your_name.lower() == my_name.lower():
        return True
    return False

print(same_name("Colby", "Colby"))
# should print True
print(same_name("Colby", "colbY"))
# should print False with Option 1, True with Option 2
print(same_name("Tina", "Amber"))
# should print False