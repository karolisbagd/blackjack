import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def game():
    player_first_draw = random.sample(cards,2)
    dealer_first_draw = random.sample(cards,2)
    
    print(f"Player: {player_first_draw} {sum(player_first_draw)}")
    print(f"Dealer: {dealer_first_draw} {sum(dealer_first_draw)}")

    player_score = sum(player_first_draw)
    dealer_score = sum(dealer_first_draw)
        
    game_over = False
    while not game_over:
        
        player_score = sum(player_first_draw)
        dealer_score = sum(dealer_first_draw)
    
        if player_score == 21 and dealer_score == 21:
            print("Draw")
            game_over = True
        elif player_score == 21:
            print(f"Player won with {player_score}")
            game_over = True
        elif  dealer_score == 21:
            print(f"You lose, dealer won with {dealer_score}")
        elif player_score > 21:
            print("You have over 21")
            game_over = True
        else: 
            if input("Draw another card") == "y":
                player_first_draw.append(deal_card())
                print(f"Player: {player_first_draw} {sum(player_first_draw)}")
                
game()
