import time
import random
import json
from player import Player

import choice
from colorama import init, Fore, Style

import items

def main_menu():
    init(autoreset=True)
    print(Style.DIM + Fore.LIGHTRED_EX + " ██████  ██████  ███    ███ ██████   █████  ████████" + Style.RESET_ALL + "     ███████ ██ ███    ███ ██    ██ ██       █████  ████████  ██████  ██████")
    print(Style.DIM + Fore.LIGHTRED_EX + "██      ██    ██ ████  ████ ██   ██ ██   ██    ██" + Style.RESET_ALL + "        ██      ██ ████  ████ ██    ██ ██      ██   ██    ██    ██    ██ ██   ██")
    print(Style.DIM + Fore.LIGHTRED_EX + "██      ██    ██ ██ ████ ██ ██████  ███████    ██" + Style.RESET_ALL + "        ███████ ██ ██ ████ ██ ██    ██ ██      ███████    ██    ██    ██ ██████")
    print(Style.DIM + Fore.LIGHTRED_EX + "██      ██    ██ ██  ██  ██ ██   ██ ██   ██    ██" + Style.RESET_ALL + "             ██ ██ ██  ██  ██ ██    ██ ██      ██   ██    ██    ██    ██ ██   ██")
    print(Style.DIM + Fore.LIGHTRED_EX + " ██████  ██████  ██      ██ ██████  ██   ██    ██" + Style.RESET_ALL + "        ███████ ██ ██      ██  ██████  ███████ ██   ██    ██     ██████  ██   ██")

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


def start_game_message(class_index, traveller_name, armour_name, weapon_name):

    berserker_message = f"You woke up this morning with a burning fire in the pit of your stomach, finally you are able to equip your worn {armour_name} and \n" \
                        f"sheath your {weapon_name} in its scabbard on your hip, after this you say farewell to your family, you enter the dungeon.."

    archer_message = f"Within minutes after getting the message from the King about the dungeon that has claimed many warriors, you have already donned your {armour_name,}\n" \
                     f" filled your quiver and made sure {weapon_name} was on your horse, then you make haste towards the dungeon.."

    mage_message = f"Your brain raced as you went to pack for the journey, finally it was time to put the years of studying the arcance to use. You polish your {weapon_name} \n" \
                   f"and slip it into {armour_name}, then on your magic broom, start the long trip to the dungeon.."

    tank_message = f"When faced with the challenge of the dungeon you have your strong {armour_name} equipped alongside your trusty {weapon_name}, slowly you made your way \n" \
                   f"into the dungeon.."

    messages = [berserker_message, archer_message, mage_message, tank_message]

    class_message = messages[class_index]
    print(class_message)