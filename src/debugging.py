from cgi import test
from card import Card
from deck import Deck


test_deck = Deck()
test_deck.remove_card('Spades', '2')
test_deck.remove_card('Hearts', '10')
test_deck.add_card('Spades', '2')
test_deck.add_card('Hearts', '10')
test_deck.display()