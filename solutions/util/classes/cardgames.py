
from random import shuffle

class Card(object):
    """Base Card class for card games"""
    CARD_SUITS = { 1: "spades", 2: "clubs", 3: "hearts", 4: "diamonds"}
    CARD_VALUES = { "ace": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
            "jack": 11, "queen": 12, "king": 13}
    
    def __init__(self, value = None, suit = None):
        self.value = value
        self.suit = suit
        if value == CARD_VALUES("ace") or value > CARD_VALUES("ten"):
            self.isFace = True
        else: 
            self.isFace = False


    def to_string(self):
        if self.value == None or self.suit == None:
            print("Card not completely defined")
        else:
            print(CARD_VALUES(self.value) + " of " + CARD_SUITS(self.suit))



class CardHand(object):
    """description of Hand class"""
    def __init__(self, hand_size = None):
        self.cards = {}
        self.hand_size = hand_size
    
    def add_card(self, card):
        pass

    def remove_card(self, card):
        pass


class Deck(object):
    """description of Deck class"""
    NUM_CARDS = 52
    NUM_PER_SUIT = 13
    def __init__(self, preshuffle = False, number_of_decks = 1):
        self.createDeck(preshuffle, number_of_decks)
        self.cards_out = set() 
    
    def create_deck(self, preshuffle):
        self.deck = []
        suit = 0
        for card in range(NUM_CARDS): # iterate from 0 to 52
            if card % NUM_PER_SUIT == 0:
                suit = suit + 1
            deck.append(Card(card, suit))
        if preshuffle:
            self.shuffle_deck()
        return deck

    def shuffle_deck(self):
        self.deck.shuffle()

    def draw_card(self):
        if len(self.deck) == 0:
            print("The deck is currently empty. Return card(s) in " +
                "order to draw another card")
        else:
            card = self.deck.pop()
            self.cards_out.add(card)
            return card

    def return_card(self, card):
        if len(self.deck) == NUM_CARDS:
            print("The deck is currently full. All the deck's card(s)" +
                " are currently drawn.")
        elif card not in self.cards_out:
            print("Please return a card that was from the original deck")
        else:
            self.deck.append(card)
            self.cards_out.remove(card)