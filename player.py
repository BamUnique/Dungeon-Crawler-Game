import json

import items

class Player():

    def __init__(self, class_index, traveller_name, dungeonLevel):

        self.name = traveller_name
        self.dungeonLevel = dungeonLevel
        self.player_class_index = class_index

        self.inventory = []
        self.equip_slots = {}

        self.set_class(class_index)

    def set_class(self, class_index):
        with open('classes.json', 'r', encoding='utf-8') as f:
            player_classes = json.load(f)

        current_class = player_classes["classes"][class_index]
        setattr(self, 'player_class_name', current_class['name'])

        set_skill = lambda name, points: setattr(self, name, float(points) + (float(points) * (0.1 * self.dungeonLevel)))

        for skill_name, skill_points in current_class["skills"].items():
            set_skill(skill_name, skill_points)

        for equip_slot, equipment_name in current_class["kit"].items():
            if equip_slot:
                eq = items.get_item_by_name(equipment_name, items.WEAPONS)
                if eq:
                    self.inventory.append(eq)
                else:
                    self.inventory.append(equipment_name)

            self.equip_slots[equip_slot] = equipment_name


class Equipment():

    def __init__(self, equipment_dict):

        self.name = equipment_dict["name"]
        self.type = equipment_dict["type"]

        self.rarity = equipment_dict["rarity"]
        self.rarity_name = items.ITEM_RARITY[self.rarity]

        self.rarity_prefix = items.ITEM_RARITY_COLOR[self.rarity_name]

        self.buffs = equipment_dict["buffs"]

    def __str__(self):

        pretty_name = self.rarity_prefix + self.name

        return pretty_name