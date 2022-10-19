#!/usr/bin/env python3
# Created by: Patrice Pat-Odita
# Created on: Oct 18, 2022
# This program asks the user to guess a
# number and if they get it wrong they are told so.
import random


def main():
    # a number between 0 and 9
    random_variable = random.randint(0, 9)
    # Get number from user
    number_guessed_as_string = input("Guess my favorite number from 0-9: ")
    print("")

    # try catch
    try:
        # Changing string to integer
        number_guessed_as_number = int(number_guessed_as_string)
        print("\033[1;35;38mYou entered an integer correctly")
        print()
        # Check to see if they got the right number or wrong
        if number_guessed_as_number == random_variable:
            print("\033[1;3;39mYOU GOT IT RIGHT!")
        else:
            print("\033[1;35;39mYou got it wrong...")
            print("\033[1;34;38mmy favorite number is {} ".format(random_variable))
    except Exception:
        print("\033[1;35;38mThis is not an integer")
    finally:
        print()
        print("\033[1;35;38mThanks for playing")


if __name__ == "__main__":
    main()
