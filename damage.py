import random

def who_fights_first(m, p):
    if p.player_stats['agility'] >= m.monster_stats['agility']:
        attack_first = 'player'
    else:
        attack_first = 'monster'
    return attack_first

def monster_fight(player_damage, does_hit, dodge, cooldown):
    if dodge == 'Stun':
        cooldown = 1
    else:
        cooldown -= 1

def player_fight():
    pass