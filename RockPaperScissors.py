"""
Lab 1
Group #5
Author: James Hay
Date: 2025-09-25

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

def play():
    """ Play a game of Rock, Paper, Scissors """
    print("Let's play a game of Rock, Paper, Scissors together!")
    computer_selection = random.randint(1, 3)
    computer_throw = rock_paper_scissors[computer_selection]

    user_selection = int(
        input(
            "Select your throw:\n" \
            "\t1. Rock\n" \
            "\t2. Paper\n" \
            "\t3. Scissors\n"
        )
    )
    user_throw = rock_paper_scissors[user_selection]

    print("\tYou're throwing", user_throw)
    print("Let's see what the computer will try..")
    print("\tThe computer threw", computer_throw)
    
    print(score_throw(user_throw, computer_throw))
    print("Returning to main menu.\n")

def score_throw(my_throw, their_throw):
    """ Find the outcome of a game of rock, paper, scissors. """
    if(my_throw == their_throw): return "It's a tie!"
    elif(
        my_throw == rock and their_throw == paper
        or my_throw == paper and their_throw == scissors
        or my_throw == scissors and their_throw == rock
        ):
        return "Sorry, you lose."
    elif(
        my_throw == rock and their_throw == scissors
        or my_throw == paper and their_throw == rock
        or my_throw == scissors and their_throw == paper
        ):
        return "Congratulations, you win!"
    else:
        return "I didn't understand that."
    
if __name__ == "__main__":
    keep_playing = True
    while keep_playing:
        play()
        keep_playing = input("Keep playing Rock, Paper, Scissors? Y/N\n") == "Y"