'''CardDeck class to represent a deck and pull a card out at random'''

import random

class CardDeck:

    def __init__(self):
        self.__drawnCards = set()  # hold the cards that have been drawn

    def __getSuit(self, num):
        # change this to switch case later
        if (num == 0):
            return 'Spade'
        elif (num == 1):
            return 'Club'
        elif (num == 2):
            return 'Heart'
        elif (num == 3):
            return 'Diamond'
        else:
            return 'Invalid'

    def getACard(self):
        found = False

        while not found:
            # choose of suit
            suit = random.randint(0, 3)
            # choose a card
            card = random.randint(1, 13)
            if (suit, card) not in self.__drawnCards:
                found = True
                self.__drawnCards.add((suit, card))
        return (self.__getSuit(suit), card)

        