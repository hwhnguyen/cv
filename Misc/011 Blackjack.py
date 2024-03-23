import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

card_values = {
    'A': 0,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

def scorer(char):
    score = 0
    n_Ace = 0
    for card in char:
        score += card_values[card]
        if card == 'A':
            n_Ace += 1

    if n_Ace==1 and score < 10:
        score += 11
    elif n_Ace > 0:
        for n in range(n_Ace):
            score += 1
    return score

main = True
while main is True:
    game_or_nogame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if game_or_nogame == 'n':
        main = False # Break main loop
    elif game_or_nogame == 'y':
        print(logo)
        deck = [
            'A', '2', '3', '4', '5', '6' ,'7', '8', '9', '10', 'J', 'Q', 'K',
            'A', '2', '3', '4', '5', '6' ,'7', '8', '9', '10', 'J', 'Q', 'K',
            'A', '2', '3', '4', '5', '6' ,'7', '8', '9', '10', 'J', 'Q', 'K',
            'A', '2', '3', '4', '5', '6' ,'7', '8', '9', '10', 'J', 'Q', 'K',
            ]
        random.shuffle(deck)
        player = []
        dealer = []
        player.append(deck.pop())
        dealer.append(deck.pop())
        player.append(deck.pop())
        dealer.append(deck.pop())

        game_on = True
        while game_on is True:
            player_score = scorer(player)
            dealer_score = scorer(dealer)
            dealer_show = [dealer[0]]
            dealer_show.extend(['*' for n in range(len(dealer)-1)])
            print(f"Your cards: {player}, current score: {player_score}")
            if dealer_score>=21 or player_score>=21:
                print(f"Dealer\'s cards: {dealer}")
            else:
                print(f"Dealer\'s cards: {dealer_show}")

            if player_score==21 and player_score==dealer_score:
                print("It\'s a tie!\n")
                break
            elif player_score>21:
                print("You bust!\n")
                break
            elif dealer_score>21:
                print("Dealer bust!\n")
                break
            elif player_score==21:
                print("You win!\n")
                break
            elif dealer_score==21:
                print("Dealer win!\n")
                break

            draw = input("Type \'y\' to get another card, type \'n\' to pass: ")
            if draw == 'y':
                player.append(deck.pop())
            if dealer_score < 17:
                dealer.append(deck.pop())
                dealer_score = scorer(dealer)
            print("\n")
            if draw == 'n':
                while dealer_score < 17:
                    dealer.append(deck.pop())
                    dealer_score = scorer(dealer)
                print(f"Your final hand: {player}, final score: {player_score}")
                print(f"Dealer\'s final hand: {dealer}, final score: {dealer_score}\n")
                if player_score==dealer_score:
                    print("It\'s a tie!")
                elif dealer_score>21:
                    print("Dealer bust!\n")
                elif player_score>dealer_score:
                    print("You win!")
                elif dealer_score<=21 and dealer_score>player_score:
                    print("Dealer win!")
                print("\n")
                break
