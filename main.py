import damage
import dungeon
import interface
from player import Player
from monster import Monster


if __name__ == '__main__':
    dungeonLevel = 0

    interface.main_menu()

    interface.main_menu_option()

    traveller_name = interface.player_name()

    chosen_class, class_name = interface.class_choice(traveller_name)

    p = Player(chosen_class, traveller_name, dungeonLevel)

    weapon = (p.inventory[0])["name"]
    armour = (p.inventory[1])
    cooldown = 0

    interface.start_game_message(chosen_class, traveller_name, armour, weapon)
    while game_run == True:



        maxLevel, level = dungeon.entering_dungeon(chosen_class, traveller_name, dungeonLevel)

        while level <= maxLevel:

            m = Monster(dungeonLevel, level)

            current_abilities = dungeon.dungeon_interaction(chosen_class, class_name, traveller_name,
                                                                              dungeonLevel, maxLevel, level, m.index)

            attack_first = damage.who_fights_first(m, p)

            player_damage, does_hit, dodge = dungeon.attack_phase(current_abilities, chosen_class, m, p)

            if attack_first == 'monster':
                damage.monster_fight(player_damage, does_hit, dodge, cooldown)
            elif attack_first == 'player':
                damage.player_fight()

