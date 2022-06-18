"""
This file establishes the deck module to be used in card game implementations.
"""
from card import Card
import random


class Deck:
    """
    A representation of a USPCC standard 52 card deck which allows for the
    addition and removal of cards, as well as multiple forms of display
    for visualizing the deck.
    """

    def __init__(self):
        """
        Initializer for a standard 52 card deck.
        Arguments: None
        Returns: None
        """
        
        self.known_suites = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
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
        self.order = []
        self.standard_order()
        

    def display(self):
        """
        A string representation of the card, showing all cards and noting
        missing cards from their own suite.
        Arguments: None
        Returns: None
        """

        for suite in self.known_suites:
            cards = self.suites[suite]
            for card in cards:
                print(card)

    
    def display_suite(self, suite):
        """
        Displays the condition of specific desired suite.
        Arguments: suite (str) -- The suite to display
        Returns: None
        """

        if suite not in self.known_suites:
            raise ValueError("This suite is not recognized! Please input one "
                             + "of: Clubs, Spades, Hearts, Diamonds.")
        print("-" * 79)
        print(f"All cards of {suite}.")
        print("-" * 79)
        for card in self.suites[suite]:
            print(card)

    
    def display_rank(self, rank):
        """
        Displays all cards of a given rank.
        Arguments: rank (str) -- The rank to display
        Returns: None
        """
        
        if rank not in self.known_ranks:
            raise ValueError("This rank is not recognized!")
        
        print("-" * 79)
        print(f"All cards of {rank} rank.")
        print("-" * 79)
        
        for suite in self.known_suites:
            cards = self.suites[suite]
            for card in cards:
                if card.get_rank() == rank:
                    print(card)
    

    def display_order(self):
        """
        Displays the order of the current deck of cards.
        Arguments: None
        Returns: None
        """

        print("-" * 79)
        print("Card Order")
        print("-" * 79)
        for idx, card in enumerate(self.order):
            print(f"{str(idx + 1).zfill(2)}: {card}")


    def standard_order(self):
        """
        Places all cards in order.
        Arguments: None
        Returns: None
        """
        for card in self.suites['Spades']:
            self.order.append(card)
        for card in self.suites['Diamonds']:
            self.order.append(card)
        for card in self.suites['Clubs']:
            self.order.append(card)
        for card in self.suites['Hearts']:
            self.order.append(card)


    def shuffle_order(self):
        """
        Shuffles the current order of cards.
        Arguments: None
        Returns: None
        """

        random.shuffle(self.order)

    
    def add_card(self, suite, rank):
        """
        Adds a card back into the deck if it does not already exist. The
        new card is added to the back of the stack.
        Arguments: suite (str) -- the suite the new card belongs to
                   rank (str) -- the rank of the new card
        Returns: None
        """

        if suite not in self.known_suites:
            raise ValueError("This suite is not recognized!")
        if rank not in self.known_ranks:
            raise ValueError("This rank is not recognized!")

        if self.card_ispresent(suite, rank):
            raise ValueError("This card already exists in the deck!")
        
        new_card = Card(suite, rank)
        for idx in range(len(self.order)):
            if self.order[idx] == None:
                self.order[idx] = new_card
                break
        
        self.suites[suite].insert(self.rankmapping[rank], new_card)


    def remove_card(self, suite, rank):
        """
        Removes a card in the deck and shifts all cards forward.
        Arguments: suite (str) -- The suite the card belongs to
                   rank (str) -- The rank of the card
        Returns: None
        """

        if suite not in self.known_suites:
            raise ValueError("This suite is not recognized!")
        if rank not in self.known_ranks:
            raise ValueError("This rank is not recognized!")

        if not self.card_ispresent(suite, rank):
            raise ValueError("This card is already removed from the deck!")
        
        idx = 0
        for card in self.order:
            if card.get_suite() == suite and card.get_rank() == rank:
                self.order[idx] = self.order[idx + 1]
                idx += 1
                break
            idx += 1

        idx_2 = 0
        for i in range(51 - idx):
            self.order[i + idx] = self.order[i + idx + 1]
            idx2 = idx + i
            if self.order[i + idx + 1] == None:
                idx = i + idx
                break
        
        for i in range(51 - idx2):
            self.order[i + idx2 + 1] = None
        
        self.suites[suite].remove(self.return_card(suite, rank))
    

    def card_ispresent(self, suite, rank):
        """
        Returns whether the card is present in the deck.
        Arguments: suite (str) -- The suite the card belongs to
                   rank (str) -- The rank of the card
        Returns: (bool) -- Whether the card is present
        """

        for card in self.suites[suite]:
            if card != None and card.get_rank() == rank:
                return True
        return False


    def return_card(self, suite, rank):
        """
        Returns the card object in a deck.
        Arguments: suite (str) -- The suite the card belongs to
                   rank (str) -- The rank of the card
        Returns: (Card) -- The corresponding Card object if present
        """

        if self.card_ispresent(suite, rank):
            for card in self.suites[suite]:
                if card.get_suite() == suite and card.get_rank() == rank:
                    return card