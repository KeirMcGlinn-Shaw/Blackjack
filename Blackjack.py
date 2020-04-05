'''
Blackjack
Author: Keir McGlinn-Shaw
Verions 0.1
'''


# Need:
# Deck of cards
#   Use import random to shuffle the pack
# Collection of chips
# Player
# Dealer

import random

# Set to store the values of all suits in a deck of cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
# Set to store the values of all ranks in a deck of cards (excluding jokers)
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
# Dictionary to map each rank in a deck of cards to a numeric value
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

# TODO
playing = True
total_chips = 100

# Class which represents a card in this game
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Class which represents a deck of cards in this game
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)
                
    def __str__(self):
        return "\n".join(map(str, self.deck))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        # hand = []
        # for i in range(2):
        #     hand.append(random.choice(self.deck))

        # return hand
        
        # TODO should remove the card from the deck as well
        return random.choice(self.deck)

# Class which represents the players hand of cards in this game
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
    '''
    Use deck.deal()?

    Take random card from deck?

    Need to pass a deck object into init?
    '''

    def adjust_for_aces(self):
        if self.value > 21: # TODO May not be needed as this may be the condition by which the method is called
            num_aces = self.aces # TODO have some counter of how many aces have been changed? Move while loop checking value, to hit()
            while num_aces > 0 and value > 21:
                value -= 10
                num_aces -= 1
        '''
        if value > 21
        num_aces = self.aces
        while num_aces > 0 and value > 21:
            value -= 10
            num_aces -= 1


        OR

        if value > 21:
            if self.aces == 1:
                self.value -= 10

        '''

class Chips:
    def __init__(self):
        self.total = total_chips
        self.bet = 0

    def win_bet(self):
        pass

    def lose_bet(self):
        pass


# Functions


def take_bet(): # TODO Does this need to take a Chips object as an argument?
    incorrect = True
    while incorrect:
        try:
            bet = int(input("Please enter the amount you wish to bet: "))
        except ValueError:
            print("That won't work. Please try again")
            continue
        else:
            if bet > Chips.total:
                print("You don't have enough chips for that bet. Try again")
                continue
            else:
                print("Thank you")
                incorrect = False
    return bet

def hit(deck, hand):
    hand.add_card(deck.deal())
    if hand.value > 21:
        hand.adjust_for_aces

def hit_or_stand(deck, hand):
    global playing

    choice = ""

    while choice != 'hit' or choice != 'stand':
        choice = input("Please enter 'hit' or 'stand' to either hit or stand").lower()

    if choice == 'hit':
        hit(deck, hand)
    elif choice == 'stand':
        playing = False


def show_some(player, dealer):
    pass

def show_all(player, dealer):
    pass




def player_busts():
    pass

def player_wins():
    pass

def dealer_busts():
    pass
    
def dealer_wins():
    pass
    
def push():
    pass

# card = Card('Hearts', 'Two')

deck = Deck()

print(deck)