from __future__ import annotations

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

    def __init__(self, cards:Card) -> None:
        self.cards=cards
        self.best_hand = combination
        self.cat, self.cat_rank = get_best_hand()
        self.cat = None
        self.cat_rank = None

    def rank_freq(self) -> dict[str, int]: 
        result = {}
        for card in self.cards:
            if card.rank in result:
                result[card.rank] = result.get(card.rank) + 1
            else:
                result[card.rank] = 1
        return result

    @property
    def highest_card(self):
        return max(self.all_cards)

    def high_card(self):
        self.cat = Hand.HIGH_CARD
        return self.cat, self.highest_card

    def one_pair(self):
        for card in self.all_cards:
            if self.all_cards.count(card.rank) == 2:
                self.cat = Hand.ONE_PAIR
                return self.cat, self.hig
        return None

    def two_pair(self):
        num_of_pairs = 0
        for card in self.all_cards:
            if Hand.one_pair():
                num_of_pairs += 1
            if num_of_pairs == 2:
                self.cat = Hand.TWO_PAIR
                return self.cat
        return

    def three_of_a_kind(self):
        for card in self.all_cards:
            if self.all_cards.count(card.rank) == 3:
                self.cat = Hand.THREE_OF_A_KIND
                return self.cat, 
        return Hand.two_pair()

    def straight(self):
        first_card = sorted(self.all_cards)[0].rank
        for card in self.all_cards[1:]:
            if first_card + 1 == card.rank:
                return Hand.three_of_a_kind()
            first_card += 1
        self.cat = Hand.STRAIGHT
        return self.cat

    def four_of_a_kind(self):
        ranks = [card.rank for card in self.all_cards]
        for rank in ranks:
            if ranks.count(rank) == 4:
                self.cat = Hand.FOUR_OF_A_KIND
                return self.cat
        return Hand.full_house()

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
            self.cat = Hand.FULL_HOUSE
            return self.cat
        return Hand.flush()

    def flush(self):
        suits = {'❤': [], '♠': [], '◆': [], '♣': []}
        for card in self.all_cards:
            suits[card.suit].append(card)
        for suit_cards in suits.values():
            if len(suit_cards) >= 5:

                self.cat = Hand.FLUSH
                self.cat_rank = max(suit_cards)
                return self.cat, self.highest_card
        return None
        # return Hand.straight(self.all_cards)

    def straight_flush(self):
        if self.flush() and self.straight():
            self.cat = Hand.STRAIGHT_FLUSH
            return self.cat, self.highest_card
        return None

    def find_category(self) -> tuple[int, str|tuple[str, str]]:
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








5, 5, 9, 10, J

def one_pair():
if 2 in hoola.values():
    for rank, ratio in hoola.items():
        if ratio == 2
            return Hand.ONE_PAIR, rank
return None
hoola = {
    '5': 2,
    '9': 1,
    '10': 1,
    'J': 1
}

6,6,6,1,1  (6, 1)

{
    '6': 3
    '1': 2
}

