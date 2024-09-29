import random
import art
import dictionary

alive = True
right_answer = ''

print(art.logo)
print('Welcome to Higher Or Lower!')

def play_game():
    play_game_answer = input('Wanna play? (y/n): ').lower()
    if play_game_answer == 'y':
        game()
    elif play_game_answer == 'n':
        print('Thanks for playing!')
        exit()
    else:
        print('Wrong input, please try again!')
        play_game()

def get_two_celebrities():
    celeb1, celeb2 = random.sample(dictionary.celebrities, 2)  # Get two random celebrities
    return celeb1, celeb2

def game():
    score = 0
    game_active = True

    while game_active:
        celeb_a, celeb_b = get_two_celebrities()

        # Display celebrity A
        print(f"Compare A: {celeb_a['name']}.")
        print(f'{celeb_a['description']} From {celeb_a['country']}.')

        print(art.vs)

        # Display celebrity B
        print(f"Compare B: {celeb_b['name']}.")
        print(f'{celeb_b['description']} From {celeb_b['country']}.')

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        right_answer = 'a' if celeb_a['follower_count'] > celeb_b['follower_count'] else 'b'

        if answer == right_answer:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_active = False

        # Ask if user wants to play again after a wrong answer
        if not game_active:
            replay = input('Play again? (y/n): ').lower()
            if replay == 'y':
                game()
            else:
                print('Thanks for playing!')
                game_active = False

play_game()
