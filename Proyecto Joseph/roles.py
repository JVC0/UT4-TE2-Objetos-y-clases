from __future__ import annotations
from helpers import shuffle
from cards import Card

class Dealer:
    def __init__(self, common_cards: Card = 0) -> None:
        self.deck = shuffle([num + suit for suit in ['❤', '♠', '◆', '❤'] for num in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']])
        if common_cards == 0:
            self.common_cards = [Card(self.deck[4]), Card(self.deck[5]), Card(self.deck[6]), Card(self.deck[7]), Card(self.deck[8])]
        else:
            self.common_cards = common_cards
        

class Player:

    def __init__(self, name: str,private_cards:Card):
        self.name = name
        self.private_cards=private_cards


