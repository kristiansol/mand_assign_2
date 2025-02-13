class HandOfCards:
    """
    A class to represent a hand of playing cards.
    Attributes:
    -----------
    cards : list
        A list of card objects representing the hand.
    Methods:
    --------
    is_flush():
        Checks if all cards in the hand have the same suit.
    __str__():
        Returns a string representation of the hand of cards.
    """
    def __init__(self, cards=None):
        if cards is None:
            cards = []  
        self.cards = cards

    def is_flush(self):
        if len(self.cards) < 5:
            return False
        first_suit = self.cards[0].get_suit()
        return all(card.get_suit() == first_suit for card in self.cards)

    def __str__(self):
        return ', '.join(card.get_as_string() for card in self.cards)
    
    def add_card(self, card):
        self.cards.append(card)
    
    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)
        else:
            raise ValueError("Kortet finnes ikke i hånden")
    
    

    
