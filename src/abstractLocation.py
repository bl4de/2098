class AbstractLocation:
    '''
    base abstract class representing location in game
    '''
    TYPE = 'ground'  # buidling, street, Rapid Transit System, ??

    ICON = '.'  # default for ground

    def __init__(self, type = None, icon = None) -> None:
        self.TYPE = type if type is not None else self.TYPE
        self.ICON = icon if icon is not None else self.ICON
        
    def draw(self) -> None:
        '''
        rendering location
        '''
        pass
