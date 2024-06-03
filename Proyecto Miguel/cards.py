from __future__ import annotations

from helpers import combinations
from roles import Dealer, Player


class Card:
    RANK_ORDER = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, card_values: str) -> None:
        self.rank, self.suit = card_values[:-1], card_values[-1]

    def __eq__(self, other: Card) -> bool:
        return Card.RANK_ORDER.index(self.rank) == Card.RANK_ORDER.index(other.rank)

    def __lt__(self, other: Card) -> bool:
        return Card.RANK_ORDER.index(self.rank) < Card.RANK_ORDER.index(other.rank)

    def __gt__(self, other: Card) -> bool:
        return Card.RANK_ORDER.index(self.rank) > Card.RANK_ORDER.index(other.rank)

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"


class Hand:
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 4
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8

    def __init__(self) -> None:
        self.all_cards = Dealer.common_cards + Player.private_cards

    def high_card(self):
        pass

    def one_pair(self):
        for card in self.all_cards:
            if self.all_cards.count(card.rank) == 2:
                return True
        return Hand.high_card(self.all_cards)

    def two_pair(self):
        num_of_pairs = 0
        for card in self.all_cards:
            if self.one_pair(self.all_cards):
                num_of_pairs += 1
            if num_of_pairs == 2:
                return True

    def three_of_a_kind(self):
        for card in self.all_cards:
            if self.all_cards.count(card.rank) == 3:
                return True
        return Hand.two_pair(self.all_cards)

    def straight(self):
        first_card = sorted(self.all_cards)[0].rank
        for card in self.all_cards[1:]:
            if first_card + 1 != card.rank:
                return Hand.three_of_a_kind(self.all_cards)
            first_card += 1
        return True

    def flush(self):
        suits = {'❤': [], '♠': [], '◆': [], '♣': []}
        for card in self.all_cards:
            suits[card.suit].append(card)
        for suit_cards in suits.values():
            if len(suit_cards) >= 5:
                return True
        return Hand.straight(self.all_cards)

    def four_of_a_kind(self):
        ranks = [card.rank for card in self.all_cards]
        for rank in ranks:
            if ranks.count(rank) == 4:
                return True
        return Hand.flush(self.all_cards)

    def full_house(self):
        ranks = [card.rank for card in self.all_cards]
        has_three = False
        has_pair = False
        for rank in set(ranks):
            if ranks.count(rank) == 3:
                has_three = True
            elif ranks.count(rank) == 2:
                has_pair = True
        if all(has_pair, has_three):
            return True
        return Hand.four_of_a_kind(self.all_cards)

    def straight_flush(self):
        if not self.flush():
            return False
        suits = {'❤': [], '♠': [], '◆': [], '♣': []}
        for card in self.all_cards:
            suits[card.suit].append(card)
        for suit_cards in suits.values():
            if len(suit_cards) >= 5:
                rank_indices = sorted([Card.RANK_ORDER.index(card.rank) for card in suit_cards])
                for i in range(len(rank_indices) - 4):
                    if rank_indices[i : i + 5] == list(range(rank_indices[i], rank_indices[i] + 5)):
                        return True
        return False
