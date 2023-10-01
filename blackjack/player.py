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
    def __init__(self):
        pass 
        
    def get_hand(self):
        pass
    
    def clear_hand(self):
        pass 
    
    def add_card(self):
        pass 
    
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
