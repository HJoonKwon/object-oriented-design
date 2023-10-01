from abc import ABC, abstractmethod

class Hand:
    def __init__(self):
        pass 
    
    def add_card(self):
        pass 
    
    def get_cards(self):
        pass 
    
    def get_score(self):
        pass 
    
    def print(self):
        pass 

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
