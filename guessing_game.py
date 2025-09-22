def guessing_game():
    answer=15
    correct=0
    while (correct=0):
        skibidiGyat=int(input())
        if(skibidiGyat==answer):
            correct=1
            return "Congratulations! You guessed it!"
        elif(skibidiGyat<answer):
            return "Too Low! Guess again."
        elif(skibidiGyat>answer):
            return "Too High! Guess again."

