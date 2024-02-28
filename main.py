#!a/usr/bin/env python3
import os
import src.utils.keyboard as keyboard

from src.utils import gamestate
from src import world, play, player, npc
from src.locations import tree

if __name__ == "__main__":
    game = play.Play()
    world = world.World()
    gamestate = gamestate.Gamestate()

    world.add_location(0, 0, 0, tree.Tree())
    world.add_location(0, 0, 1, tree.Tree())
    world.add_location(0, 0, 2, tree.Tree())
    
    player = player.Player('Player One', None, None)
    man1 = npc.NPC('Johny', None, 'blue')

    try:
        while True:
            game.render(world)
            key_pressed = keyboard.getkey()
            
            if key_pressed == 'esc' or key_pressed == 'q':
                print(f"\nQuitting at {game.get_game_time()}")
                gamestate.save(game, world)
                quit()
            else:
                # main loop
                game_time = game.set_game_time()
                game.play(key_pressed)

    except (KeyboardInterrupt, SystemExit):
        os.system('stty sane')
        print('stopping.')
