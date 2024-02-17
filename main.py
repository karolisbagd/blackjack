import random

def deal_card():
    """Generates and returns a random card."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

players_cards = []
dealers_cards = []


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 21:
     # Returns 0 if player/dealer has got blackjack score 21
     return 0
    # If 'Ace' in hand and over score 21, changes to score 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)
    
# player_score = sum(player_first_draw)
# dealer_score = sum(dealer_first_draw)

# print(f"Player: {player_first_draw} {sum(player_first_draw)}")
# print(f"Dealer: {dealer_first_draw} {sum(dealer_first_draw)}")



for _ in range(2):
    players_cards.append(deal_card)
    dealers_cards.append(deal_card)
    

# if calculate_score(players_cards) == 21 and calculate_score(dealers_cards) == 21:
#     print("Draw")
# elif calculate_score(players_cards) == 21:
#     print(f"Player won with {calculate_score(players_cards)}")
# elif  dealers_cards == 21:
#     print(f"You lose, dealer won with {calculate_score(dealers_cards)}")
# elif calculate_score(players_cards) > 21:
#     print("You have over 21")
# else: 
#     question = input("Draw another card")
# if question == "y":
#     players_cards.append(deal_card)
#     print(f"Player's hand {calculate_score(players_cards)}")
# elif question == "n":
#     while calculate_score(dealers_cards) < 17:
#         dealers_cards.append(deal_card)
#         print(f"Dealer: {calculate_score(dealers_cards)}")
#         if calculate_score(dealers_cards) > 21: 
#             print(f"Dealer have over 21 with {calculate_score(dealers_cards)}, Player wins.")
    
        
# if dealer_score > player_score:
#         print(f"Dealer wins with: {dealer_first_draw} {sum(dealer_first_draw)}\n while player {player_first_draw} {sum(player_first_draw)}")

# elif dealer_score == player_score:
#     print("Draw")
# else:
#         print(f"Player wins with: {player_first_draw} {sum(player_first_draw)}\n while dealer {dealer_first_draw} {sum(dealer_first_draw)}")

