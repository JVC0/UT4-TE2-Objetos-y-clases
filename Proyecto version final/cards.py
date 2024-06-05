from __future__ import annotations

from helpers import shuffle


class Card:
    RANK_ORDER = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, card_values: str) -> None:
        self.rank, self.suit = card_values[:-1], card_values[-1]

    def __eq__(self, other) -> bool:
        return Card.RANK_ORDER.index(self.rank) == Card.RANK_ORDER.index(other.rank)

    def __lt__(self, other: Card) -> bool:
        return Card.RANK_ORDER.index(self.rank) < Card.RANK_ORDER.index(other.rank)

    def __gt__(self, other: Card) -> bool:
        return Card.RANK_ORDER.index(self.rank) > Card.RANK_ORDER.index(other.rank)

    def __str__(self) -> str:
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

    def __init__(self, all_cards) -> None:
        self.hand = all_cards

        self.cat, self.cat_rank = self.find_category()

    def highest_card(self):
        return self.sort_cards(self)[-1]

    def high_card(self):
        self.cat = Hand.HIGH_CARD
        return self.cat, self.highest_card

    def one_pair(self):
        for card in self:
            if self.count(card[:-1]) == 2:
                self.cat = Hand.ONE_PAIR
                return self.cat, card
        return None

    def two_pair(self):
        num_of_pairs = 0
        highest_cards = []
        for card in self:
            if self.one_pair(self):
                num_of_pairs += 1
                highest_cards.append(card)
            if num_of_pairs == 2:
                self.cat = Hand.TWO_PAIR
                return self.cat, highest_cards
        return None

    def three_of_a_kind(self):
        ranks = [card[:-1] for card in self]
        for rank in ranks:
            if ranks.count(rank) == 3:
                self.cat = Hand.THREE_OF_A_KIND
                return self.cat, rank
        return None

    def straight(self):
        first_card = self.sort_cards(self)[0][0]
        all_cards = self.sort_cards(self)
        for card in all_cards[1:]:
            if int(Card.RANK_ORDER.index(first_card)) + 1 != Card.RANK_ORDER.index(card):
                return False
            first_card += 1
        self.cat = Hand.STRAIGHT
        return self.cat, self.highest_card(self)

    def four_of_a_kind(self):
        ranks = [card[:-1] for card in self]
        for rank in ranks:
            if ranks.count(rank) == 4:
                self.cat = Hand.FOUR_OF_A_KIND
                return self.cat, rank
        return None

    def full_house(self):
        ranks = [card[:-1] for card in self]
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
            return self.cat, highest_cards
        return None

    def flush(self):
        suits = {'❤': [], '♠': [], '◆': [], '♣': []}
        for card in self:
            suits[card[-1]].append(card)
        for suit_cards in suits.values():
            if len(suit_cards) == 5:
                self.cat = Hand.FLUSH
                self.cat_rank = max(suit_cards)
                return self.cat, self.highest_card(self)
        return None

    def straight_flush(self):
        if self.flush(self) and self.straight(self):
            self.cat = Hand.STRAIGHT_FLUSH
            return self.cat, self.highest_card
        return None

    def sort_cards(self, cards):
        rank_order = Card.RANK_ORDER
        sorted_cards = sorted(cards, key=lambda card: rank_order.index(card[0]))
        return sorted_cards

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

    def __iter__(self):
        for card in self.hand:
            yield card

    def __eq__(self, other) -> bool:
        return self.find_category()[0] == other.find_category()[0]

    def __lt__(self, other: Hand) -> bool:
        return self.find_category()[0] < other.find_category()[0]

    def __gt__(self, other: Hand) -> bool:
        return self.find_category()[0] > other.find_category()[0]
