#!a/usr/bin/env python3
import os
import src.utils.keyboard as keyboard

from src.utils import gamestate
from src import world, play, player, npc

if __name__ == "__main__":
    game = play.Play()
    world = world.World()
    gamestate = gamestate.Gamestate()
    player = player.Player()

    try:
        game.render(world)
        while True:
            key_pressed = keyboard.getkey()
            if key_pressed == 'esc' or key_pressed == 'q':
                print(f"\nQuitting at {game.get_game_time()}")
                gamestate.save(game, world)
                quit()
            else:
                # main loop
                game.render(world)
                game_time = game.set_game_time()

                game.play(key_pressed)

    except (KeyboardInterrupt, SystemExit):
        os.system('stty sane')
        print('stopping.')
