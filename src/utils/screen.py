import os


class Screen:
    '''
    Screen utils
    '''

    def __init__(self) -> None:
        pass

    @staticmethod
    def clear_screen() -> None:
        os.system("clear")
