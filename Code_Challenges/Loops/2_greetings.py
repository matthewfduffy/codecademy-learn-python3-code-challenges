"""
    2. Greetings
    Create a function named add_greetings() which takes a list of strings named names as a parameter.

    In the function, create an empty list that will contain each greeting. Add the string 'Hello, ' in front of each name in names and append the greeting to the list.

    Return the new list containing the greetings.
"""
# Option 1:
def add_greetings(names):
    greeting_list = []

    for name in names:
        greeting_list.append("Hello, " + name)
    
    return greeting_list


print(add_greetings(["Owen", "Max", "Sophie"]))