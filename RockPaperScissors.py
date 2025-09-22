"""
Lab 1
Group #12
Author: James Hay
Date: 9-18-25

Your function will generate a random number (1, 2, 3) and will ask you to choose a number.
Depending on the combination of the random number generated and the number you chose,
the program will decide on who won or if it is a tie.
"""

import random

def rockpaperscissors_game():
    Computer_Selection = random.randint(1, 3)
    User_Selection = int(input("Select your throw:\n" \
        "1. Rock\n" \
        "2. Paper\n" \
        "3. Scissors\n"
    ))
    print(f"You're throwing {throw_text(User_Selection)}")
    print("Let's see what the computer will try..")
    print(f"The computer threw {throw_text(Computer_Selection)}")
    
    print(score_throw(User_Selection, Computer_Selection))
    
def throw_text(i):
    if(i == 1): return "Rock"
    if(i == 2): return "Paper"
    if(i == 3): return "Scissors"

def score_throw(My_Throw, Their_Throw):
    if(My_Throw == Their_Throw): return "It's a tie!"
    elif(My_Throw == 1 and Their_Throw == 2
        or My_Throw == 2 and Their_Throw == 3
        or My_Throw == 3 and Their_Throw == 1):
        return "Sorry, you lose."
    elif(My_Throw == 1 and Their_Throw == 3
         or My_Throw == 2 and Their_Throw == 1
         or My_Throw == 3 and Their_Throw == 2):
        return "Congratulations, you win!"
    else:
        return "I didn't understand that."
    
    