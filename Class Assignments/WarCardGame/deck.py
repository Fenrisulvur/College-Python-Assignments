import random

class Card:
    def __init__(self, suit, number):
        self._suit = suit
        self._number = number

    def __repr__(self):
        return str(self.number) + self.suit

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if str(number).upper() in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
            self._number = number
        else:
            print("That's not a valid number!")


class Deck:
    def __init__(self):
        self._cards = []
        self.populate()
        #print(self._cards)

    def populate(self):
        suits = ["H", "C", "D", "S"]
        numbers = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self._cards = [Card(s, n) for s in suits for n in numbers]

    def Shuffle(self):
        random.shuffle(self._cards)
        #print(self._cards)

    def Deal(self, players):
        count = len(self._cards) // len(players)
        print(count,"Cards shall be handed out to keep hands even.")
        for player in players:
            for i in range(count):
                choice = self._cards.pop(random.randrange(len(self._cards)))
                player.AddCard(choice)


class Hand:
    def __init__(self):
        self._cards = []

    @property
    def cards(self):
        return self._cards

    def Play(self):
        return self._cards.pop()

    def AddCard(self, card):
        self._cards.append(card)

    def PrintHand(self):
        print(self._cards)

    def __repr__(self):
        return str(self._cards)



