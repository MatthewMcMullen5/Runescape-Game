from os import system, name
import random
from Bestiary import *


class Character:
    def __init__(self, name, health, inventory, level):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.level = level


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def game_header():
    print(f"{bcolors.UNDERLINE}{bcolors.OKBLUE}{bcolors.BOLD}*ﾟ✧ WELCOME TO RUNESCAPE ✧ﾟ*"
          f"\n{bcolors.ENDC}~{user.name}~      ~HP {user.health}~        ~LVL {user.level}~\n")


def fight_header():
    print(
        f"{bcolors.UNDERLINE}{bcolors.FAIL}{bcolors.BOLD}*ﾟ✧ ENCOUNTER ✧ﾟ*\n"
        f"{bcolors.ENDC}~{user.name}~      ~HP {user.health}~        ~LVL {user.level}~\n")


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def home_screen():
    options = ['fight', 'rest', 'check', 'quit']
    choice = False
    has_healed = False

    while choice is not True:
        game_header()
        data = str(input("Choose what to do next!\nFight - Rest - Check - Quit\n"))
        clear()

        if data.lower() == "fight":
            fight()
            choice = True
            has_healed = False

        if data.lower() == "rest":
            if has_healed is False:
                rest()
                has_healed = True
                choice = True
            else:
                home_screen()

        if data.lower() == "check":
            check()
            choice = True

        if data.lower() == "quit":
            clear()
            user.health = 0
            game_header()
            print("Thank you for playing!\n")
            quit()

        if data.lower() not in options:
            print("invalid input, try again")
            clear()


def rest():
    random_heal = random.randrange(1, 11)
    print(f"You rest, and heal {bcolors.FAIL}{random_heal}{bcolors.ENDC} health.")
    user.health += random_heal
    home_screen()


def fight():
    encounter = monster_list[random.randrange(2)]
    encounter_health = encounter.hp
    print(f"You have started an encounter with {encounter.name}!")

    while encounter_health > 0:
        fight_header()
        print(f"{bcolors.UNDERLINE}{bcolors.FAIL}{bcolors.BOLD}*ﾟ✧ {encounter.name} HP{encounter_health}/{encounter.hp} ✧ﾟ*{bcolors.ENDC}")
        decide = input("Attack    Run    Info    ").lower()
        print("\n")

        if user.health < 1:
            die()

        if decide == "attack":
            damage = random.randrange(user.level + 5)
            encounter_health -= damage

            encounter_damage = random.randrange(encounter.attack)
            user.health -= encounter_damage

            print(f"The {encounter.name} deals {bcolors.FAIL}{encounter_damage}{bcolors.ENDC} damage!")
            print(f"You deal {bcolors.FAIL}{damage}{bcolors.ENDC} damage to the {encounter.name}!")
            continue

        if decide == "run":
            run_penalty = random.randrange(encounter.attack)
            user.health -= run_penalty
            print(f"The {encounter.name} hits you for {run_penalty} as you flee!")
            home_screen()

        if decide == "info":
            print(f"You are fighting a level {encounter.level} {encounter.name} with {encounter.hp} HP {encounter.defence} "
                  f"defence and {encounter.attack} attack.")
            continue

        else:
            fight_header()
            continue

    user.level += encounter.level
    print(f"You have defeated the {encounter.name} and gained {encounter.level} XP!")
    home_screen()


def check():
    print("You check your equipment")
    home_screen()

def die():
    print("Oh dear, you are dead.")
    quit()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~GAME STARTS HERE~~~~~~~~~~~~~~~~~~~~~~~~#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

user = Character("", 5, [], 0)
game_header()

user.name = str(input("Choose a name! "))

clear()
game_header()

age_limit = 16
is_old_enough = False
while is_old_enough is not True:
    try:
        age = int(input("How old are you? "))

        if age >= age_limit:
            print("You're old enough to play!")
            is_old_enough = True

        if age < age_limit:
            print(f"You're not old enough to play! It's for ages {age_limit} and up!")
            exit()

    except (ValueError, NameError):
        clear()
        game_header()
        print("Enter a number you dingus.")

wants_to_play = False
while wants_to_play is not True:

    decision = input(f"Would you like to play? (Yes/No) ").lower()

    if decision == "yes":
        wants_to_play = True

    elif decision == "no":
        clear()
        game_header()
        print("Understandable, have a nice day.")
        exit()

clear()

home_screen()
