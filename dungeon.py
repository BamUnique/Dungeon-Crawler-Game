import monster
from colorama import Style, Fore
from player import Player


def entering_dungeon(chosen_class, class_name, traveller_name, dungeonLevel, monster_index):
    if dungeonLevel == 0:
        dungeonLevel = 1
    level = 0
    print('As you enter the dungeon you hear a voice:')
    print(f"Welcome {traveller_name} the {class_name} to my dungeon, you will be faced with the hardest of challenges"
          f" this is Dungeon {dungeonLevel}")
    print(f"Do you continue? (Press " + Style. BRIGHT + Fore.LIGHTBLUE_EX + "Enter" + Style.RESET_ALL + ')')
    confirm_entry = input()
    if confirm_entry != '':
        print("It's ok to be scared to try the Dungeon, try again later!")
    else:
        level = 1
    maxLevel = (dungeonLevel * 5)
    return maxLevel, level


def dungeon_interaction(chosen_class, class_name, traveller_name, dungeonLevel, maxLevel, level, monster_index):
    print(f"Well done {traveller_name} for accepting the challenge. I wish you the best of luck.")
    print(f'You enter floor {level} of {maxLevel}')
    number_of_monsters, monster_name, individual_monster_stats = monster.summon_monsters(monster_index, level)
    print(number_of_monsters, monster_name)
    print(individual_monster_stats)
    if number_of_monsters > 1:
        plurality = 's'
    else:
        plurality = ''
    print(f"On floor {level} you see {number_of_monsters} {monster_name}{plurality}, the {monster_name}{plurality} has "
          f"{individual_monster_stats['hp']}HP")

