# Roll The Dice by (PAPIAGAMERS)
#  You Can Download it from github/papiagamers
# The Dice Game Conatins 1 Players,
#      Let's Start To Make:

import random

# ========== MAKING CONFIG GAMES ==========

while True:

    
    choice = input('Roll The Dice Now (y/n) ? : ').lower()

    if choice == 'y':

     dice1 = random.randint(1, 6)
     dice2 = random.randint(1, 6)
     print(f'({dice1}, {dice2})')

    elif choice == 'n':
        
        print('\nThanks For Choosing The Dice!')
        break

    else:

        print('\nInvalid Choice! Write The Correct Letter.')