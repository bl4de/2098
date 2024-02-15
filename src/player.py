from . import abstractCharacter

class Player(abstractCharacter.AbstractCharacter):
    '''
    class representing main character
    '''
    def __init__(self) -> None:
        super().__init__(avatar = '\U0000c6c3')

    def __str__(self):
        return self.AVATAR
