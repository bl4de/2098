from . import abstractCharacter

class Player(abstractCharacter.AbstractCharacter):
    '''
    class representing main character
    '''
    def __init__(self, avatar_name, avatar, color) -> None:
        super().__init__(avatar_name, avatar = '\U0000c6c3' )

    def __str__(self):
        return self.AVATAR
