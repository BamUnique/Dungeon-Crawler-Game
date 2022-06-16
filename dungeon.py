import monster
import json
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
    print(individual_monster_stats)
    total_monster_hp = int(individual_monster_stats['hp'] * number_of_monsters)
    if number_of_monsters > 1:
        plurality = 's'
    else:
        plurality = ''
    print(f"On floor {level} you see {number_of_monsters} {monster_name}{plurality}, they have "
          f"{individual_monster_stats['hp']}HP each")
    if number_of_monsters > 1:
        print(f"They have a total of {total_monster_hp}HP")

    with open('class_abilities.json', 'r', encoding='utf-8') as f:
        all_abilities = json.load(f)

    current_abilities = all_abilities["classes"][chosen_class]
    return current_abilities, number_of_monsters, monster, individual_monster_stats, total_monster_hp




def attack_phase(current_abilities):
    print(f"Choose an ability:")
    ability_num = 0
    valid_ability = False
    ability_list = []

    while valid_ability == False:
        for ability_type, ability_name in current_abilities["abilities"].items():
            print(f'{ability_num}.', ability_name)
            ability_num += 1
            ability_list.append(ability_name)
        print(ability_list[0])

       # for item in ability_list:
            #with open()


        chosen_ability = input()
        if chosen_ability == '0' or chosen_ability == ability_list[0]:
            pass
