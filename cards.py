class Card:
    #[2,3,4,5,6,7,8,9,10,J,Q,K,A] Posible atributo de clase 
    def __init__(self, card_values:str) -> None:
        self.rank, self.suit=card_values
        #self.value= Posible atributo de prueba

class Hand:

    def __init__(self) -> None:
        pass