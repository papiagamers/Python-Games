# Python Quiz Game by (PAPIAGAMERS)
#    It's For The Begginners and Good in Python
#        So, Let's Make The Game:

questions = (
    "\nWhich animal lays the largest eggs? : ",
    "\nWhich planet is known as the Red Planet? : ",
    "\nThe Nobel Prize was established by which person? : ", 
    "\nWhat does “HTTP” stand for? : ", 
    "\nWhich of the following is NOT a type of machine learning? : ", 
    "\nWhat is the chemical symbol for water? : ")

options = (
    ("A. Ostrich", "B. Eagle", "C. Penguin", "D. Chicken"), 
    ("A. Earth", "B. Mars", "C. Venus", "D. Jupiter"), 
    ("A. Albert Einstein", "B. Isaac Newton", "C. Alfred Nobel", "D. Marie Curie"), 
    ("A. HyperText Transfer Protocol", "B. HighText Transmission Process", "C. Hyperlink Text Transfer Program", "D. High Transfer Text Protocol"), 
    ("A. Supervised Learning", "B. Unsupervised Learning", "C. Reinforcement Learning", "D. Sequential Learning"), 
    ("A. H2O", "B. CO2", "C. O2", "D. NaCl"))

answer = ("C", "B", "A", "D", "B", "B")
guesses = []
score = 0
question_num = 0 

for question in questions:
    print("------------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input('Enter The Answer (A, B, C, D) : ').upper()
    guesses.append(guess)

    if guess == answer[question_num]:

        score += 1
        print('\nYou Inputed The Correct Answer!')
        print(f'\nYour Score is incresed to {score}')

    else:

        print('\nYou Entered The Incorrect Answer!')
        print(f'\n{answer[question_num]} is the Correct Answer.')
        print(f'\nYour Score Was Decresed To {score - 1}')

    question_num += 1
    # ================ FINISHED NOW PLAY ====================