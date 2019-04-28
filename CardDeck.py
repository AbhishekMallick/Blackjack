'''CardDeck class to represent a deck and pull a card out at random'''

import random

class CardDeck:

    nameMap = {
                1:'Ace',
                2:'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine',
                10: 'Ten',
                11: 'Jack',
                12: 'Queen',
                13: 'King'
            }
    
    def __init__(self):
        self.__drawnCards = set()  # hold the cards that have been drawn

    def __getSuit(self, num):
        # change this to switch case later
        if (num == 0):
            return 'Spades'
        elif (num == 1):
            return 'Clubs'
        elif (num == 2):
            return 'Hearts'
        elif (num == 3):
            return 'Diamonds'
        else:
            return f'suit is {num}, which is invalid'

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
        return (suit, card)

    def getName(self, suit, card):
        return f'{self.nameMap[card]} of {self.__getSuit(suit)}'
        


        