# The main game file - where everything comes together.
import time

from CardDeck import CardDeck

class Game:
    def __init__(self):
        self.endGame = False
        self.playerScore = 0
        self.dealerScore = 0
        self.cardDeck = CardDeck()    # the game holds a deck of cards.

    def __hitOrStay(self):
            while True:
                try:
                    playerInput = input('Do you want to hit(h) or stay(s)? ')
                    if (playerInput == 'h' or playerInput == 's'):
                        break
                    else:
                        print('Please enter a valid input')
                except:
                    print('Please enter a valid input')
                finally:
                    return playerInput


    def __addOneOrEleven(self):
        inp = 1
        while True:
            try:
                inp = int(input('Add one(1) or eleven(11)? '))
                if (inp == 1 or inp == 11): 
                    break
            except:
                print('Please input a valid input (1 or 11) ')
        return inp
    
    def __playerTurn(self):
        # get next card and add to player score
        card = self.cardDeck.getACard()
        # if the next card is Ace, and both 1 and 11 fit in the score ask the player whether to treat is as 1 or 11
        # TODO: add helper to get card name from deck
        print(f'The card drawn is {card[1]} of {card[0]}') 
        if (card[1] == 1 and self.playerScore <= 10):
            self.playerScore += self.__addOneOrEleven()
        elif(card[1] >= 10):
            self.playerScore += 10
        else:
            self.playerScore += card[1]
        
        print(f'Your current score is {self.playerScore}.\n')
        # if the score is beyond 21 - player loses - bust.
        if (self.playerScore > 21):
            print(f". That's a bust! You lose.")
            self.endGame = True
        if (self.playerScore == 21):
            print(f"BLACKJACK!! You Win!!")
            self.endGame = True

    def __dealerTurn(self):
        print(f'Alright your final score is {self.playerScore}.\n')
        print('The dealer is going to start drawing now!')

        while (self.dealerScore <= self.playerScore):
            time.sleep(3)
            print('Dealer hits')
            card = self.cardDeck.getACard()
            print(f'The card drawn is {card[1]} of {card[0]}')
            if (card[1] == 1):
                if (self.dealerScore <= 10):
                    self.dealerScore += 11
                else:
                    self.dealerScore += 1

            elif (card[1] >= 10):
                self.dealerScore += 10
            else:
                self.dealerScore += card[1]

            print(f'Current dealer score is {self.dealerScore}.\n')
            
            if (self.dealerScore > 21):
                print(f'The dealer has busted! You Win!!')
                self.endGame = True
            elif (self.dealerScore > self.playerScore):
                print(f'The dealer wins. You lose.')
                self.endGame = True

    def run(self):
        # first - we need to decide whose turn it is.
        while True:
            if self.endGame:
                break

            playerInput = self.__hitOrStay()

            if playerInput == 'h': #hit
                self.__playerTurn()
            
            elif playerInput == 's': #stay
                self.__dealerTurn()
                    

                        

if __name__ == '__main__':
    while True:
        print('\n')
        print('-' * 80)
        print('Welcome to a game of Blackjack!')
        print('-' * 80)
        
        game = Game()
        game.run()
        playAgain = input('want to play again (y/n)?')
        if (playAgain == 'y'):
            continue
        else:
            break



