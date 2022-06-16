import monster
import json
import choice
import math
import random
from colorama import Style, Fore
from player import Player


def entering_dungeon(class_name, traveller_name, dungeonLevel):
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




def attack_phase(current_abilities, chosen_class):
    ability_list = []

    for ability_type, ability_name in current_abilities["abilities"].items():
        ability_list.append(ability_name)

    with open('ability_damage.json', 'r', encoding='utf-8') as f:
        ability_damages = json.load(f)

    chosen = choice.Menu(ability_list, title='Choose your ability').ask()
    chosen_ability = ability_list.index(chosen)
    type_list = ['damaging_abilities', 'misc_abilities']
    chosen_index = math.floor(chosen_ability/2)
    type_of_abilities = type_list[chosen_index]
    ability_class_index = chosen_ability + (2*chosen_class)

    stats = ability_damages[type_of_abilities][ability_class_index]
    name = stats['name']
    if type_of_abilities == 'misc_abilities':
        chosen_ability_type = stats['type']
        print(f'You used {chosen_ability_name} to {chosen_ability_type}')
    else:
        chosen_ability_damage = stats['damage']
        damage_type = stats['damage_type']
        chance_of_hit = stats['chance_of_hit']
        per_chance = int(chance_of_hit * 10)
        hit_list = ['True', 'False']
        chance = [per_chance,(100-per_chance)]
        does_hit = random.choices(hit_list, chance)

        if does_hit == 'True':
            print(f"You used {name} doing {chosen_ability_damage} {damage_type}")
