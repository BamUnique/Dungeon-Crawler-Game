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

        with open("monster.json", 'r', encoding='utf-8') as f:
            monster_list = json.load(f)
            self.monster_name = monster_list['monsters'][self.index]['name']
        z = random.randint(1, level)
        monster_quan = [1, 5, 10, 25, 100, 500]
        self.number_of_monsters = int(z / monster_quan[self.index])

        self.monster_stats = monster_list['monsters'][self.index]['stats']



