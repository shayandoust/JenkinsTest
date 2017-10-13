# SHAYAN DOUST
# HANGMAN

#                                                                 LAST LESSON: STILL DOESNT FUNCTION CORRECTLY

import time
import random
import os

#Python via CMD doesn't like global vars. :(
global timer
global countdown
guesses = 1
countdown = 4

#str() otherwise .center() attribute doesn't function :(
global words
global hints
words = ["whiplash",
"blueprint",
"clap",
"capitalism",
"brainstorm"]
hints = ["You experience this during a car accident",
"Layout for designing a building",
"Sign of respect usually done for congratulations or speech",
"Industry that is controlled by private owners",
"Share ideas"
]


def hangman_graphics(guesses):
    if guesses == 0:
        print ("""
                ________
                |      |
                |
                |
		        |
		        |
`       """)

    elif guesses == 1:
        print ("""
                ________
                |      |
                |      0
                |
                |
                |

        """)

    elif guesses == 2:
         print ("""
                ________
                |      |
                |      0
                |     /
                |
                |

        """)

    elif guesses == 3:
        print ("""
                ________
                |      |
                |      0
                |     /|
                |
                |
                Be careful, your fate is getting ever so closer.

        """)


    elif guesses == 4:
        print ("""
                ________
                |      |
                |      0
                |     /|\
                |
                |
        """)

    elif guesses == 5:
        print("""
                ________
                |      |
                |      0
                |     /|\
                |     /
                |

        """)

    else:
        print("""
                ________
                |      |
                |      0
                |     /|\
                |     / \
                |

              The noose tightens around your neck, and you fell the sudden
              urge to urinate.

                   GAME OVER!
            """)


def game():
    gameActive = 1
    global guesses
    global words
    global hints
    chosenIndex = random.randint(0,4)
    chosenWord = words[chosenIndex]

    while(gameActive):
        while guesses != 0:
            usr_input = input("Please enter a word or a letter, or type help: ")
            usr_input.lower()
            if usr_input == "help":
                print("Here is a hint:\n",hints[chosenIndex],"\n")
            else:


        else:
            print("The game is over :(")
            break
    else:
        print("Something unexpected happened :(")


def menu():
    global countdown
    if countdown > 0:
        print("""
    _____________________________________________


                HANGMAN BY SHAYAN
            Please follow the instructions.

        Continuing in:""")
        global countdown
        print(countdown)
        print("\n")
        time.sleep(1)
        countdown -= 1
        menu()
    else:
        game()



#Start the nested functions correctly
menu()
#Wait for 1 minute once the program finishes & inform user of termination
print("Program terminated.")
time.sleep(60)