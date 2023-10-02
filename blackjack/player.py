from abc import ABC, abstractmethod
from card import Card 

class Hand:
    def __init__(self):
        self._cards = []  
        self._score = 0 
    
    def add_card(self, card: Card):
        assert isinstance(card, Card), 'invalid card instance'
        self._cards.append(card)
    
    def get_cards(self) -> list[Card]:
        return self._cards
    
    def get_score(self) -> int:
        return self._score 
    
    def print(self):
        print(f"Hand: \n")
        print(f"  cards: {self.get_cards()} \n")
        print(f"  score: {self.get_score()} \n")

class Player(ABC):
    def __init__(self, hand: Hand):
        self._hand = hand  
        
    def get_hand(self) -> Hand:
        return self._hand 
    
    def clear_hand(self):
        self._hand = Hand()  
    
    def add_card(self, card: Card):
        self._hand.add_card(card) 
    
    @abstractmethod
    def make_move(self):
        pass 

class UserPlayer(Player):
    def __init__(self):
        pass 
    
    def make_move(self):
        pass 
   

class Dealer(Player):
    def __init__(self):
        pass 
    
    def make_move(self):
        pass 
