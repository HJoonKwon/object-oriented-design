from enum import Enum


class Suit(Enum):
    SPADES, HEARTS, DIAMONDS, CLUBS = "spades", "hearts", "diamonds", "clubs"


class Card:
    def __init__(self, value: int, suit: Suit):
        assert 1 <= value <= 10, f"value = {value} should be >=1 and <=10"
        assert isinstance(suit, Suit), "invalid suit"

        self._value = value
        self._suit = suit

    def get_value(self) -> int:
        return self._value

    def get_suit(self) -> Suit:
        return self._suit

    def __repr__(self):
        return f"({self._value},{self._suit})"
