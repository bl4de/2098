from src.abstractSimpleLocation import AbstractSimpleLocation

class Tree(AbstractSimpleLocation):
    '''
    class to create objects representing trees
    '''

    def __init__(self) -> None:
        '''
        Simple Location representing a tree
        '''
        self.TYPE =  'tree'
        self.SYMBOL = '\U0001F332'

