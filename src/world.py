from typing import List


class World:
    '''
    main class representing game's world
    '''

    def __init__(self, locations={}) -> None:
        '''
        initilaizes world with locations
        '''
        self.matrix = [
            ['empty','empty', 'empty'],
            ['empty','empty', 'empty'],
            ['empty','empty', 'empty']
        ]
        self.locations = {}

    def get_matrix(self) -> List:
        '''
        returns world's matrix
        '''
        return self.matrix

    def render(self) -> None:
        '''
        renders the world
        '''
        for x in self.matrix:
            for y in x:
                print(y, end='')
            print()
