import json
import random
import math


global monster_name, monster_hp, monster_defence, monster_strength, monster_wisdom, monster_agility


class Monster():

    def __init__(self, dungeonLevel, level):
        monster_indexes = [0, 20, 50, 100, 250, 100]

        for i in range(len(monster_indexes)-1):
            if monster_indexes[i] < level < monster_indexes[i+1]:
                self.index = i


        self.dungeonLevel = dungeonLevel

        with open("monster.json", 'r', encoding='utf-8') as f:
            monster_classes = json.load(f)

        current_monster = monster_classes["monsters"][self.index]
        setattr(self, 'monster_class_name', current_monster['name'])

        monster_stats = lambda name, points: setattr(self, name, float(points))

        for skill_name, skill_points in current_monster["stats"].items():
            monster_stats(skill_name, skill_points)


def summon_monsters(monster_index, level):
    with open("monster.json", 'r', encoding='utf-8') as f:
        monster_list = json.load(f)
        monster_name = monster_list['monsters'][monster_index]['name']
    z = random.randint(1, level)
    if monster_index == 1:
        z = z / 5
        z = math.ceil(z)
    elif monster_index == 2:
        z = z / 10
        z = math.ceil(z)
    elif monster_index == 3:
        z = z / 25
        z = math.ceil(z)
    elif monster_index == 4:
        z = z / 100
        z = math.ceil(z)
    elif monster_index == 5:
        z = z / 500
        z = math.ceil(z)
    number_of_monsters = z
    return number_of_monsters, monster_name, monster_list['monsters'][monster_index]['stats']


