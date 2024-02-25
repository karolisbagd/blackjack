import random
from blackjack_art import logo
import os


def clear(): os.system('cls')

def deal_card():
    """Generates and returns a random card."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Takes a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 21:
     # Returns 0 if player/dealer has got blackjack score 21
     return 0
    # If 'Ace' in hand and over score 21, changes to score 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(p_score, d_score):
    if p_score == d_score:
        return "Draw"
    elif d_score == 0:
        return "Lose, opponent has Blackjack"
    elif p_score == 0:
        return "Win with a Blackjack"
    elif p_score > 21:
        return "You went over 21. You lose"
    elif d_score > 21:
        return "Dealer, went over 21. You win"
    elif p_score > d_score:
        return "You win"
    else:
        return "You lose"
    
def play_game():
    
    print(logo) 
    
    players_cards = []
    dealers_cards = []
    game_over = False

    for _ in range(2):
        players_cards.append(deal_card())
        dealers_cards.append(deal_card())
        
    while not game_over:

        player_score = calculate_score(players_cards)
        dealers_score = calculate_score(dealers_cards)
        print(f"Player's cards:{players_cards}, current score: {player_score} ")
        print(f"Dealer's first card: {dealers_cards[0]}")

        if player_score == 0 or dealers_score == 0 or player_score > 21:
            game_over = True
        else:
            extra_card = input("Type 'y' to get another card, type 'n' to pass:")
            if extra_card == 'y':
                players_cards.append(deal_card())
            else:
                game_over = True
        
    while dealers_score !=0 and dealers_score < 17:
        dealers_cards.append(deal_card())
        dealers_score = calculate_score(dealers_score)

    print(f"Player cards: {players_cards}, score: {player_score}")
    print(f"Dealer's cards: {dealers_cards}, score: {dealers_score}")
    print(compare(player_score, dealers_score))


while input("Do you want play a game of Blackjack? Type 'y', otherwise 'n': ") == "y":
    clear()
    play_game()
