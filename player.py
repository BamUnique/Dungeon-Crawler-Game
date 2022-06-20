import json
import item


class Player():

    def __init__(self, class_index, traveller_name, dungeonLevel):
        self.name = traveller_name
        self.dungeonLevel = dungeonLevel
        self.player_class_index = class_index

        self.inventory = []
        self.equip_slots = {}

        self.player_stats = {}

        self.set_class(class_index)


    def set_class(self, class_index):
        with open('classes.json', 'r', encoding='utf-8') as f:
            player_classes = json.load(f)

        current_class = player_classes["classes"][class_index]
        setattr(self, 'player_class_name', current_class['name'])

        set_skill = lambda name, points: setattr(self, name, float(points) + (float(points) * (0.1 * self.dungeonLevel)))

        for skill_name, skill_points in current_class["skills"].items():
            set_skill(skill_name, skill_points)
            self.player_stats.update({skill_name: skill_points})

        for equip_slot, equipment_name in current_class["kit"].items():
            if equip_slot:
                weapon = item.get_item_by_name(equipment_name, item.WEAPONS)
                if weapon:
                    self.inventory.append(weapon)
                armour = item.get_item_by_name(equipment_name, item.ARMOUR)
                if armour:
                    self.inventory.append(armour)

            self.equip_slots[equip_slot] = equipment_name
        e = Equipment(self.inventory)
        self.current_weapon = e.pretty_weapon
        self.current_armour = e.pretty_armour



class Equipment():

    def __init__(self, equipment_dict):

        self.weapon_rarity = equipment_dict[0]["rarity"]
        self.weapon_rarity_prefix = (item.item_rarity(self.weapon_rarity))
        self.equipped_weapon = equipment_dict[0]['name']
        self.pretty_weapon = self.weapon_rarity_prefix + self.equipped_weapon

        self.armour_rarity = equipment_dict[1]["rarity"]
        self.armour_rarity_prefix = (item.item_rarity(self.armour_rarity))
        self.equipped_armour = equipment_dict[1]['name']
        self.pretty_armour = self.armour_rarity_prefix + self.equipped_armour
