all_cards = ['A❤', '9❤', '2❤', '5❤', '4❤']

suits = {'❤': [], '♠': [], '◆': [], '♣': []}
for card in all_cards:
    suits[card.suit].append(card)
for suit_cards in suits.values():
    if len(suit_cards) >= 5:

        cat = 5
        cat_rank = max(suit_cards)
        print(cat, cat_rank)
