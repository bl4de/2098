class Gamestate:
    '''
    keeps information about current game state for saves,
    restoring game after crashes etc.
    '''

    def __init__(self) -> None:
        self.state = {}

    def save(self, game) -> str:
        '''
        saves game
        '''
        self.state = {
            'game_time': game.get_game_time()
        }

        print(self.state)
