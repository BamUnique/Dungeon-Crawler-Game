import json
from colorama import Style, Fore


def get_item_by_name(name,  item_dict):
    for subdict in item_dict:
        if subdict['name'] == name:
            return subdict
    return None


def your_item_equipped():
    with open('items.json', 'r', encoding='utf-8'):
        all_items = json.load(f)


global ITEMS, WEAPONS, ARMOUR


with open("items.json", 'r', encoding='utf-8') as f:
    ITEMS = json.load(f)

WEAPONS = ITEMS["weapons"]
ARMOUR = ITEMS["armour"]

def item_rarity(prefix):
    if prefix == 0:
        color = (Style.BRIGHT + Fore.WHITE)
    elif prefix == 1:
        color = (Style.BRIGHT + Fore.GREEN)
    elif prefix == 2:
        color = (Style.BRIGHT + Fore.BLUE)
    elif prefix == 3:
        color = (Style.BRIGHT + Fore.MAGENTA)
    elif prefix == 4:
        color = (Style.BRIGHT + Fore.LIGHTYELLOW_EX)
    elif prefix == 5:
        color = (Style.BRIGHT + Fore.LIGHTRED_EX)

    return color
