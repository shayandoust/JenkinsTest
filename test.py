import time
import sys
import threading
import os
import random
from ProgressBar import progressBar

# Defining all variables & arrays
global currentRoom
global hydration
global counter
global inventory
currentRoom = 1
hydration = 20
counter = 1
inventory = []

rooms = {
    1:{"name":"Hall",
       "east": 2,
       "south": 3
      },
      2:{"name":"Kitchen",
       "west": 1,
       "south": 4,
       "item":"Water Bottle"
      },
      3:{"name":"Bathroom",
       "north": 1,
       "item":"Toilet Paper"
      },
      4:{"name":"Bedroom",
       "north": 2,
       "item":"Wooden Plank"
      }


}
# Yes, these thread classes could have been combined into 1 class, but oh well... :)
class hydrationOverTimeThread(threading.Thread):
   def __init__(self, threadID, name, counter):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.name = name
    self.counter = counter
   def run(self):
    print("DEBUG: Thread 1 - Hydration over time running\n")
    hydrationOverTime(hydrationOverTimeThread, counter)
class zombieThreadOverTime(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        def run(self):
            print("DEBUG: Thread 2 - Zombie over time running")
            zombie(zombieThreadOverTime, counter)
def zombie(zombieThreadOverTime, counter):
    while counter:
        time.sleep(random.randint(30, 50))
        print("A zombie has been detected in the HALL. Head over there and defeat it!")



def hydrationOverTime(hydrationOverTimeThread, counter):
    while counter:
        global hydration
        hydration -= 5
        time.sleep(5)
def hydrationUpdate(operation, value):
    if operation == "-":
        global hydration
        hydration -= value
        return hydration
    else: # Assuming operation is an increase
        global hydration
        hydration += value
        return hydration
def timeCountdown():
    i = 5
    sys.stdout.write("Starting game in 5 seconds...")
    sys.stdout.flush()
    while i != 0:
        sys.stdout.write(i)
        i -= 1
        time.sleep(1)
    return 0

def game():
    hydrationThread = hydrationOverTimeThread(1, "hydrationOverTimeThread", 1)
    zombieThread = zombieThreadOverTime(2, "zombieThreadOverTime", 2)
    hydrationThread.start()
    zombieThread.start()
    while True:
        showMap()
        global currentRoom
        try:
            usr_command = input("Enter a command: ").lower().split()
        except(EOFError):
            break
        print(usr_command)

        if usr_command[0] == "go":
            if usr_command[1] in rooms[currentRoom]:
                currentRoom= rooms[currentRoom][usr_command[1]]
                print(currentRoom)
            else:
                print("You cannot go that way!")
        else:
            print("Invalid command.")
        if hydration == 0 or hydration < 0:
            print("You are dehydrated, and as a cause, you have died.")
            os.system("cls")
            sys.exit()

def showInstructions():
    print("""

    A game... Also, make your console/Interpreter FULL SCREEN


    Use key inputs such as 'a' to move left, 'w' to move up, 's' to move down
    'd' to move right


    Good luck... Will continue in 5 seconds...

    """)
    time.sleep(5)
    game()

def showMap():
    global hydration
    # We use concatenation
    print("----------------------------")
    print("You are in the " + rooms[currentRoom]["name"],"\n")
    print("Your current Inventory: " + str(inventory),"\n")
    # print("Your current hydration (%): " + str(hydration),"\n")
    global prog
    prog = progressBar(maxValue = 100)
    prog.updatePercentage(hydration)
    print("hydration:")
    prog.draw()
    print("----------------------------")
    if rooms[currentRoom]["name"] == "Hall":
        print("""
        _____________________________
        !            |              !
        !     Hall   |   Kitchen    !
        !(YOU ARE    |              !
        !   HERE)    |              !
        !---------------------------!
        !            |              !
        ! Bathroom   |    Bedroom   !
        !            |              !
        -----------------------------

        """)
    elif rooms[currentRoom]["name"] == "Kitchen":
        print("""
        _____________________________
        !            |              !
        !     Hall   |   Kitchen    !
        !            | (YOU ARE     !
        !            |    HERE)     !
        !            |              !
        !---------------------------!
        !            |              !
        ! Bathroom   |    Bedroom   !
        !            |              !
        -----------------------------

        """)
    elif rooms[currentRoom]["name"] == "Bedroom":
        print("""
        _____________________________
        !            |              !
        !     Hall   |   Kitchen    !
        !            |              !
        !            |              !
        !            |              !
        !---------------------------!
        !            |              !
        ! Bathroom   |    Bedroom   !
        !            |  (YOU ARE    !
        !            |      HERE)   !
        !            |              !
        -----------------------------

        """)
    elif rooms[currentRoom]["name"] == "Bathroom":
        print("""
        _____________________________
        !            |              !
        !     Hall   |   Kitchen    !
        !            |              !
        !            |              !
        !---------------------------!
        !            |              !
        ! Bathroom   |              !
        ! (YOU ARE   |              !
        !      HERE) |    Bedroom   !
        !            |              !
        -----------------------------

        """)
    else:
        print("Something unexpected occured. Stopping application & threads")
        hydrationOverTimeThread.exit()
        sys.exit()
    print("\n\n\n\n\n\n\n\n\n\n")

    if "item" in rooms[currentRoom]:
        print("You have found a " + rooms[currentRoom]["item"])
        print("\n")
        global hydration
        hydrationUpdate("-",25)
        if rooms[currentRoom]["item"] == "Water Bottle":
            hydrationUpdate("+",50)
showInstructions()
