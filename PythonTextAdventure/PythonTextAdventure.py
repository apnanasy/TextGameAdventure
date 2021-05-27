STATES = ("INITIAL", "MAIN_MENU", "PLAYING_MENU", "PLAYING", "QUIT")
State = STATES[0]

def display_mainmenu():
    global State
    wrong_prompt = "Please enter a valid letter or number"
    prompt = "Would you like to:\n(q)uit\n(p)lay\n"
    choice = input(prompt)
    while choice != 'q' and choice != 'p':
        print(wrong_prompt)
        choice = input(prompt)

    if choice == 'q':
        State = STATES[4]
    elif choice == 'p':
        State = STATES[3]

def display_splashscreen():
    print("Welcome to the text adventure!!!!!")

def run():
    global State
    print("Thank you for playing")
    State = STATES[4]
   


while State != STATES[4]:
    if State == STATES[0]:
        display_splashscreen()
        State = STATES[1]
    elif State == STATES[1]:
        display_mainmenu()
    elif State == STATES[3]:
        run()

print("GoodBye!!!")





