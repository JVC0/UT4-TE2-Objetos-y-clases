from __future__ import annotations

from helpers import combinations
from roles import Player,Dealer


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
    def high_card(Player:Player,Dealer:Dealer):
    
    def one_pair(Player:Player,Dealer:Dealer):
    
    def two_pair(comon_cards:list[Card],private_cards:list[Card]):

    def three_of_a_kind(comon_cards:list[Card],private_cards:list[Card]):

    def straight(comon_cards:list[Card],private_cards:list[Card]):
    
    def flush(comon_cards:list[Card],private_cards:list[Card]):
    
    def four_of_a_kind(comon_cards:list[Card],private_cards:list[Card]):
        
    def full_house(comon_cards:list[Card],private_cards:list[Card]):

    def straight_flush(comon_cards:list[Card],private_cards:list[Card]):

     #all the cards same colour and num


    def __init__(
        self,
    ) -> None:
        pass
    def high_card():
        return None
    def calc_best_hands(self):
        return combinations()
