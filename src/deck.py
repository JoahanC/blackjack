"""
This file establishes the deck class which simulates a standard card deck.
"""
from card import Card


class Deck:

    def __init__(self):
        """
        Initializer for a standard 52 card deck.
        """
        
        self.known_suites = ['Club', 'Spade', 'Heart', 'Diamond']
        self.known_ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9',
                            '10', 'Jack', 'Queen', 'King']
        self.rankmapping = {'Ace': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5,
                            '7': 6, '8': 7, '9': 8, '10': 9, 'Jack': 10, 
                            'Queen': 11, 'King': 12}
        self.suites = {}
        for suite in self.known_suites:
            self.suites[suite] = [None] * 13
            for rank in self.known_ranks:
                self.suites[suite][self.rankmapping[rank]] = Card(suite, rank)
        


    def display(self):
        """
        A string representation of the card, showing all cards and noting
        missing cards from their own suite.
        """
        for suite in self.known_suites:
            cards = self.suites[suite]
            for card in cards:
                print(card)

    
    def display_suite(self, suite):
        """
        Displays the condition of specific desired suite.
        """
        if suite not in self.known_suites:
            raise ValueError("This suite is not recognized! Please input one "
                             + "of: Club, Spade, Heart, Diamond.")
        for card in self.suites[suite]:
            print(card)
        
        
