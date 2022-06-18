"""
This file established the card module to be used in card game implementations.
"""

from multiprocessing.sharedctypes import Value


class Card:
    """
    A representation of a card found in a standard playing deck. The suite
    and rank of the card are stored in this object.
    """

    def __init__(self, suite, rank):
        """
        Initializer for the Card class.
        Arguments: suite (str) -- The suite of the card. 
                   rank (str) -- The rank of the card in a standard suite.
        Returns: (Card) -- A new card object.
        """

        self.known_suites = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
        self.known_ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9',
                            '10', 'Jack', 'Queen', 'King']
        if suite not in self.known_suites:
            raise ValueError('This is not a known suite!')
        if rank not in self.known_ranks:
            raise ValueError('This is not a known rank!')
        self.suite = suite
        self.rank = rank


    def __str__(self):
        """
        A string representation of the card, revealing its suite and rank.
        Arguments: None
        Returns: None
        """

        return f"{self.rank} of {self.suite}"

    
    def get_suite(self):
        """
        Returns the suite of the card.
        Arguments: None
        Returns: None
        """

        return self.suite


    def get_rank(self):
        """
        Returns the rank of the card.
        Arguments: None
        Returns: None
        """
        
        return self.rank
