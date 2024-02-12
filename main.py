import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def game():
    keep_playing = False
    while not keep_playing:
        player_hand = random.sample(cards,2)
        dealer_hand = random.sample(cards,2)
        print(f"Player: {player_hand} {player_hand[0] + player_hand[1]}")
        print(f"Dealer: {dealer_hand} {dealer_hand[0] + dealer_hand[1]}")

        player_first_hand = sum(player_hand)
        dealer_first_hand = sum(dealer_hand)
    
        if player_first_hand == 21 and dealer_first_hand == 21:
            print("Draw")
            keep_playing = True
        elif player_first_hand == 21:
            print(f"Player won with {player_first_hand}")
            keep_playing = True
        elif dealer_first_hand == 21:
            print(f"Dealer won with {dealer_first_hand}")
            keep_playing = True        
game()
