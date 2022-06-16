import json
import random
import math


global monster_name, monster_hp, monster_defence, monster_strength, monster_wisdom, monster_agility


class Monster():

    def __init__(self, monster_index, dungeonLevel, level):
        if level < 20:
            monster_index = 0
        elif level < 50:
            monster_index = 1
        elif level < 100:
            monster_index = 2
        elif level < 250:
            monster_index = 3
        elif level < 1000:
            monster_index = 4
        elif level >= 1000:
            monster_index = 5

        self.dungeonLevel = dungeonLevel
        self.monster_class_index = monster_index

        self.get_monster(monster_index, level)


    def get_monster(self, monster_index, level):

        with open("monster.json", 'r', encoding='utf-8') as f:
            monster_classes = json.load(f)

        current_monster = monster_classes["monsters"][monster_index]
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


