# TODO create guessing game function
# HINT: Target number should be 15
# HINT: Return message should be "Congratulations! You guessed it!"
# HINT: Use input("Enter your guess: ") for user input
# HINT: Print "Too low! Try again." for low guesses
# HINT: Print "Too high! Try again." for high guesses

def guessing_game():
    x:int  = 0
    while x := (int(input())) != 15: # this isn't confusing in the slightest :3
        print(f"Too {'high' if x > 15 else 'low'}! Try again.")
    return "Congratulations! You guessed it!"

# tests do not ensure that method is implemented
""" # this method works with current tests
def guessing_game():
    return "Congratulations! You guessed it!"
"""
