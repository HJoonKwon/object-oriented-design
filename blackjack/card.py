from enum import Enum 

class Suit(Enum):
    SPADES, HEARTS, DIAMONDS, CLUBS = 'spades', 'hearts', 'diamonds', 'clubs'

class Card:
    def __init__(self):
        pass 
    
    def get_value(self):
        pass 
    
    def get_suit(self):
        # spades/ hearts / diamonds / clubs 
        pass 