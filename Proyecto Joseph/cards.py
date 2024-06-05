from __future__ import annotations

from helpers import shuffle


class Card:
    RANK_ORDER = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

    def __init__(self, card_values) -> None:
        self.rank, self.suit = card_values[:-1], card_values[-1]

    def __eq__(self, other: Card) -> bool:  # type: ignore
        return self.rank == other.rank

    def __gt__(self, other: Card) -> bool:
        return Card.RANK_ORDER.index(self.rank) < Card.RANK_ORDER.index(other.rank)

    def __repr__(self) -> str:
        return f"{self.rank}{self.suit}"

class Deck:

    def __init__(self):
        self.deck = [
            Card(num + suit)
            for suit in ['❤', '♠', '◆', '♣']
            for num in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        ]

    def deck_shuffle(self) -> None:
        shuffle(self.deck)

    def __iter__(self):
        for card in self.deck:
            yield card

class Hand:
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8

    def __init__(self, cards: list) -> None:
        self.hand = sorted(cards)
        self.suits = tuple(card.suit for card in self)
        self.ranks = tuple(card.rank for card in self)
        self.cat, self.cat_rank = self.find_category()

    def highest_card(self):
        return self[-1]

    def high_card(self):
        self.cat = Hand.HIGH_CARD
        return self.cat, self.highest_card()

    def one_pair(self):
        for card in self.hand:
            if self.ranks.count(card.rank) == 2:
                self.cat = Hand.ONE_PAIR
                return self.cat, card.rank
        return None

    def two_pair(self):
        num_of_pairs = 0
        highest_cards = []
        for rank in set(self.ranks):
            if self.ranks.count(rank) == 2:
                num_of_pairs += 1
                highest_cards.append(rank)
        if num_of_pairs == 2:
            self.cat = Hand.TWO_PAIR
            return self.cat, tuple(highest_cards)
        return None

    def three_of_a_kind(self):
        for rank in set(self.ranks):
            if self.ranks.count(rank) == 3:
                self.cat = Hand.THREE_OF_A_KIND
                return self.cat, rank
        return None

    def straight(self):
        sorted_ranks = sorted(self.ranks)
        first_rank_idx = Card.RANK_ORDER.index(sorted_ranks[0])
        if Card.RANK_ORDER[first_rank_idx : first_rank_idx + 5] == sorted_ranks:
            self.cat = Hand.STRAIGHT
            return self.cat, self.highest_card()
        return None

    def four_of_a_kind(self):
        for rank in set(self.ranks):
            if self.ranks.count(rank) == 4:
                self.cat = Hand.FOUR_OF_A_KIND
                return self.cat, rank
        return None

    def full_house(self):
        ranks = [card.rank for card in self.hand]
        has_three = False
        has_pair = False
        highest_cards = []
        for rank in set(ranks):
            if ranks.count(rank) == 3:
                has_three = True
                highest_cards.append(rank)
            elif ranks.count(rank) == 2:
                has_pair = True
                highest_cards.append(rank)
        if has_pair and has_three:
            self.cat = Hand.FULL_HOUSE
            return self.cat, tuple(highest_cards)
        return None

    def flush(self):
        suits = {'❤': [], '♠': [], '◆': [], '♣': []}
        for card in self.hand:
            suits[card.suit].append(card)
        for suit_cards in suits.values():
            if len(suit_cards) == 5:
                self.cat = Hand.FLUSH
                self.cat_rank = max(suit_cards)
                return self.cat, self.highest_card()
        return None

    def straight_flush(self):
        if self.flush() and self.straight():
            self.cat = Hand.STRAIGHT_FLUSH
            return self.cat, self.highest_card()
        return None

    def find_category(self) -> tuple[int, str | tuple[str, str]]:
        if match := self.straight_flush():
            return match
        if match := self.four_of_a_kind():
            return match
        if match := self.full_house():
            return match
        if match := self.flush():
            return match
        if match := self.straight():
            return match
        if match := self.three_of_a_kind():
            return match
        if match := self.two_pair():
            return match
        if match := self.one_pair():
            return match
        return self.high_card()

    def __contains__(self, card):
        return card in self.hand

    def __repr__(self):
        return f'{self.hand}'

    def __getitem__(self, index: int):
        return self.hand[index]

    def __iter__(self):
        return HandIterator(self)

    def __eq__(self, other: Hand) -> bool:  # type: ignore
        return self.cat == other.cat

    def __gt__(self, other: Hand) -> bool:
        if self.cat != other.cat:
            return self.cat > other.cat
        else:
            return self.highest_card() > other.highest_card()

class HandIterator:
    def __init__(self, hand: Hand) -> None:
        self.pointer = 0
        self.hand = hand

    def __next__(self):
        if self.pointer >= len(self.hand.hand):
            raise StopIteration
        else:
            card = self.hand[self.pointer]
            self.pointer += 1
            return card

    