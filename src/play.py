from src.utils.gamestate import Gamestate
from src.utils.screen import Screen


class Play:
    '''
    main game class
    '''

    def __init__(self) -> None:
        '''
        init new game
        '''
        self.game_time = 0

    def play(self, key_pressed='') -> None:
        '''
        executes game single round
        '''
        # print(key_pressed + ' was pressed')
        pass

    def render(self, world) -> None:
        '''
        renders the screen (menu, world)
        '''
        Screen.clear_screen()
        print(f"Game time {self.get_game_time()}\n")
        world.render()

    def get_game_time(self) -> int:
        '''
        returns current time in game
        '''
        return self.game_time

    def set_game_time(self, delta=1) -> int:
        '''
        sets and returns game time
        by default timer is increased by 1 unit
        '''
        self.game_time += delta
        return self.game_time
