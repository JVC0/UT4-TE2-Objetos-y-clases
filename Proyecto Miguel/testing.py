from __future__ import annotations

from helpers import shuffle


class Game:
    def __init__(self) -> None:
        self.deck = [
            num + suit
            for suit in ['❤', '♠', '◆', '♣']
            for num in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        ]
        shuffle(self.deck)
        self.pointer = 0

    def deck_cards(self):
        for card in self.deck:
            yield card

    def __iter__(self) -> Game:
        return self

    def __next__(self) -> Card:
        if self.pointer >= len(self.deck):
            raise StopIteration
        card = Card(self.deck[self.pointer])
        self.pointer += 1
        return card

    def get_winner(
        players: list[Player],
        common_cards: list[Card],
        private_cards: list[list[Card]],
    ) -> tuple[Player | None, Hand]:
        pass


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
    def __init__(self, name: str, dealer: Dealer, private_cards: list[Card] | None = None):
        self.name = name
        if private_cards is None:
            self.private_cards = [
                Card(next(dealer.deck_generator)),
                Card(next(dealer.deck_generator)),
            ]
        else:
            self.private_cards = private_cards


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

    def __init__(self, dealer: Dealer, player: Player) -> None:
        self.all_cards = dealer.common_cards + player.private_cards

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
        pass

    def full_house(self):
        pass

    def straight_flush(self):
        pass


import unittest
from unittest.mock import MagicMock, patch


class TestGame(unittest.TestCase):
    @patch('helpers.shuffle', MagicMock())
    def test_game_initialization(self):
        game = Game()
        self.assertEqual(len(game.deck), 52)
        self.assertEqual(game.pointer, 0)

    @patch('helpers.shuffle', MagicMock())
    def test_dealer_initialization(self):
        dealer = Dealer()
        self.assertEqual(len(dealer.common_cards), 5)

    @patch('helpers.shuffle', MagicMock())
    def test_player_initialization(self):
        dealer = Dealer()
        player = Player(name="Player1", dealer=dealer)
        self.assertEqual(len(player.private_cards), 2)

    def test_card_comparison(self):
        card1 = Card("10♠")
        card2 = Card("J♠")
        card3 = Card("10♠")
        self.assertTrue(card1 < card2)
        self.assertTrue(card1 == card3)
        self.assertTrue(card2 > card1)

    def test_hand_evaluations(self):
        common_cards = [Card("10♠"), Card("J♠"), Card("Q♠"), Card("K♠"), Card("A♠")]
        private_cards = [Card("2❤"), Card("3◆")]
        hand = Hand(common_cards, private_cards)
        self.assertTrue(hand.straight_flush())
        self.assertFalse(hand.four_of_a_kind())
        self.assertFalse(hand.full_house())


if __name__ == "__main__":
    unittest.main()
