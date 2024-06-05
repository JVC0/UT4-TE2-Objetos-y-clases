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
        best_hand = None
        for hand in combinations(all_cards, n=5):
            hand = Hand(list(hand))
            if not best_hand or hand > best_hand:
                best_hand = hand
            elif hand == best_hand:
                if hand.highest_card() > best_hand.highest_card():
                    best_hand = hand
        return best_hand
