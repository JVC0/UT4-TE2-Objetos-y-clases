from __future__ import annotations

from cards import Card
from helpers import shuffle


class Dealer:
    def __init__(self, common_cards: list[Card] | None) -> None:
        self.deck = [
            num + suit
            for suit in ['❤', '♠', '◆', '❤']
            for num in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        ]
        shuffle(self.deck)
        if common_cards == 0:
            self.common_cards = [
                Card(self.deck[4]),
                Card(self.deck[5]),
                Card(self.deck[6]),
                Card(self.deck[7]),
                Card(self.deck[8]),
            ]
        else:
            self.common_cards = common_cards


class Player:

    def __init__(self, name: str, private_cards: list[Card] | None):
        self.name = name
        self.private_cards = private_cards
