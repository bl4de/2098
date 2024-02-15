#!/usr/bin/env python3
import os

import src.utils.keyboard as keyboard
from src.game.game import Game

if __name__ == "__main__":
    game = Game()
    try:
        while True:
            key_pressed = keyboard.getkey()
            if key_pressed == 'esc' or key_pressed == 'q':
                game.save()
                quit()
            else:
                # main loop
                game.play(key_pressed)

    except (KeyboardInterrupt, SystemExit):
        os.system('stty sane')
        print('stopping.')
