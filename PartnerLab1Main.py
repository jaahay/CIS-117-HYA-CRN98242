"""
Lab 1
Group #5
Authors: James Hay 
Date: 2025-09-25

The main program will ask the user which game they want to play.
"""

import RockPaperScissors as rps

def run():
    """ Play games with the User """
    print("Welcome! Let's have some fun playing games.")
    keep_playing = True
    while keep_playing:
        user_input = int(
            input(
                "Which game would you like to play?\n"\
                "\t1. Guessing Game\n" \
                "\t2. Rock, Paper, Scissors\n" \
                "\t3. Stop playing\n"
            )
        )
        if user_input == 1:
            print("Not yet implemented.")
            print("Returning to main menu.\n")
        elif user_input == 2:
            rps.play()
            print("Returning to main menu.\n")
        elif user_input == 3:
            keep_playing = False
            print("Goodbye!")
        else:
            print("I didn't understand that command.")

if __name__ == "__main__":
    run()