from __future__ import annotations
from helpers import combinations
from roles import Dealer, Player


class Card:
    CARD_RANK = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

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
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8

    def __init__(self, player:Player,dealer:Dealer) -> None:
        self.best_hand = Hand.get_best_hand(player.private_cards+dealer.common_cards)
        
        self.cat, self.cat_rank = self.find_category(self.best_hand)

    @property
    def highest_card(self,hand:tuple):
        return self.sort_cards(hand)[-1]

    def high_card(self):
        self.cat = Hand.HIGH_CARD
        return self.cat, self.highest_card

    def one_pair(self,hand:tuple):
        for card in hand:
            if hand.count(card[:-1]) == 2:
                self.cat = Hand.ONE_PAIR
                return self.cat, card
        return None

    def two_pair(self,hand:tuple):
        num_of_pairs = 0
        highest_cards = ()
        for card in  hand:
            if Hand.one_pair(hand):
                num_of_pairs += 1
                highest_cards.append(card)
            if num_of_pairs == 2:
                self.cat = Hand.TWO_PAIR
                return self.cat, highest_cards
        return None

    def three_of_a_kind(self,hand:tuple):
        ranks = [card[:-1] for card in hand]
        for rank in ranks:
            if ranks.count(rank) == 3:
                self.cat = Hand.THREE_OF_A_KIND
                return self.cat, rank
        return None

    def straight(self,hand:tuple):
        first_card = int(self.sort_cards(hand)[0][0])
        all_cards = self.sort_cards(hand)
        for card in all_cards[1:]:
            if Card.CARD_RANK.index(first_card) + 1 != Card.CARD_RANK.index(card):
                return False
            first_card += 1
        self.cat = Hand.STRAIGHT
        return self.cat, self.highest_card(hand)

    def four_of_a_kind(self,hand:tuple):
        ranks = [card[:-1] for card in hand]
        for rank in ranks:
            if ranks.count(rank) == 4:
                self.cat = Hand.FOUR_OF_A_KIND
                return self.cat, rank
        return None

    def full_house(self,hand:tuple):
        ranks = [card[:-1] for card in hand]
        has_three = False
        has_pair = False
        highest_cards = ()
        for rank in set(ranks):
            if ranks.count(rank) == 3:
                has_three = True
                highest_cards.append(rank)
            elif ranks.count(rank) == 2:
                has_pair = True
                highest_cards.append(rank)
        if all(has_pair, has_three):
            self.cat = Hand.FULL_HOUSE
            return self.cat, highest_cards
        return None

    def flush(self,hand:tuple):
        suits = {'❤': [], '♠': [], '◆': [], '♣': []}
        for card in hand:
            suits[card[-1]].append(card)
        for suit_cards in suits.values():
            if len(suit_cards) == 5:
                self.cat = Hand.FLUSH
                self.cat_rank = max(suit_cards)
                return self.cat, self.highest_card(hand)
        return None

    def straight_flush(self,hand:tuple):
        if self.flush(hand) and self.straight(hand):
            self.cat = Hand.STRAIGHT_FLUSH
            return self.cat, self.highest_card
        return None
    
    def get_best_hand(self,all_cards:list[Card]):
        all_combinations = combinations(all_cards,5)
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
    
    def sort_cards(cards):
        rank_order = "23456789TJQKA"
        sorted_cards = sorted(cards, key=lambda card: rank_order.index(card[0]))
        return sorted_cards

    def find_category(self,hand:tuple) -> tuple[int, str|tuple[str, str]]:
        if match := self.straight_flush(hand):
            return match
        if match := self.four_of_a_kind(hand):
            return match
        if match := self.full_house(hand):
            return match
        if match := self.flush(hand):
            return match
        if match := self.straight(hand):
            return match
        if match := self.three_of_a_kind(hand):
            return match
        if match := self.two_pair(hand):
            return match
        if match := self.one_pair(hand):
            return match
        return self.high_card(hand)

    def __eq__(self, other: Hand) -> bool:
        return self.find_category()[0] == other.find_category()[0]

    def __lt__(self, other: Hand) -> bool:
        return self.find_category()[0] < other.find_category()[0]
    
    def __gt__(self, other: Hand) -> bool:
        return self.find_category()[0] > other.find_category()[0]