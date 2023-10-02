from abc import ABC, abstractmethod
from card import Card


class Hand:
    def __init__(self):
        self._cards = []
        self._score = 0

    def add_card(self, card: Card):
        assert isinstance(card, Card), "invalid card instance"
        self._cards.append(card)
        if card.get_value() == 1:
            self._score += 11 if self._score + 11 < 21 else 1
        else:
            self._score += card.get_value()

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
    def __init__(self, hand: Hand, money: int = 0):
        super().__init__(hand)
        self._money = money

    def get_money(self):
        return self._money

    def add_money(self, money: int):
        self._money += money

    def bet_money(self, money: int):
        self._money -= money

    def make_move(self):
        return str(input("Draw? y/n: ")) == "y"


class Dealer(Player):
    def __init__(self, hand: Hand, target_score: int = 17):
        super().__init__(hand)
        self._target_score = target_score
        self._hand = hand

    def make_move(self):
        if self._hand.get_score() < self._target_score:
            return True
        else:
            return False
