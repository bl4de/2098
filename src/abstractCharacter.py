import src.utils.keyboard as keyboard

class AbstractCharacter:
    '''
    abstract character class
    all characters in game inherits form this class
    '''
    AVATAR = ''

    COLOR = keyboard.colors['white']

    # initial stats
    HEALTH = 100

    STRENGTH = 10

    MODE = 'friendly' # 'none', 'angry', 'aggresive', ??

    # location in world
    LEVEL = 0

    POS_X = 0

    POS_Y = 0

    def __init__(self, avatar_name, avatar, color = None) -> None:
        '''
        character initialization
        '''
        self.avatar_name = avatar_name
        self.avatar = avatar
        self.color = color if color is not None else self.COLOR
        self.POS_X = 0
        self.POS_Y = 0

    def move(self, pos_x: int, pos_y: int, level = 1) -> None:
        '''
        character move
        '''
        self.POS_X = pos_x
        self.POS_Y = pos_y
        self.LEVEL = level if int(level) >= 1 else self.LEVEL

    def getX(self) -> int:
        return self.POS_X

    def getY(self) -> int:
        return self.POS_Y

    def getLevel(self) -> int:
        return self.LEVEL

    def render(self) -> None:
        '''
        returns character's avatar for rendering
        '''
        print(f"{self.color}{self.avatar}")

