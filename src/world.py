import os
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
            [0, 1, 2],
            [0, 1, 2],
            [0, 1, 2]
        ]
        self.locations = {}

    def get_matrix(self) -> List:
        '''
        returns world's matrix
        '''
        return self.matrix

    def draw(self) -> None:
        '''
        re-draws the world
        '''
        for x in self.matrix:
            for y in x:
                print(y, end='')
            print()
