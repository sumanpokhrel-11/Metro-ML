import random

win = False
num_to_guess = random.randint(1,10)
user_guess = int(input("Enter the Number between 1 to 10: "))


while not win:
    if num_to_guess == user_guess:
        print("You Won!!")
        win = True
    else:
        win = False
        if num_to_guess<user_guess:
            print("Guess Lower")
        elif num_to_guess>user_guess:
            print("Guess Higher")
        else:
            print("Enter number only")