import random
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Version 1.0
# This program is the initial psudocode and logic for Luncher app in python
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

__author__ = 'Randy Lee'


def main():
    # Create array to store locations
    choices = []

    # Counter for amount of locations
    amount_of_locations = int(input("How many locations?: "))
    for counter in range(amount_of_locations):
        choices.append(input("Add Location: "))

    # Print choices array for debugging
    print(choices)

    # Choose random location from array
    location_choice = random.randint(1, len(choices) - 1)

    # Print location choice for debugging
    print("Location Choice Index Number = ", location_choice)

    # Print final choice
    print("Final Choice = ", choices[location_choice])


main()