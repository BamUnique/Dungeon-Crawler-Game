import random
import json
from player import Player

import choice
from colorama import init, Fore, Style

import item

def main_menu():
    init(autoreset=True)
    print(Style.DIM + Fore.LIGHTRED_EX + " ██████  ██████  ███    ███ ██████   █████  ████████" + Style.RESET_ALL +
          "     ███████ ██ ███    ███ ██    ██ ██       █████  ████████  ██████  ██████")
    print(Style.DIM + Fore.LIGHTRED_EX + "██      ██    ██ ████  ████ ██   ██ ██   ██    ██" + Style.RESET_ALL +
          "        ██      ██ ████  ████ ██    ██ ██      ██   ██    ██    ██    ██ ██   ██")
    print(Style.DIM + Fore.LIGHTRED_EX + "██      ██    ██ ██ ████ ██ ██████  ███████    ██" + Style.RESET_ALL +
          "        ███████ ██ ██ ████ ██ ██    ██ ██      ███████    ██    ██    ██ ██████")
    print(Style.DIM + Fore.LIGHTRED_EX + "██      ██    ██ ██  ██  ██ ██   ██ ██   ██    ██" + Style.RESET_ALL +
          "             ██ ██ ██  ██  ██ ██    ██ ██      ██   ██    ██    ██    ██ ██   ██")
    print(Style.DIM + Fore.LIGHTRED_EX + " ██████  ██████  ██      ██ ██████  ██   ██    ██" + Style.RESET_ALL +
          "        ███████ ██ ██      ██  ██████  ███████ ██   ██    ██     ██████  ██   ██")

def main_menu_option():
    print("Choose an option:")
    print('1. Start Game')
    print('2. Show Rarities')
    print('3. Quit')
    choice = input()
    if choice == '1':
        pass


def player_name():
    print('Welcome Traveller, What is your name?')
    traveller_name = input()

    return traveller_name


def class_choice(traveller_name):
    class_options = ["Berserker", "Archer", "Mage", "Tank"]

    chosen = choice.Menu(class_options, title=f'Choose your class, {traveller_name}').ask()
    chosen_class = class_options.index(chosen)
    return chosen_class, chosen


def start_game_message(class_index, p):

    berserker_message = f"You woke up this morning with a burning fire in the pit of your stomach, finally you are " \
                        f"able to equip your worn {p.current_armour}" + Style.RESET_ALL + " and \n" \
                        f"sheath your {p.current_weapon}" + Style.RESET_ALL + " in its scabbard on your hip, " \
                                                                              "after this you say farewell " \
                        f"to your family, you enter the dungeon.."

    archer_message = f"Within minutes after getting the message from the King about the dungeon that has claimed many" \
                     f" warriors, you have already donned your {p.current_armour}" + Style.RESET_ALL + "\n" \
                     f" filled your quiver and made sure {p.current_weapon}" + Style.RESET_ALL + " was on " \
                                                                                                 "your horse, then " \
                     f"you make haste towards the dungeon.."

    mage_message = f"Your brain raced as you went to pack for the journey, finally " \
                   f"it was time to put the years of studying the arcance to use. \n" \
                   f"You polish your {p.current_weapon}" + Style.RESET_ALL + f" and slip " \
                                                     f"it into {p.current_armour}, "  + Style.RESET_ALL +\
                   f"then on your magic broom, start the long trip to the dungeon.."

    tank_message = f"When faced with the challenge of the dungeon you have your strong {p.current_armour} "\
                   + Style.RESET_ALL + " equipped " \
                   f"alongside your trusty {p.current_weapon}," + Style.RESET_ALL + " slowly you made your way \n" \
                   f"into the dungeon.."

    messages = [berserker_message, archer_message, mage_message, tank_message]

    class_message = messages[class_index]
    print(class_message)


def in_game_interface():
    x = False
    while x:
        print("Choose an option:")
        print("1. Enter the Dungeon")
        print("2. Inventory")
        print("3. Quit Game")
        option = input()
        if option == '1':
            x = True
        elif option == '2':
            x = True
        elif option == '3':
            print(Style.BRIGHT + Fore.RED + 'Warning!' + Style.RESET_ALL + "Quitting is the same as dying"
                                                                           "You will lose all current progress")
            print("Type" + Style.BRIGHT + Fore.GREEN + "YES")
