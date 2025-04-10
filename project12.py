logo = """
   _____                       _   _            _   _                 _               
  / ____|                     | | | |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_| 
                                                                                   """

print(logo)

from random import randint

EASY_LVL_TURNS = 10
HARD_LVL_TURNS = 5

def check_answer(user_guess,actual_answer,turns):
    """check answer against  guess, returns the number of turns remaining"""
    if user_guess > actual_answer:
        print("Too High")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"you got it! the answer was: {actual_answer}")     
        
def set_difficulty():
    level = input("choose difficulty type 'easy' or 'hard': ") 
    if level.lower() == "easy":
        return EASY_LVL_TURNS
    elif level.lower() == "hard":
        return HARD_LVL_TURNS

def game():
    print("Welcome to the number guessing game!")  
    print("I am thinking between a number 1 and  100") 
    answer = randint(1,100)
    #print(f"psst the correct answer is {answer}")
                                                    
    turns = set_difficulty()
    guess = 0 
    while guess != answer:
        print(f"You have {turns} attempts  remaining to guess the number")
        guess = int(input("Make a Guess: "))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out of guesses, you lose!")
            break
        elif guess != answer:
            print("Guess again!")

game()