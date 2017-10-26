# craps.py
#
# This program simulates the dice game craps. The user starts with $100 and is allowed to bet on the roll of two
# six-sided dice:
#
#  - A roll of 7 or 11 on the opening throw results in a win
#  - A roll of 2, 3, or 12 on the opening throw results in a loss
#  - A roll of anything else means the user has to re-roll the dice until that same number is rolled (a win) or a 7 is
#    rolled (a loss)
#
# A win pays whatever amount was bet. A loss takes the amount bet. The user can continue to play until he/she is out of
# money.
#
# by Mr. Ciccolo

import random
winnings = 100
bet = 0
x = 1

def main():
    global winnings
    global bet
    global x

    display_welcome()

    play_again = True
    while play_again:
        place_bet()
        total = roll_dice()
        if total == 7 or total == 11:
            print("You win!")
            winnings = winnings + bet
        elif total == 2 or total == 3 or total == 12:
            print("You lose!")
            winnings = winnings - bet
        else:
            re_roll(total)
        print() # Blank line for spacing
        if winnings > 5:
            play_again = (input("Press 'Y' to play another round. Do anything else to keep your money") == 'Y')
            clear_screen()
        else:
            clear_screen()
            print("Sorry so much, your too broke to play in this casino.")
            play_again = False
    print("It was fun playing! You finish with $", winnings, sep = "")



def clear_screen():
    for i in range(20):
        print()


def display_welcome():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$                                              $")
    print("$ Welcome to the Computer Science Craps Table! $")
    print("$                                              $")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()

def roll_dice():
    input("Press Enter to roll the dice...") # We don't do anything with the input, we're just using it to pause the game

    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    total = die1 + die2

    print()
    print(" +---+   +---+")
    print(" |", die1, "| + |", die2, "| =", total)
    print(" +---+   +---+")
    print()

    return total

def re_roll(point):
    global winnings, bet
    print("You have to keep rolling until you get another", point)
    print() # Blank line for spacing

    total = roll_dice()
    while total != point and total != 7:
        total = roll_dice()

    if total == point:
        print("You win!")
        winnings = winnings + bet
    else:
        print("You lose!")
        winnings = winnings - bet


def place_bet():
    global bet
    bet = eval(input("You have $" + str(winnings)+ ". How much do you want to bet? ($5-"+ str(winnings)+")"))
    while bet < 5 or bet > winnings:
        bet = eval(input("Nice Try type in another bet"))



main()
