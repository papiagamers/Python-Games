# Number Guessing Game by (PAPIAGAMERS)
#  This Game is For Gussing The Game
#    It's For Begginners Games
#        Let's Start The Game:

import random

number_guess = random.randint(1, 100)

# ============= MAKING THE NUMBER GUESS GAME =============

while True:
    try:

     guess = int(input('\nGuess The Number Between 1 to 100 : '))

     if guess < number_guess:
        print('\nToo Low! Make It Balanced Brother')

     elif guess > number_guess:
        print('\nToo High! The Number Between 1 to 100')

     else:
        print('\nCongratulations! You Gussed The Number.')
        break

    except ValueError:

        print('\nInvalid Choice! Input The Number Not Word.')
# ============== FINISHED THE GAME ========================