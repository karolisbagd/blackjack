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
            game_over = True
        elif player_score > 21:
            print("You have over 21")
            game_over = True
        else: 
            question = input("Draw another card")
            if question == "y":
                player_first_draw.append(deal_card())
                print(f"Player: {player_first_draw} {sum(player_first_draw)}")
            elif question == "n":
                while dealer_score < 17:
                    dealer_first_draw.append(deal_card())
                    dealer_score = sum(dealer_first_draw)
                    print(f"Dealer: {dealer_first_draw} {sum(dealer_first_draw)}")
                    if dealer_score > 21: 
                        print(f"Dealer have over 21 with {dealer_score}, Player wins.")
                        game_over = True
                    
            if dealer_score > player_score:
                 print(f"Dealer wins with: {dealer_first_draw} {sum(dealer_first_draw)}\n while player {player_first_draw} {sum(player_first_draw)}")
                 game_over = True
            elif dealer_score == player_score:
                print("Draw")
                game_over = True
            else:
                 print(f"Player wins with: {player_first_draw} {sum(player_first_draw)}\n while dealer {dealer_first_draw} {sum(dealer_first_draw)}")
                 game_over = True
game()