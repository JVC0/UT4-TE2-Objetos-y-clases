from __future__ import annotations

from cards import Card
from game import Game


class Dealer:
    def __init__(self, common_cards: list[Card] | None = None) -> None:
        self.game_instance = Game()
        self.deck_generator = self.game_instance.deck_cards()
        if common_cards is None:
            self.common_cards = [
                Card(next(self.deck_generator)),
                Card(next(self.deck_generator)),
                Card(next(self.deck_generator)),
                Card(next(self.deck_generator)),
                Card(next(self.deck_generator)),
            ]
        else:
            self.common_cards = common_cards


class Player:
    def __init__(self, name: str, private_cards: list[Card] | None = None):
        self.name = name
        if private_cards is None:
            self.private_cards = [
                Card(next(Dealer.deck_generator)),
                Card(next(Dealer.deck_generator)),
            ]
        else:
            self.private_cards = private_cards

    def get_best_hand(self):
        all_cards = privadas + comunes
        combinaciones = combinations(all_cards, n=5)
        best_hand = Hand(next(combinaciones))
        for hand in combinaciones:
            hand = Hand(hand)
            if hand > best_hand:
                best_hand = hand