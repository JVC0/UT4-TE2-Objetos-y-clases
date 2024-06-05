from __future__ import annotations
from helpers import shuffle, combinations


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
    
def get_winner(
    players: list[Player],
    common_cards: list[Card],
    private_cards: list[list[Card]],
) -> tuple[Player | None, Hand]:
    dealer = Dealer()
    Dealer.common_cards = common_cards
    player1, player2 = players
    player1.private_cards, player2.private_cards = private_cards
    hand_player1 = player1.get_best_hand()
    hand_player2 = player2.get_best_hand()
    if hand_player1 > hand_player2:
        winner = (player1, hand_player1)
    elif hand_player1 < hand_player2:
        winner = (player2, hand_player2)
    else:
        winner = (None, hand_player1)
    return winner


pytest.param(
        [Player('Player 1'), Player('Player 2')],
        [Card('A❤'), Card('K◆'), Card('Q♣'), Card('9❤'), Card('3♣')],
        [[Card('6◆'), Card('3◆')], [Card('J◆'), Card('4◆')]],
        'Player 1',
        [Card('3◆'), Card('3♣'), Card('A❤'), Card('K◆'), Card('Q♣')],
        Hand.ONE_PAIR,
        '3',
        id="1",
    ),
pytest.param(
        [Player('Player 1'), Player('Player 2')],
        [Card('A◆'), Card('K❤'), Card('K◆'), Card('10❤'), Card('3◆')],
        [[Card('4◆'), Card('3❤')], [Card('9◆'), Card('2♠')]],
        'Player 1',
        [Card('K❤'), Card('K◆'), Card('3❤'), Card('3◆'), Card('A◆')],
        Hand.TWO_PAIR,
        ('K', '3'),
        id="3",
    ),

pytest.param(
        [Player('Player 1'), Player('Player 2')],
        [Card('Q◆'), Card('10♣'), Card('8❤'), Card('5❤'), Card('3❤')],
        [[Card('A♠'), Card('Q♣')], [Card('J❤'), Card('4❤')]],
        'Player 2',
        [Card('J❤'), Card('8❤'), Card('5❤'), Card('4❤'), Card('3❤')],
        Hand.FLUSH,
        'J',
        id="4",
    ),
pytest.param(
        [Player('Player 1'), Player('Player 2')],
        [Card('K◆'), Card('9❤'), Card('8◆'), Card('7❤'), Card('5♠')],
        [[Card('J♠'), Card('10♣')], [Card('K♠'), Card('Q❤')]],
        'Player 1',
        [Card('J♠'), Card('10♣'), Card('9❤'), Card('8◆'), Card('7❤')],
        Hand.STRAIGHT,
        'J',
        id="6",
    ),
pytest.param(
        [Player('Player 1'), Player('Player 2')],
        [Card('A♠'), Card('Q❤'), Card('9♠'), Card('5♣'), Card('4◆')],
        [[Card('J◆'), Card('10❤')], [Card('K❤'), Card('2❤')]],
        'Player 2',
        [Card('A♠'), Card('K❤'), Card('Q❤'), Card('9♠'), Card('5♣')],
        Hand.HIGH_CARD,
        'A',
        id="11",
    ),
pytest.param(
        [Player('Player 1'), Player('Player 2')],
        [Card('A◆'), Card('Q♠'), Card('Q◆'), Card('10◆'), Card('4◆')],
        [[Card('Q❤'), Card('4♣')], [Card('6◆'), Card('2◆')]],
        'Player 1',
        [Card('Q❤'), Card('Q♠'), Card('Q◆'), Card('4♣'), Card('4◆')],
        Hand.FULL_HOUSE,
        ('Q', '4'),
        id="28",
    ),

pytest.param(
        [Player('Player 1'), Player('Player 2')],
        [Card('Q◆'), Card('9♣'), Card('9♠'), Card('6◆'), Card('4❤')],
        [[Card('K♣'), Card('Q❤')], [Card('J❤'), Card('9❤')]],
        'Player 2',
        [Card('9❤'), Card('9♣'), Card('9♠'), Card('Q◆'), Card('J❤')],
        Hand.THREE_OF_A_KIND,
        '9',
        id="35",
    ),
pytest.param(
        [Player('Player 1'), Player('Player 2')],
        [Card('10♣'), Card('9♠'), Card('8♣'), Card('7♣'), Card('6♣')],
        [[Card('8♠'), Card('4♣')], [Card('9❤'), Card('9♣')]],
        'Player 2',
        [Card('10♣'), Card('9♣'), Card('8♣'), Card('7♣'), Card('6♣')],
        Hand.STRAIGHT_FLUSH,
        '10',
        id="816",
    ),