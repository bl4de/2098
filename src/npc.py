from . import abstractCharacter
import src.utils.keyboard as keyboard

class NPC(abstractCharacter.AbstractCharacter):
    '''
    class representing NPC
    '''

    def __init__(self, avatar = None, color = None) -> None:
        '''
        create NPC skeleton
        '''
        if avatar is None:
            self.avatar = '\U0001304c'
        if color is None:
            self.color = keyboard.colors['yellow']

        super().__init__(avatar = avatar)
