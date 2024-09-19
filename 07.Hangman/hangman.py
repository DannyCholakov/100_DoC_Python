import random
import hangman_words
import hangman_art

word = random.choice(hangman_words.word_list)
placeholder = ''

for letter in word:
    placeholder += "_"

print(hangman_art.hangman_logo)
print("****************** WELCOME TO HANGMAN!!! ******************")

player_lives = 6
stage = 6
game_over = False
correct_letters = []
guessed_letters = set()

while not game_over:
    print(f'****************** YOU HAVE {player_lives} LIVES. ******************')
    print(hangman_art.hangman_stages[stage - player_lives])
    print(f"Your Word: {placeholder}")
    user_guess = input("****************** Guess a letter: ").lower()

    if user_guess in guessed_letters:
        print("^^^^^^^^^^^^^^^^ You already guessed that letter! Try a different one. ^^^^^^^^^^^^^^^^")
        continue
    else:
        guessed_letters.add(user_guess)

    display = ""
    for letter in word:
        if letter == user_guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'

    print(f'^^^^^^^^^^^^^^^^ YOUR WORD SO FAR: {display} ^^^^^^^^^^^^^^^^')

    if user_guess not in word:
        player_lives -= 1
        if player_lives <= 0:
            game_over = True
            print(hangman_art.hangman_stages[6])
            print("****************** YOU GOT HANGED! ******************")
            print(f"^^^^^^^^^^^^^^^^ THE WORD WAS {word}! ^^^^^^^^^^^^^^^^")

    if '_' not in display:
        game_over = True
        print(f"****************** You got it {display}!!! ******************")
