from __future__ import annotations

from cards import Card, Hand
from roles import Dealer, Player


def get_winner(
    players: list[Player],
    common_cards: list[Card],
    private_cards: list[list[Card]],
) -> tuple[Player | None, Hand]:
    dealer = Dealer()
    dealer.common_cards = common_cards
    player1, player2 = players
    player1.private_cards, player2.private_cards = private_cards
    hand_player1 = player1.get_best_hand()
    hand_player2 = player2.get_best_hand()
    if hand_player1 > hand_player2:
        winner = (player1, hand_player1)
    elif hand_player1 < hand_player2:
        winner = (player2, hand_player2)
    elif hand_player1 == hand_player2:
        winner = (None, hand_player1)
    return winner
