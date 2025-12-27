# ROCK, PAPER, SICCORS by (PAPIAGAMERS)
#  This Game is we Played in Childhood
#    It's For Begginners Games and Pro of Python
#        Let's Start To Make The Game:

import random

# ============ GAMES CONFIG ===============

choices = ('r', 'p', 's')
emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}

# ============ MAKING THE GAME ============

while True:

    user_choice = input('\nEnter Rock, Paper, Scissors (r/p/s) : ').lower()

    if user_choice not in choices:
        print('\nInvalid Choice! Please Choice Between (r/p/s)')
        continue

    computer_choice = random.choice(choices)

    # Make The User and The Computer Value:
    print(f'\nYour Choices : {emojis[user_choice]}')
    print(f'\nComputer Choices : {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('\nYou Tied in The Game 🪢 !')

    elif (
        (user_choice == 'r' and computer_choice == 's') or 
        (user_choice == 's' and computer_choice == 'p') or (user_choice == 'p' and computer_choice == 'r')):

        print('\nYou Win The Game Correctly 😎')
    
    else:
        print('\nYou Lose in The Game 😞')

    should_continue = input('\nContinue The Game? (y/n) : ').lower()

    if should_continue == 'n':

        print('\nThanks For Playing Our Papiagamers Games!')
        break

    # ============= FINISH NOW PLAY THE GAME ================