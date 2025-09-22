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

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

rock_paper_scissors = {
    1: rock, rock: 1,
    2: paper, paper: 2,
    3: scissors, scissors: 3
}

def rockpaperscissors_game():
    Computer_Selection = random.randint(1, 3)
    Computer_Throw = rock_paper_scissors[Computer_Selection]

    User_Selection = int(input("Select your throw:\n" \
        "1. Rock\n" \
        "2. Paper\n" \
        "3. Scissors\n"
    ))
    User_Throw = rock_paper_scissors[User_Selection]

    print("You're throwing", User_Throw)
    print("Let's see what the computer will try..")
    print("The computer threw", Computer_Throw)
    
    print(score_throw(User_Throw, Computer_Throw))

def score_throw(My_Throw, Their_Throw):
    if(My_Throw == Their_Throw): return "It's a tie!"
    elif(
        My_Throw == rock and Their_Throw == paper
        or My_Throw == paper and Their_Throw == scissors
        or My_Throw == scissors and Their_Throw == rock
        ):
        return "Sorry, you lose."
    elif(
        My_Throw == rock and Their_Throw == scissors
        or My_Throw == paper and Their_Throw == rock
        or My_Throw == scissors and Their_Throw == paper
        ):
        return "Congratulations, you win!"
    else:
        return "I didn't understand that."
    
if __name__ == "__main__":
    rockpaperscissors_game()