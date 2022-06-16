import dungeon
import interface
from player import Player


if __name__ == '__main__':
    dungeonLevel = 0
    monster_index = 0

    interface.main_menu()

    interface.main_menu_option()

    traveller_name = interface.player_name()

    chosen_class, class_name = interface.class_choice(traveller_name)

    p = Player(chosen_class, traveller_name, dungeonLevel)

    weapon = (p.inventory[0])["name"]
    armour = (p.inventory[1])

    interface.start_game_message(chosen_class, traveller_name, armour, weapon)

    maxLevel, level = dungeon.entering_dungeon(chosen_class, class_name, traveller_name, dungeonLevel, monster_index)

    current_abilities, number_of_monsters, monster, individual_monster_stats, total_monster_hp = \
        dungeon.dungeon_interaction(chosen_class, class_name, traveller_name,
                                    dungeonLevel, maxLevel, level, monster_index)

    dungeon.attack_phase(current_abilities)
