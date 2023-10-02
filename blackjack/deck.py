import random
from card import Card, Suit


class Deck:
    def __init__(self):
        self._cards = []
        for suit in Suit:
            for i in range(1, 14):
                card = Card(i, suit) if i < 11 else Card(10, suit)
                self._cards.append(card)
        self.shuffle()

    def draw(self):
        return self._cards.pop(0)

    def shuffle(self):
        for i in range(len(self._cards)):
            j = random.randrange(0, len(self._cards) - 1)
            self._cards[i], self._cards[j] = self._cards[j], self._cards[i]
