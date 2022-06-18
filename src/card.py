"""
The class represents a singular card in a blackjack deck.
"""

from multiprocessing.sharedctypes import Value


class Card:
    """
    This class defines the Card with given attributes such as card suite and 
    card type. This class is intended to be used with the deck module.
    """

    def __init__(self, suite, type):
        """
        Initializer for the Card class.
        Arguments: suite (str) -- The suite of the card. Must be grammatically singular
                   type (str) -- The type of the card in a standard suite.
        """

        self.known_suites = ['Club', 'Spade', 'Heart', 'Diamond']
        self.known_types = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9',
                            '10', 'Jack', 'Queen', 'King']
        if suite not in self.known_suites:
            raise ValueError('This is not a known suite!')
        if type not in self.known_types:
            raise ValueError('This is not a known type!')
        self.suite = suite
        self.type = type

    def __str__(self):

        return f"{self.suite}: {self.type}"
