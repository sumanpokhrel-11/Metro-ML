import random
ATTEMPT = 1
def guess_number(num_to_guess):
    try:
        user_guess = int(input("Enter the Number between 1 to 10: "))
    except Exception as ex:
        print("Enter digits only")
        user_guess = int(input("Enter the Number between 1 to 10: "))
    global ATTEMPT
    ATTEMPT
    if num_to_guess == user_guess:
        winner = True
        print("You Won!!")
        print(f"YOU TOOK {ATTEMPT} ATTEMPTS TO WIN")
        
        
    else:
        
        ATTEMPT += 1
        winner = False
        if num_to_guess<user_guess:
            print("Guess Lower")
        elif num_to_guess>user_guess:
            print("Guess Higher")
        else:
            print("Enter number only")
    return winner

num_to_guess = random.randint(1,10)
while not guess_number(num_to_guess):
    continue
    
    
    
