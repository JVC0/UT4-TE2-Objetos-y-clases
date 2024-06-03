from __future__ import annotations

from cards import Card, Hand
from helpers import shuffle
from roles import Dealer, Player


class Game:
    def __init__(self) -> None:
        self.deck = [
            num + suit
            for suit in ['❤', '♠', '◆', '♣']
            for num in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        ]
        shuffle(self.deck)
        self.pointer = 0

    def deck_cards(self):
        for card in self.deck:
            yield card

    def __iter__(self) -> Game:
        return self

    def __next__(self) -> Card:
        if self.pointer >= len(self.deck):
            raise StopIteration
        card = Card(self.deck[self.pointer])
        self.pointer += 1
        return card

    def get_winner(
        players: list[Player],
        common_cards: list[Card],
        private_cards: list[list[Card]],
    ) -> tuple[Player | None, Hand]:

        return players
