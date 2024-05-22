import random
choices = ['r', 'p', 's']
ATTEMPT = 1
def play():
    global ATTEMPT
    ATTEMPT
    try:
        user_guess = str(input("Enter ROCK > [R] OR PAPER > [P] OR SCISSOR > [S]")).lower()
    except Exception as ex:
        print("Wrong Input")
        user_guess = str(input("Enter ROCK > [R] OR PAPER > [P] OR SCISSOR > [S]")).lower()
    bot = random.choice(choices)
    bot_guess = bot[0]

    if (bot_guess =="r" and user_guess =="p") or (bot_guess =="p" and user_guess =="s") or(bot_guess =="s" and user_guess=="r"):
        print("You Won")
        print("---------------------------------------------------------")
        print(f"You took {ATTEMPT} attempts")
        winner = True
    else:
        
        if bot_guess ==user_guess:
            winner = False
            print("Draw")
        else:
            ATTEMPT +=1
            print("You lose")
            print(f"Your guess was {user_guess} and bot guess was {bot_guess}")
            winner = False
    return winner

while not play():
    continue