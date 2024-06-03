from cards import Card, Hand
from roles import Player,Dealer

class game:
    def __init__(self) -> None:
        pass

    def get_winner(
        players: list[Player],
        common_cards: list[Card],
        private_cards: list[list[Card]],) -> tuple[Player | None, Hand]: