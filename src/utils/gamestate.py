class Gamestate:
    '''
    keeps information about current game state for saves,
    restoring game after crashes etc.
    '''

    def __init__(self) -> None:
        self.state = {}

    def save(self, game, world) -> str:
        '''
        saves game
        '''
        self.state = {
            'game_time': game.get_game_time(),
            'world_matrix': world.get_matrix()
        }

        print(self.state)
