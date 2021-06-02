STATES = ("SPLASH", "MAIN_MENU", "PLAYING_MENU", "PLAYING", "MAIN_SETTINGS", "PLAY_SETTINGS", "NEW_CHARACTER", "QUIT")
State = STATES[0]

def display_mainmenu():
    global State
    wrong_prompt = "Please enter a valid letter or number"
    prompt = "Would you like to:\n(q)uit\n(p)lay new character\n(s)ettings\n(c)ontinue old character\n"
    choice = input(prompt)
    while choice != 'q' and choice != 'p' and choice != 's' and choice != 'c':
        print(wrong_prompt)
        choice = input(prompt)

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
    while State == STATES[3]:
        print("play Game!!!")
        choice = input(prompt)
        if choice == 'm':
            State = STATES[2]

def display_playmenu():
    global State
    prompt = "Would you like to:\n(s)ettings\n(q)uit\n(c)ontinue playing\n"
    choice = input(prompt)
    while choice != 's' and choice != 'q' and choice != 'c':
        print("Sorry please enter a valid response")
        choice = input(prompt)

    if choice == 's':
        State = STATES[5]
    elif choice == 'q':
        State = STATES[1]
    elif choice == 'c':
        State = STATES[3]

def display_playsettings():
    global State
    prompt = "Would you like to (c)ontinue playing>\nGo back to the (m)enu?\n"
    choice = input(prompt)
    while choice != 'c' and choice != 'm':
        print("Sorry please enter a valid response\n")
        choice = input(prompt)

    if choice == 'c':
        State = STATES[3]
    elif choice == 'm':
        State = STATES[1]

def display_mainsettings():
    global State
    prompt = "Would you like to go back to the (m)enu?\n"
    choice = input(prompt)
    while choice != 'm':
        print("Please enter a valid response.\n")
        choice = input(prompt)

    if choice == 'm':
        State = STATES[1]

def display_newcharacterscreen():
    global State
    prompt = "Would you like to (c)reate a new character?\nGo back to the (m)enu?\n"
    choice = input(prompt)
    while choice != 'c' and choice != 'm':
        print("Please enter a valid response.\n")
        choice = input(prompt)

    if choice == 'c':
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





