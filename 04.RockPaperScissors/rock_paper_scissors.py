import random
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


print('******* ROCK PAPER SCISSORS *******')
print('What do you choose?')

user_input = input('Rock, Paper or Scissors?: ')

computer_choice = random.choice(['rock', 'paper', 'scissors'])

user_drawing =""
computer_drawing =""

if user_input.lower() =='scissors':
    user_drawing = scissors
elif user_input.lower() == 'paper':
    user_drawing = paper
elif user_input.lower() == 'rock':
    user_drawing = rock

if computer_choice =='scissors':
    computer_drawing = scissors
elif computer_choice == 'paper':
    computer_drawing = paper
elif computer_choice == 'rock':
    computer_drawing = rock

if user_input.lower() == computer_choice:
    print(f'You picked {user_input}.')
    print(user_drawing)
    print('--------------------------------')
    print(f'Computer picked {computer_choice}.')
    print(computer_drawing)
    print('--------------------------------')
    print('It\'s a tie')
elif user_input.lower() == "rock" and computer_choice == 'scissors' or user_input.lower() == "paper" and computer_choice == 'rock' or user_input.lower() == "scissors" and computer_choice == 'paper':
    print(f'You picked {user_input}.')
    print(user_drawing)
    print('--------------------------------')
    print(f'Computer picked {computer_choice}.')
    print(computer_drawing)
    print('--------------------------------')
    print('You win!')
elif computer_choice == "rock" and user_input.lower() == 'scissors' or computer_choice == "paper" and user_input.lower() == 'rock' or computer_choice == "scissors" and user_input.lower() == 'paper':
    print(f'You picked {user_input}.')
    print(user_drawing)
    print('--------------------------------')
    print(f'Computer picked {computer_choice}.')
    print(computer_drawing)
    print('--------------------------------')
    print('You lose...')



