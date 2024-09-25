import random
import art

lives = 0
difficulty = ''
computer_number = random.randint(1, 100)
def new_game():
    global lives, difficulty
    lives = 0
    print('I\'m thinking of a number between 1 and 100!')
    difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")
    game_difficulty()


def game_difficulty():
    global lives, difficulty
    if difficulty.lower() == 'easy':
        lives = 10
        tries()
    elif difficulty.lower() == 'hard':
        lives = 5
        tries()
    else:
        print('Wrong input type!')
        new_game()

def tries():
    global lives, difficulty,computer_number

    for i in range(1,lives+1):
        guess = int(input('Make a guess: '))
        if guess == computer_number:
            print('You guessed my number!')
            new_game_answer =  input("Do you want to play again? (yes or no)")
            if new_game_answer.lower() == 'yes':
                new_game()
            elif new_game_answer.lower() == 'no':
                print('Game over! Thanks for playing!')
                exit()
            break
        elif guess < computer_number:
            print('Sorry you guessed too low!')
            print(f'You have {lives-i} attempts left.')
        elif guess > computer_number:
            print(f'You have {lives - i} attempts left.')
            print('Sorry you guessed too high!')

        if lives == 0:
            print('You ran out of lives!')
            new_game_answer = input("Do you want to play again? (yes or no): ")
            if new_game_answer.lower() == 'yes':
                new_game()
            elif new_game_answer.lower() == 'no':
                print('Game over! Thanks for playing!')
                exit()

print(art.logo)
print('Welcome to the Number Guessing Game!')
new_game()