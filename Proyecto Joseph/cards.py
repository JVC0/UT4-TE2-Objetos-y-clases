class Card:
    #[2,3,4,5,6,7,8,9,10,J,Q,K,A] Posible atributo de clase
    def __init__(self, card_values: str) -> None:
        self.rank, self.suit = list(card_values)
        #self.value= Posible atributo de prueba


class Hand:
    HIGH_CARD=1
    ONE_PAIR=2
    TWO_PAIR=3
    THREE_OF_A_KIND=4
    STRAIGHT=5
    FLUSH=6
    FULL_HOUSE=7
    FOUR_OF_A_KIND
    STRAIGHT_FLUSH
    def __init__(self, cat: list) -> None:
        self.cat = ('HIGH_CARD', 'ONE_PAIR', 'TWO_PAIR', 'THREE_OF_A_KIND',
                    'STRAIGHT', 'FLUSH', 'FULL_HOUSE', 'FOUR_OF_A_KIND',
                    'STRAIGHT_FLUSH')

    # def HIGH_CARD(self):

    # def ONE_PAIR(self):

    # def TWO_PAIR(self):

    # def THREE_OF_A_KIND(self):

    # def STRAIGHT(self):

    # def FLUSH(self):

    # def FULL_HOUSE(self):

    # def FOUR_OF_A_KIND(self):

    # def STRAIGHT_FLUSH(self):
