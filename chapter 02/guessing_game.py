#This simple guessing game was designed by Joe Barresi of Mr. Ciccolo class

#My program is structured extremely unorthodox mostly based around my wanting to make it So the prompt would differ from the first time compared to the second.
#That's the only reason my numberof guesses starts at 1. Because the 1st prompt is outside  of the while loop.
#Also at the end of the program number of guesses if checked to see if someone sniped it first try.


import random

def main():
    print("So you want to guess my number. I dare you to try.")
    magic_number = random.randrange(1, 101)
    guess = eval(input("Guess what number I'm thinking of."))
    number_of_guesses = 1
    while guess != magic_number:
        if magic_number > guess:
            print("Too low. You need to guess higher!")
        elif magic_number < guess:
            print("Too high. You need to guess lower!")
        guess = eval(input("Guess another number:"))
        number_of_guesses = number_of_guesses + 1
    if number_of_guesses > 1:
        print("Congrats you guessed my Magic Number. It only took you", number_of_guesses, "times to beat me. I'll beat you next time.")
    else:
        print("You're either a cheater or extremely good! Either way you got it first time.")
main()
