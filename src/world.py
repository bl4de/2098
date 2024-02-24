from typing import List
from src.abstractLocation import AbstractLocation

class World:
    '''
    main class representing game's world
    '''

    def __init__(self, locations={}) -> None:
        '''
        initilaizes world with locations
        '''
        self.matrix = [
            [
                []
            ]
        ]


        self.locations = {}

    def add_location(self, level = 0, x = 0, y = 0, location = {}) -> None:
        '''
        adds location to the world matrix using coordinates
        '''
        self.matrix[level][0].append(location)
        
    def get_matrix(self) -> List:
        '''
        returns world's matrix
        '''
        return self.matrix

    def render(self) -> None:
        '''
        renders the world
        '''
        level = 0 # start from default level 1 - ground level

        for level in self.matrix:
            for row in level: 
                for location in row:
                    if location.get_type() in ['tree']:
                        location.render()
                    else:
                        pass
