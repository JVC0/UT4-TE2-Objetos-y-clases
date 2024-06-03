from __future__ import annotations

from cards import Card
from game import game


class Dealer:
    def __init__(self, common_cards: list[Card] | None) -> None:

        if common_cards is None:
            self.common_cards = [
                Card(next(game.card)),
                Card(next(game.card)),
                Card(next(game.card)),
                Card(next(game.card)),
                Card(next(game.card)),
            ]
        else:
            self.common_cards = common_cards


class Player:

    def __init__(self, name: str, private_cards: list[Card] | None):
        self.name = name
        if private_cards is None:
            self.private_cards = [Card(next(game.card)), Card(next(game.card))]
        else:
            self.private_cards = private_cards
