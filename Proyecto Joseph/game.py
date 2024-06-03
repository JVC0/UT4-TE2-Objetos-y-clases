from __future__ import annotations

from cards import Card, Hand
from helpers import shuffle
from roles import Dealer, Player


class Game:
    def __init__(self) -> None:
        self.deck = []

    def deck_cards(self):  # puede mejorarse
        self.deck = [
            num + suit
            for suit in ['❤', '♠', '◆', '❤']
            for num in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        ]
        shuffle(self.deck)
        for card in self.deck:
            yield card

    def __iter__(self) -> object:
        return self

    def __next__(self) -> Game:
        pointer = 0

        if pointer >= self.deck:

            raise StopIteration

        game = Game(str(pointer))

        pointer += 1

        return game
