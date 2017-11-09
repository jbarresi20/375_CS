#This is a program that pits two players against eachother in a game of pig. It is created by James Drago and Joseph Barresi. Peter Bell kind of but he kinda went off and did something way to advanced.
#The program is only 2 players against eachother uses an important random function for dice rolls.
import random
player1name = 0
player2name = 0
dicetotal = 0
roll_total = 0
player1total = 0
player2total = 0
WINNING_SCORE = 100


def main():
    global dicetotal,player1total,player2total,player1name,player2name, WINNING_SCORE
    next_players_turn = 1
    welcome_screen()
    playernames()
    #This while loop checks player scores as it rotates through turns
    while player1total < WINNING_SCORE and player2total < WINNING_SCORE:
        clearscreen()
        scoreboard()
        #This if/ else function controls which players turn it is
        if next_players_turn == 1:
            print("It's", player1name, "'s turn", sep = "")
            play_turn()
            player1total = dicetotal + player1total
            next_players_turn = 2
            if player1total >= WINNING_SCORE:
                break
        else:
            print("It's", player2name, "'s turn", sep = " ")
            play_turn()
            player2total = dicetotal + player2total
            next_players_turn = 1
    #This chooses, depending on who won, on who to direct the winning message to.
    if player1total >= WINNING_SCORE:
        print("Congrats",player1name, "You won! Now laugh in", player2name, "'s face", sep = " ")
    else:
        print("Congrats",player2name, "You won! Now laugh in", player1name, "'s face", sep = " ")

def scoreboard():
    #This displays the current score between both players after every turn
    global player1name, player2name, player1total,player2total
    print("Scoreboard")
    print("----------")
    print(player1name, player1total)
    print(player2name, player2total )
    print("")



def welcome_screen():
    #This prints the start screen and an introductory comment.
    print("""
      ,:´'*:^-:´¯'`:·,                        ',:'/¯/`:,                    __'
     '/::::/::::::::::;¯'`*:^:-.,            /:/_/::::/';'           ,.·:'´::::::::`'·-.
    /·´'*^-·´¯'`^·,/::::::::::::'`:,         /:'     '`:/::;        '/::::::::::::::::::';
    '`,             ¯'`*^·-:;::::::'\'       ;         ';:';       /;:· '´ ¯¯  `' ·-:::/'
      '`·,                     '`·;:::i'      |         'i::i      /.'´      _         ';/' 
         '|       .,_             \:'/'       ';        ;'::i    ,:     ,:'´::;'`·.,_.·'´.,    
         'i       'i:::'`·,          i/'       'i        'i::i'   /     /':::::/;::::_::::::::;
         'i       'i::/:,:          /'          ;       'i::;' ,'     ;':::::'/·´¯     ¯'`·;:::¦
          ;      ,'.^*'´     _,.·´           ';       i:/'  'i     ';::::::'\             ';:';
          ';     ;/ '`*^*'´¯                   ';     ;/ °   ;      '`·:;:::::`'*;:'´      |/'
           \    /                               ';   / °      \          '`*^*'´         /'  
            '`^'´                                `'´       °    `·.,               ,.-·´
                                                                    '`*^~·~^*'´
    """)
    print("So you wanna play Pig Huh. I hope you do not bust!")


def dice_roll():
    #This rolls the dice when the player who's turn it is hits enter.
    global roll_total
    input("Press enter to roll the Dice")
    die1 = random.randrange(1, 7)
    roll_total = die1
    print()
    print(" +---+   ")
    print(" |", die1, "|")
    print(" +---+   ")
    print()

def play_turn():
    #This decides the dice roll and allows the player to choose whether or not they want to roll again.
    global dicetotal,roll_total
    keepplaying = True
    dicetotal = 0
    while keepplaying:
        dice_roll()
        if roll_total == 1:
            dicetotal = 0
            print('You busted. Nice try')
            keepplaying = False
        else:
            dicetotal = dicetotal + roll_total
            print("Running Total =", dicetotal)
            keepplaying = (input("Press Y to keep rolling. Do anything else to keep your points this round") == 'Y')




def playernames():
    #This asks for the 2 players names at the start of the game
    global player1name, player2name
    print("")
    player1name = input("What would Player 1 like to be called?")
    player2name = input("What would Player 2 like to be called?")


def clearscreen():
    #This clears the screen in between rolls
    for i in range (10):
        print("")

main()
