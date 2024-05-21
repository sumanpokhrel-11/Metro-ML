import random

def guess_number():
    num_to_guess = random.randint(1,10)
    user_guess = int(input("Enter the Number between 1 to 10: "))


    if num_to_guess == user_guess:
        winner = True
        print("You Won!!")
        
        
    else:
        winner = False
        if num_to_guess<user_guess:
            print("Guess Lower")
        elif num_to_guess>user_guess:
            print("Guess Higher")
        else:
            print("Enter number only")
    return winner

while not guess_number():
    guess_number()