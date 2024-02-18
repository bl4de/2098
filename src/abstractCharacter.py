class AbstractCharacter:
    '''
    abstract character class
    all characters in game inherits form this class
    '''
    AVATAR = ''
    
    # initial stats
    HEALTH = 100
    
    STRENGTH = 10
    
    MODE = 'friendly' # 'none', 'angry', 'aggresive', ??

    # location in world
    LEVEL = 0

    POS_X = 0

    POS_Y = 0

    def __init__(self, avatar) -> None:
        '''
        character initialization
        '''
        self.AVATAR = avatar
        self.POS_X = 0
        self.POS_Y = 0

    def move(self, pos_x: int, pos_y: int, level = None) -> None:
        '''
        character move
        '''
        self.POS_X = pos_x
        self.POS_Y = pos_y
        self.LEVEL = level if int(level) > 0 else self.LEVEL

    def getPosX(self) -> int:
        return self.POS_X

    def getPosY(self) -> int:
        return self.POS_Y

    def getLevel(self) -> int:
        return self.LEVEL
