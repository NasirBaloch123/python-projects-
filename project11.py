logo = """
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /       
| |_) | | (_| | (__|   <| | (_| | (__|   <      
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/   """
                      
print(logo)

import  random
def blackjack():
    """ to return a  random card from deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """take a list of cards and return the score calculated  of the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum (cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    """compare user's score to computer's score and return outcome"""
    if user_score == computer_score:
        return "It's a tie!"
    elif computer_score == 0:
        return "lose,opponent has a Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack!"
    elif computer_score > 21:
        return "You win!"
    elif user_score > 21:
        return "You went over 21 you lose!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose"
    
def play_game():
        user_cards = []
        computer_cards = []
        computer_score =  -1
        user_score = -1
        is_gameover = False
        
        for _ in range (2):
            user_cards.append(blackjack())
            computer_cards.append(blackjack())
        
        while not is_gameover:
            user_score  = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")
            
            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_gameover = True
            else:
                user_choice = input("type 'y' to get  another card or type 'n' to pass? ")
                if user_choice == "y":
                    user_cards.append(blackjack())
                else:
                    is_gameover = True
            
        while computer_score != 0 and computer_score < 17:
                computer_cards.append(blackjack())
                computer_score = calculate_score(computer_cards)
            
        print(f"your final hand: {user_cards}, current score: {user_score}")
        print(f"\nComputer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))

while input("Do you want to play a game of blackjack? type 'y' or 'n':  " )  == 'y':
    print("\n" * 30)
    print(logo)
    play_game()              
        
                      