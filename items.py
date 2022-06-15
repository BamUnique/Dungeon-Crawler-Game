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


global ITEMS, WEAPONS, ARMOUR, SPELLS, ITEM_RARITY, ITEM_RARITY_COLOR


with open("items.json", 'r', encoding='utf-8') as f:
    ITEMS = json.load(f)

WEAPONS = ITEMS["weapons"]
ARMOUR = ITEMS["armour"]
SPELLS = ITEMS["spells"]

ITEM_RARITY_COLOR = {
    "Common": Style.BRIGHT + Fore.WHITE,
    "Uncommon": Style.BRIGHT + Fore.GREEN,
    "Rare": Style.BRIGHT + Fore.BLUE,
    "Epic": Style.BRIGHT + Fore.MAGENTA,
    "Legendary": Style.BRIGHT + Fore.LIGHTYELLOW_EX,
    "Mythical": Style.BRIGHT + Fore.LIGHTRED_EX
}

ITEM_RARITY = ITEM_RARITY_COLOR.keys()