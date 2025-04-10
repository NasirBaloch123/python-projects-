log = """
 _   _ _       _               
| | | (_) __ _| |__   ___ _ __ 
| |_| | |/ _` | '_ \ / _ \ '__|
|  _  | | (_| | | | |  __/ |   
|_| |_|_|\__, |_| |_|\___|_|   
| |    __|___/    _____ _ __   
| |   / _ \ \ /\ / / _ \ '__|  
| |__| (_) \ V  V /  __/ |     
|_____\___/ \_/\_/ \___|_|     
"""


vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
print(log)
from game_data import data
import random


def format_data(account):
        """Takes the account data and return into printable format."""
        account_name = account["name"]
        account_desc = account["description"]
        account_country = account["country"]
        return(f"{account_name} , a {account_desc} , from {account_country}")

def check_answer(user_guess,a_followers,b_followers):
    """Take a user 's guess and the followers counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
score = 0
game_Continue = True 
account_b = random.choice(data)
while game_Continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)
        
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.") 

    guess = input("Who has more followers? Type 'A' or 'B': ").lower() 
    print("\n" * 20)
    print(log)
    a_follwer_count = account_a["follower_count"]  
    b_follwer_count = account_b["follower_count"]  
    is_correct = check_answer(guess,a_follwer_count,b_follwer_count)
    if is_correct:
        score +=1
        print(f"you are right! Current score {score}")
    else:
        print(f"Sorry , that 's wrong. Final score {score}")
        game_Continue = False