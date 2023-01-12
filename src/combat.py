
from random import randint

import pyxel

import world
from player import Player

def send_msg(world, msg, col):
    world.journal.push_new_line(msg, col)

def kill_enemy(world, enemy):
    world.current_map.entities.remove(enemy)

def player_attacked_enemy(world, player, enemy):
    enemy.hp = max(0, enemy.hp - (player.attack + Player.WEAPONS[player.weapon][0]))
    if enemy.hp == 0:
        send_msg(world, "You traded with the " + enemy.name + \
            " and got " + str(enemy.xp) + " tokens!", 3)
        player.add_xp(world, enemy.xp)
        # kill_enemy(world, enemy)
    else:
        send_msg(world, "You talk to the " + enemy.name + ".", 11)

def enemy_attacked_player(world, enemy, player):
    shield_val = Player.SHIELDS[player.shield][0]
    print(shield_val)
    if randint(1, 100) <= shield_val:
        pass # send_msg(world, "The " + enemy.name + " is.", 12)
    else:
        player.hp = max(0, player.hp - enemy.attack)
        if player.hp == 0:
            player.add_xp(world, enemy.xp)
            player.hp = 10 # reincarnate
            # pyxel.stop()
            # pyxel.playm(2, loop=False)
            send_msg(world, "The " + enemy.name + " touches you.", 12)
            # world.set_game_over()
        else:
            send_msg(world, "The " + enemy.name + " looks at you.", 11)
