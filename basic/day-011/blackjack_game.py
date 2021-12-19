### Our Blackjack House Rules ###
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as either 1 or 11.
## The cards in the list have equal possibility of being drawn.
## Cards are not removed from the deck as they are drawn.

###### Roadmap: 
# 1. Add a function to deal a card.
# 2. Add a function to calculate the score of the given cards.
# 3. Add a function to compare the scores of the user and computer.
# 4. Build the user loop.
# 5. Build the computer loop.
# 6. Add a function to play the game.

import random

from arts import logo

def deal_card() -> int:
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards: list) -> int:
    """Returns the score of the given cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score: int, computer_score: int) -> str:
    """Returns the winner of the game."""
    if user_score == computer_score:
        return "Draw!"
    
    if user_score == 0:
        return "You win with a Blackjack!"
    
    if computer_score == 0:
        return "You lose! Computer got a Blackjack!"
    
    if user_score > 21:
        return "You lose! You busted!"
    
    if computer_score > 21:
        return "You win! Computer busted!"
    
    if user_score > computer_score:
        return "You win!"
    
    return "You lose!"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    print(logo)

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\nYour cards: {user_cards}, current score {user_score}")
        print(f"Computer's first card: [{computer_cards[0]}]")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
            user_should_deal = input("Type 'y' to get another card or 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final cards: {user_cards}, final score {user_score}")
    print(f"Computer's final cards: {computer_cards}, final score {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? (y/n) ") == 'y':
    print(logo)
    print("\nWelcome to the Blackjack game!")
    play_game()
