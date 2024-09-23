import random
import deck_dictionary
import art

# Initialize player and computer points
player_points = 0
computer_points = 0
computer_cards = []  # Store computer's cards

# Function to draw two random cards
def draw_two_cards():
    card_values = random.sample(list(deck_dictionary.deck.keys()), 2)  # Get two random card values
    drawn_cards = []

    for card_value in card_values:
        # Select a random suit for the card
        suit = random.choice(list(deck_dictionary.deck[card_value].keys()))
        card_art = deck_dictionary.deck[card_value][suit]
        drawn_cards.append((card_value, suit, card_art))

    return drawn_cards

def draw_one_card():
    card_values = random.sample(list(deck_dictionary.deck.keys()), 1)  # Get one random card value
    drawn_cards = []

    for card_value in card_values:
        # Select a random suit for the card
        suit = random.choice(list(deck_dictionary.deck[card_value].keys()))
        card_art = deck_dictionary.deck[card_value][suit]
        drawn_cards.append((card_value, suit, card_art))

    return drawn_cards

# Function to calculate points from drawn cards
def calculate_points(cards):
    total_points = 0
    for card_value, suit, _ in cards:
        total_points += deck_dictionary.deck[card_value][suit][0]  # Access the numeric value from the dictionary
    return total_points

# Function to display cards
def display_drawn_cards(cards, show_all=False):
    if show_all:
        for card_value, suit, card_art in cards:
            print(f"Card: {card_value} of {suit}")
            print(card_art[1])  # Print the ASCII art
    else:
        # Show only the first card
        card_value, suit, card_art = cards[0]
        print(f"Computer's visible card: {card_value} of {suit}")
        print(card_art[1])  # Print the ASCII art
        print("Computer has another card hidden.")

# Start the game
def begin_game():
    global player_points, computer_points, computer_cards
    print("Your cards are:")
    drawn_cards = draw_two_cards()
    player_points = calculate_points(drawn_cards)
    display_drawn_cards(drawn_cards, show_all=True)  # Display both player cards
    print(f'Your points: {player_points}')

    print("\nComputer's cards:")
    computer_cards = draw_two_cards()
    computer_points = calculate_points([computer_cards[0]])  # Only calculate points for the visible card
    display_drawn_cards(computer_cards)  # Display only one card for the computer
    print(f'Computer points: {computer_points}')

    # Ask if the player wants more cards
    more_cards = input("Do you want more cards? (y/n): ")
    if more_cards.lower() == 'y':
        one_more_card()
    elif more_cards.lower() == 'n':
        computer_last_card()
        determine_winner()
    else:
        print("Invalid input! Please enter 'y' or 'n'.")
        begin_game()

def one_more_card():
    global player_points

    new_card = draw_one_card()  # Draw one card
    player_points += calculate_points(new_card)  # Add the points for the drawn card
    print("You drew:")
    display_drawn_cards(new_card, show_all=True)
    print(f'Your points: {player_points}')

    # Check if player exceeds 21
    if player_points > 21:
        print("You busted! Computer wins.")
        return

    # Ask if the player wants more cards again
    more_cards = input("Do you want another card? (y/n): ")
    if more_cards.lower() == 'y':
        one_more_card()
    else:
        computer_last_card()
        determine_winner()

def computer_last_card():
    global computer_points, computer_cards
    print("Computer's turn to draw more cards.")

    # Show all computer cards and calculate total points
    computer_points = calculate_points(computer_cards)  # Calculate initial points
    while computer_points < 17:  # Example rule for the computer
        new_card = draw_one_card()
        computer_cards.append(new_card[0])  # Add the new card to the computer's hand
        print("Computer drew:")
        display_drawn_cards(new_card, show_all=True)  # Show the drawn card
        computer_points = calculate_points(computer_cards)  # Update the computer's points

    # Final point calculation
    print(f"Computer's final cards:")
    display_drawn_cards(computer_cards, show_all=True)

def determine_winner():
    global player_points, computer_points
    print(f'Final scores: Player: {player_points}, Computer: {computer_points}')
    if player_points > 21:
        print("You busted! Computer wins.")
    elif computer_points > 21 or player_points > computer_points:
        print("You win!")
    elif player_points < computer_points:
        print("Computer wins!")
    else:
        print("It's a tie!")
    play()

def play():
    answer = input("Do you want to play? (y/n): ")
    if answer.lower() == "y":
        begin_game()
    elif answer.lower() == "n":
        print("Thanks for playing!")
    else:
        print("Sorry, that's not a valid answer.")
        play()  # Prompt again if the input is invalid

print(art.logo)
print("Welcome to BlackJack!")
play()
