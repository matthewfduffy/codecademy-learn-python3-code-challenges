# 4. Movie Review
# Create a function named movie_review() that has one parameter named rating.

# If rating is less than or equal to 5, return "Avoid at all costs!". If rating is between 5 and 9, return "This one was fun.". If rating is 9 or above, return "Outstanding!"


# Option 1:
def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif rating > 5 and rating <= 8:
        return "This one was fun"
    else:
        return "Outstanding!"


# Option 2 - using Switch-Case Statements **Python 3.10 or later**:
def movie_review(rating):
    match rating:
        case rating <= 5:
            return "Avoid at all costs!"
        case rating > 5 and rating <= 8:
            return "This one was fun"
        case rating >= 9:
            return "Outstanding!"

            
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."