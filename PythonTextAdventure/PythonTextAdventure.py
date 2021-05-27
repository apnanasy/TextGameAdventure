##health = 7
#attack = 1
#turn = 0
#quit = "q"
STATES = ("INITIAL", "MAIN_MENU", "PLAYING_MENU", "PLAYING", "QUIT")
State = STATES[0]

class Player:
    def __init__(self, total_health, attack, current_tile):
        self.total_health = total_health
        self.attack = attack
        self.health = total_health - 3
        self.current_tile = current_tile

    def get_health_string(self):
        if self.health <= 0:
            return "You suddenly see a bright light..... and hear soft voices calling to you"
        elif self.health >= total_health:
            return "You feel like a million bucks!"
        elif self.health > total_health / 2:
            return "You're battered and bruised but in ok condition"
        else:
            return "You're bleeding from places you didn't even know existed....Seek medical attention"

class Tile:
    def __init__(self, name, description, actions, movements, events, discovered):
        self.name = name
        self.description = description
        self.actions = actions
        self.movements = movements
        self.events = events
        self.discovered = discovered

class Special_Event:
    def __init__(self, description):
        self.description = description


def get_player_choice(prompt, choices):
    choice = "null"
    choices.append(quit)
    while choice not in choices:
        if choice == "null":
            choice = input(prompt)
        else:
            choice = input("You look around sheepishly, please enter: " + str(choices))
    return choice

def display_mainmenu():
    wrong_prompt = "Please enter a valid letter or number"
    prompt = "Would you like to:\n(q)uit"
    choice = input(prompt)
    while choice != 'q':
        print(wrong_prompt)
        choice = input(prompt)
    State = STATES[4]

def display_splashscreen():
    print("Welcome to the text adventure!!!!!")


while State != STATES[4]:
    if State == STATES[0]:
        display_splashscreen()
        State = STATES[1]
    elif State == STATES[1]:
        display_mainmenu()





start_desc = "Press m or e. You awaken with a jolt like someone rising from a night terror./n You find rough granite, dimly lit by a fire next to you, surrounding you on all sides except for a hallway on the other side of the room."
#start_event = Special_Event("A small fire cackles in the center of the room")
#starting_tile = Tile("Start", start_desc, ["m","e"], "Hallway", start_event, False)
#hall_desc = "The hall is dark and there is something in the middle"
#hall_event = Special_Event("A stalagtite comes out of nowhere and rings your bell")
#hall_tile = Tile("Hallway", hall_desc, ["b", "f"], "Start", hall_event, False)
#first_player = Player(10, 1, starting_tile)
#player_input = ""
#print("Zombie World!!!!")
#print()

#while player_input != "q":
#    if first_player.current_tile.discovered == False:
#        print(first_player.current_tile.events.description)
#        first_player.current_tile.discovered = True

#    print(first_player.current_tile.description)
#    player_input = get_player_choice("What would you like to do: ", first_player.current_tile.actions)

#    if player_input == "m":
#        health = health - 7
#        print(first_player.get_health_string() )
#        first_player.current_tile = hall_tile
#    elif player_input == "e":
#        print("You try to look around you but the room is to dark. Grabbing one of the of the half burned sticks from the fire you use it as a torch")
#        print(first_player.get_health_string())

 #   turn += turn










