import sys
from ..util.classes.cardgames import Deck

class Blackjack(object):
    """Class definition for Blackjack object"""
    def __init__(self, num_players = 1):
        self.deck = Deck(preshuffle = True)
        self.dealer_hand = []
        self.players = {}
        for player in range(num_players):
            players[player] = []



def main(args):
    print("Hello, World! My name is John Louie and this is my" +
        " first attempt at writing Blackjack! Welcome :)")
    if len(args) > 0:
        num_players = int(args[0])
    else:
        num_players = int(input("How many players do you want" +
                                " to have?: "))
    blackjack_game = Blackjack(num_players)


main(sys.argv[1:])