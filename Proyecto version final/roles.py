from __future__ import annotations

from cards import Deck, Hand
from helpers import combinations


class Dealer:
    common_cards = []

    def __init__(self) -> None:
        self.deck = Deck()


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.private_cards = []

    def get_best_hand(self):
        all_cards = self.private_cards + Dealer.common_cards
        all_combinations = combinations(all_cards, n=5)
        best_hand = Hand(next(all_combinations))
        current_hand = None
        for hand in all_combinations:
            current_hand = Hand(hand)
            if current_hand > best_hand:
                best_hand = hand
            elif current_hand == best_hand:
                if current_hand.highest_card > best_hand.highest_card:
                    best_hand = hand
        return best_hand
