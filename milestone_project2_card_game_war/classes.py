# Classes of Card Game
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# Card


class Card():

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit.lower().title()
        self.rank = rank.lower().title()
        self.value = values[self.rank]

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

# Deck


class Deck():

    def __init__(self) -> None:
        all_cards = []
        for suit in suits:
            for rank in ranks:
                all_cards.append(Card(suit, rank))
        self.all_cards = all_cards

    def __str__(self) -> str:
        return str([str(card) for card in self.all_cards])

    def shuffle(self) -> None:
        random.shuffle(self.all_cards)

    def deal_one(self) -> Card:
        return self.all_cards.pop()

    def has_more_cards(self) -> bool:
        return len(self.all_cards) > 0

# Player


class Player():

    def __init__(self, name: str) -> None:
        self.name = name
        self.cards = []

    def remove_one(self) -> Card:
        return self.cards.pop(0) if len(self.cards) > 0 else None

    def add_cards(self, new_cards) -> None:
        if type(new_cards) == type([]):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)

    def __str__(self) -> str:
        return f"Player {self.name} has {len(self.cards)} cards: {[str(card) for card in self.cards]}"

    def has_more_cards(self) -> bool:
        return len(self.cards) > 0
