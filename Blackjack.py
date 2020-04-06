import random

# '''
# Blackjack
# Author: Keir McGlinn-Shaw
# Verions 0.1
# '''

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
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

# Class which represents the players hand of cards in this game
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values.get(card.rank)
        if card.rank == "Ace":
            self.aces += 1
    '''
    Use deck.deal()?

    Take random card from deck?

    Need to pass a deck object into init?
    '''

    def adjust_for_aces(self):
        while self.aces > 0 and self.value > 21:
            self.value -= 10
            self.aces -= 1
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
        self.total += self.bet
        self.bet = 0

    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0

    def push_bet(self):
        self.bet = 0
        

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
            if bet > chips.total:
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

    while not (choice == 'hit' or choice == 'stand'):
        choice = input("Please enter 'hit' or 'stand' to either hit or stand: ").lower()

    if choice == 'hit':
        hit(deck, hand)
    elif choice == 'stand':
        playing = False


def show_some(player, dealer):
    # Print all but the first of the dealer's cards
    print("Dealer's deck: [Hidden card] ", end="")
    for i in range(1, len(dealer.cards)):
        print(f" [{dealer.cards[i]}] ", end="")
    
    print("\n\nPlayer's deck: ", end="")
    for card in player.cards:
        print(f" [{card}] ", end="")

    print("\n")

def show_all(player, dealer):
    print("\n\nDealer's deck: ", end="")
    for card in dealer.cards:
        print(f" [{card}] ", end="")
    
    print("\n")

    print("\n\nPlayer's deck: ", end="")
    for card in player.cards:
        print(f" [{card}] ", end="")

    print("\n")


def bust(hand):
    if hand.value > 21:
        is_bust = True
        hand.adjust_for_aces()
        if hand.value > 21:
            return True
        else:
            return False
    else:
        return False

def player_busts(chips):
    chips.lose_bet()
    print("The player has bust!!! The dealer wins!")

def player_wins(chips):
    chips.win_bet()
    print("The player has won!!!")

def dealer_busts(chips):
    chips.win_bet()
    print("The dealer has bust!!! The player wins!") 
def dealer_wins(chips):
    chips.lose_bet()
    print("The dealer has won!!!")
 
def push(chips):
    chips.push_bet()
    print("It is a draw!!! The bet is pushed!")


while True:
    # Print an opening statement
    playing = True
    print("Welcome to Blackjack!\n\In this game you will play 1v1 the computer which will act as the dealer")
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    player = Hand()
    dealer = Hand()
    # player_bust = False

    for i in range(2):
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())
        
    # Set up the Player's chips
    chips = Chips()
    
    # Prompt the Player for their bet
    chips.bet = take_bet()
    
    # Show cards (but keep one dealer card hidden)
    show_some(player, dealer)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if bust(player):
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if bust(player):
        player_busts(chips)
    else:
        show_all(player, dealer)
        while dealer.value < 17:
            hit(deck, dealer)
            print("Dealer hits. Hands now show: ")
            show_all(player, dealer)
        else:
            if bust(dealer):
                dealer_busts(chips)
            elif player.value > dealer.value:
                player_wins(chips)
            elif player.value < dealer.value:
                dealer_wins(chips)
            elif player.value == dealer.value:
                push(chips)
            else:
                print("Debugging error. Error calculating the final winner") # TODO Remove
            
    
        # Show all cards
    
        # Run different winning scenarios
        
    
    # Inform Player of their chips total
    print(f"Your total chips after this round are: {chips.total}") 
    
    # Ask to play again
    choice = ""
    while not(choice == 'yes' or choice == 'no'):
        choice = input("Do you wish to play again? Enter 'yes' or 'no': ").lower()

    if choice == 'yes':
        continue
    else:
        break