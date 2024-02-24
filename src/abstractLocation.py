class AbstractLocation:
    '''
    base abstract class representing location in game
    '''
    TYPE = 'empty'  # buidling, street, Rapid Transit System, ??

    MATRIX = []

    def __init__(self, type = None, matrix = None) -> None:
        '''
        initializes location
        '''
        self.TYPE = type if type is not None else self.TYPE
        self.MATRIX = matrix if matrix is not None else self.MATRIX

    def get_type(self) -> str:
        return self.TYPE

    def render(self):
        pass

