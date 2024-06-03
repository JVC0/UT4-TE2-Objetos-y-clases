from cards import Card, Hand
from roles import Player,Dealer
from helpers import shuffle

class game:
    def __init__(self) -> None:
        pass
    
    def deck(): # puede mejorarse
        deck = [
            num + suit
            for suit in ['❤', '♠', '◆', '❤']
            for num in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        ]
        shuffle(deck)
        for card in deck:
            yield card
    def get_winner(
        players: list[Player],
        common_cards: list[Card],
        private_cards: list[list[Card]],) -> tuple[Player | None, Hand]: