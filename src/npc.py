from . import abstractCharacter

class NPC(abstractCharacter.AbstractCharacter):
    '''
    class representing NPC
    '''

    def __init__(self, avatar = None) -> None:
        '''
        create NPC skeleton
        '''
        if avatar is None:
            self.AVATAR = '\U0001304c'
        super().__init__(avatar = avatar)
