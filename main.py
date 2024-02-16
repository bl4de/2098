#!/usr/bin/env python3
import os
import src.utils.keyboard as keyboard

from src.utils import gamestate
from src import play, player, npc

if __name__ == "__main__":
    game = play.Play()
    gamestate = gamestate.Gamestate()
    player = player.Player()

    try:
        while True:
            key_pressed = keyboard.getkey()
            if key_pressed == 'esc' or key_pressed == 'q':
                gamestate.save(game)
                quit()
            else:
                # main loop
                print(player)

                game.play(key_pressed)

                game_time = game.set_game_time()

                print(game_time)

    except (KeyboardInterrupt, SystemExit):
        os.system('stty sane')
        print('stopping.')
