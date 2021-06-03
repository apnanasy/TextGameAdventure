STATES = ("SPLASH", "MAIN_MENU", "PLAYING_MENU", "PLAYING", "MAIN_SETTINGS", "PLAY_SETTINGS", "NEW_CHARACTER", "QUIT")
State = STATES[0]
class Player:
    def __init__(self, name):
        self.name = name

class Game:
    def __init__(self, player):
        self.player = player

def get_input(prompt, choices):
    choice = input(prompt)
    while choice not in choices:
        print("Please please please enter a valid response")
        choice = input(prompt)

    return choice

def display_mainmenu():
    global State
    prompt = "Would you like to:\n(q)uit\n(p)lay new character\n(s)ettings\n(c)ontinue old character\n"
    possibles = ('q', 'p', 's', 'c')

    choice = get_input(prompt, possibles)

    if choice == 'q':
        State = STATES[7]
    elif choice == 'p':
        State = STATES[6]
    elif choice == 's':
        State = STATES[4]
    elif choice == 'c':
        State = STATES[3]

def display_splashscreen():
    print("Welcome to the text adventure!!!!!")

def display_playscreen():
    global State
    prompt = "Would you like to enter (m)enu?"
    possibles = ('m')
    while State == STATES[3]:
        print("play Game!!!")
        choice = get_input(prompt, possibles)
        if choice == 'm':
            State = STATES[2]

def display_playmenu():
    global State
    prompt = "Would you like to:\n(s)ettings\n(q)uit\n(c)ontinue playing\n"
    possibles = ('s','q','c')
    choice = get_input(prompt, possibles)

    if choice == 's':
        State = STATES[5]
    elif choice == 'q':
        State = STATES[1]
    elif choice == 'c':
        State = STATES[3]

def display_playsettings():
    global State
    prompt = "Would you like to (c)ontinue playing>\nGo back to the (m)enu?\n"
    possibles = ('c','m')
    choice = get_input(prompt, possibles)

    if choice == 'c':
        State = STATES[3]
    elif choice == 'm':
        State = STATES[1]

def display_mainsettings():
    global State
    prompt = "Would you like to go back to the (m)enu?\n"
    possibles = ('m')
    choice = get_input(prompt, possibles)

    if choice == 'm':
        State = STATES[1]

def display_newcharacterscreen():
    global State
    prompt = "Would you like to (c)reate a new character?\nGo back to the (m)enu?\n"
    possibles = ('c','m')
    choice = get_input(prompt, possibles)

    if choice == 'c':
        prompt = "what would you like your name to be?\n"
        name = input(prompt)
        while len(name) <= 1 or len(name) > 12:
            print(" Please enter a name between 1 and 12 characters")
            name = input(prompt)

        player = Player(name)
        game = Game(player)
        print("Your new name is: " + game.player.name)
        State = STATES[3]
    elif choice == 'm':
        State = STATES[1]




   


while State != STATES[7]:
    if State == STATES[0]:
        display_splashscreen()
        State = STATES[1]
    elif State == STATES[1]:
        display_mainmenu()
    elif State == STATES[2]:
        display_playmenu()
    elif State == STATES[3]:
        display_playscreen()
    elif State == STATES[4]:
        display_mainsettings()
    elif State == STATES[5]:
        display_playsettings()
    elif State == STATES[6]:
        display_newcharacterscreen()


print("GoodBye!!!")





