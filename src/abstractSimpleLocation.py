class AbstractSimpleLocation:

    def __init__(self, symbol = '') -> None:
        '''
        Simple location represents non-explorable elements
        on world's matrix, thus they do not need self.MATRIX
        property
        '''
        self.TYPE = 'simple'
        self.SYMBOL = symbol i''f symbol is not '' else self.SYMBOL

    def render(self):
        '''
        renders symbol representing simple location symbol
        '''
        print(self.SYMBOL, end='')
